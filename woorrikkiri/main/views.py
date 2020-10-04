from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content, Comment, FAQ, Answer, Subject, Point
from .forms import ContentForm, CommentForm, FAQForm, AnswerForm, SubjectForm, PointForm, ApproveForm, PointPayForm
from django.shortcuts import get_object_or_404
from accounts.models import User
from accounts.forms import UserPointForm

from twilio.rest import Client

import environ
env = environ.Env()
environ.Env.read_env()

account_sid = env('TWILLIO_KEY_ID')
auth_token = env('TWILLIO_TOKEN')

# Create your views here.
def home(request):
    posts = Content.objects.all
    return render(request, 'main/home.html', {'posts_list':posts})
    
# def agreement(request):
#     return render(request, 'agreement.html')

# def private_info(request):
#     return render(request, 'private_info.html')
    
def new(request):
    #user_point = User.objects.all
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        point_form = PointForm(request.POST)
        #approve_form = ApproveForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.published_date = timezone.now()
            post.save()
            if point_form.is_valid():
                point_post = point_form.save(commit=False)
                point_post.post = post
                #point_form.points = post.coffee #커피 잔 수 * 2900 만큼을 포인트 모델에 기록(거래내역 기록용)  point.points = content.coffee*2
                point_post.published_date = timezone.now() #거래내역에 결제한 사람, 날짜를 기록 
                point_post.point_user = request.user
                #if approve_form.is_valid(): #거래가 완전히 승인되었는지 확인  
                point_post.save()
                #user_point.point = (user_point.point) - (post.coffee * 2900)
                request.user.point -= (post.coffee * 2900)
                request.user.save()
                #문자 보내기 구현
                client = Client(account_sid, auth_token)
                message = client.messages \
                .create(
                     body="귀하의 질문이 정상적으로 등록되었습니다. 답변달리면 문자 보낼게요!  우리끼리 팀^_^",
                     from_='+12052728223',
                     to='+82'+request.user.phone_num
                 )
                print(message.sid)

                return redirect('ask')
    else:
        form = ContentForm()
        point_form = PointForm()
    return render(request, 'main/new.html', {'form': form, 'point_form':point_form})

def ask(request):
    posts = Content.objects.all().order_by('-pub_date')
    return render(request, 'main/ask.html', {'posts_list':posts})

def detail(request, pk):
    post = get_object_or_404(Content, pk=pk)
    #post = super().save(Content, commit=False, pk=pk)
    comment_list = Comment.objects.filter(post=post)
    answer_list = Answer.objects.filter(post=post)
    answer_count = len(answer_list)
    if request.method == "POST":
        comment_form = CommentForm(request.POST) 
        answer_form = AnswerForm(request.POST, request.FILES)
        point_form = PointForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            comment.published_date = timezone.now() 
            comment.writer = request.user
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
        if answer_form.is_valid() and not post.respondent:
            answer = answer_form.save(commit=False)
            answer.writer = request.user
            answer.published_date = timezone.now()
            answer.post = post
            answer.save()
            post.respondent = request.user
            post.save()
            # 멘토 포인트 증가
            request.user.point += (post.coffee*2900)
            request.user.save()
            # 포인트 객체 생성
            if point_form.is_valid():
                point_post = point_form.save(commit=False)
                point_post.post = post
                point_post.points*=2900
                point_post.point_user = request.user
                point_post.published_date = timezone.now()
                point_post.approve = True
                point_post.save()
                 #문자 보내기 구현
                client = Client(account_sid, auth_token)
                message = client.messages \
                .create(
                     body="귀하의 질문이 답변 달렸습니다. 확인해보세요! 우리끼리 팀^_^",
                     from_='+12052728223',
                     to='+82'+post.writer.phone_num
                 )
                print(message.sid)
            return redirect('detail', pk=pk)
    else:
        comment_form = CommentForm()
        answer_form = AnswerForm()
    return render(request, 'main/detail.html', {'post': post, 'comment_list': comment_list, 'comment_form': comment_form, 'answer_list':answer_list, 'answer_form':answer_form, 'answer_count':answer_count})

def edit(request, index):
    post = get_object_or_404(Content, pk=index)
    #point_post = get_object_or_404(Point, pk=index)
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES, instance=post)
        #point_form = PointForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            #if point_form.is_valid():
             #   point_post = point_form.save(commit=False)
              #  point_post.post = get_object_or_404(Content, pk=post.pk)
                #point_form.points = post.coffee #커피 잔 수 * 2900 만큼을 포인트 모델에 기록(거래내역 기록용)  point.points = content.coffee*2
               # point_post.published_date = timezone.now() #거래내역에 결제한 사람, 날짜를 기록 
                #point_post.point_user = request.user
                #if approve_form.is_valid(): #거래가 완전히 승인되었는지 확인  
                #point_post.save()
                #user_point.point = (user_point.point) - (post.coffee * 2900)
                #request.user.point = request.user.point - (post.coffee * 2900)
                #request.user.save()   
            return redirect('detail', pk=post.pk)
    else:
        form = ContentForm(instance=post)
        #point_form = PointForm()
    return render(request, 'main/edit.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    request.user.point = request.user.point + (post.coffee * 2900)
    request.user.save()   
    return redirect('ask')

def delete_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('detail', pk=pk)


def about(request):
    return render(request, 'main/about.html')

def about_team(request):
    return render(request, 'main/about_team.html')

def faq(request):
    faq = FAQ.objects.all
    return render(request, 'main/faq.html', {'faq_list':faq})

def payment(request):
    if request.method == 'POST':
        if request.user.is_mento:
            point_form = PointPayForm(request.POST)
        else:
            point_form = PointForm(request.POST)
        if point_form.is_valid():
            point_post = point_form.save(commit=False)
            point_post.published_date = timezone.now()
            point_post.point_user = request.user
            point_post.save()
            return redirect('payment_check')
    else:
        point_form = PointForm()
    return render(request, 'main/payment.html', {'point_form':point_form})

def payment_check(request):
    payment_check = Point.objects.all
    return render(request, 'main/payment_check.html', {'payment_check_list':payment_check})
#---------------------popbill------by junghak
# -*- coding: utf-8 -*-
from django.shortcuts import render
from popbill import EasyFinBankService, PopbillException, ContactInfo, JoinForm, CorpInfo
from woorrikkiri import settings
from datetime import datetime
from django.utils.dateformat import DateFormat


# settings.py 작성한 LinkID, SecretKey를 이용해 EasyFinBankService 서비스 객체 생성
easyFinBankService = EasyFinBankService(settings.LinkID, settings.SecretKey)
# 연동환경 설정값, 개발용(True), 상업용(False)
easyFinBankService.IsTest = settings.IsTest
# 인증토큰 IP제한기능 사용여부, 권장(True)
easyFinBankService.IPRestrictOnOff = settings.IPRestrictOnOff
# 팝빌 API 서비스 고정 IP 사용여부(GA), true-사용, false-미사용, 기본값(false)
easyFinBankService.UseStaticIP = settings.UseStaticIP
def search(request):
    """
    거래내역의 수집 결과를 조회합니다.
    - https://docs.popbill.com/easyfinbank/python/api#Search
    """
    try:
        # 팝빌회원 사업자번호
        CorpNum = "6630801510"
        UserID = "metis08"
        BankCode = "0004" 
        AccountNumber = "45700101462642"              
        # 시작일자, 날짜형식(yyyyMMdd)
        today = DateFormat(datetime.now()).format('Ymd')
        #today = datetime.date.today()  
        SDate = "20200808"#today # 어제 날짜 구해서 넣어야 됨 (오늘 구하다가 에러나서 일단 넘아감, 밤 왜냐하면 11.59분에 결제하면 어제 결제확인 안될수 있음)
        EDate = today              
        # 팝빌회원 아이디
        UserID = "metis08"
        # 수집요청(requestJob)시 발급받은 작업아이디
        JobID = easyFinBankService.requestJob(CorpNum, BankCode, AccountNumber,SDate, EDate, UserID)
        # 거래유형 배열, [I-입금 / O-출금]
        TradeType = ["I"]
        # 조회 검색어, 입금/출금액, 메모, 적요 like 검색
        SearchString = ""
        # 페이지번호
        Page = 1
        # 페이지당 목록개수, 최대값 1000
        PerPage = 10
        # 정렬방향 [D-내림차순 / A-오름차순]
        Order = "D"
        #response = easyFinBankService.getJobState(CorpNum, JobID, UserID)
        response = easyFinBankService.search(CorpNum, JobID, TradeType, SearchString,Page, PerPage, Order, UserID)

        for tradeInfo in response.list:
            print (tradeInfo.remark1,tradeInfo.accIn);

        return render(request, 'main/Search.html', {'response': response})
        
    except PopbillException as PE:
        return render(request, 'main/exception.html', {'code': PE.code, 'message': PE.message})
