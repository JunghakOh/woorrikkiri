from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content, Comment, FAQ, Answer, Subject
from .forms import ContentForm, CommentForm, FAQForm, AnswerForm, SubjectForm
from django.shortcuts import get_object_or_404
from accounts.models import User

#---------------------popbill------by junghak
# -*- coding: utf-8 -*-
from django.shortcuts import render
from popbill import EasyFinBankService, PopbillException, ContactInfo, JoinForm, CorpInfo
from woorrikkiri import settings
# settings.py 작성한 LinkID, SecretKey를 이용해 EasyFinBankService 서비스 객체 생성
easyFinBankService = EasyFinBankService(settings.LinkID, settings.SecretKey)
# 연동환경 설정값, 개발용(True), 상업용(False)
easyFinBankService.IsTest = settings.IsTest
# 인증토큰 IP제한기능 사용여부, 권장(True)
easyFinBankService.IPRestrictOnOff = settings.IPRestrictOnOff
# 팝빌 API 서비스 고정 IP 사용여부(GA), true-사용, false-미사용, 기본값(false)
easyFinBankService.UseStaticIP = settings.UseStaticIP
def requestJob(request):
    try:
        CorpNum = "6630801510"
        UserID = "metis08"
        BankCode = "0004" 
        AccountNumber = "45700101462642"               # 시작일자, 날짜형식(yyyyMMdd)
        SDate = "20200820"
        EDate = "20200821"
        result = easyFinBankService.requestJob(CorpNum, BankCode, AccountNumber,SDate, EDate, UserID)
        return render(request, 'main/response.html', {'result': result})
    except PopbillException as PE:
        return render(request, 'main/response.html', {'code': PE.code, 'message': PE.message})
def getJobState(request):
    """
    수집 요청 상태를 확인합니다.
    - https://docs.popbill.com/easyfinbank/python/api#GetJobState
    """
    try:
        # 팝빌회원 사업자번호
        CorpNum = "6630801510"

        # 팝빌회원 아이디
        UserID = "metis08"

        # 수집요청(requestJob) 호출시 발급받은 작업아이디
        jobID = "020082117000000004"

        response = easyFinBankService.getJobState(CorpNum, jobID, UserID)

        #return render(request, 'main/GetJobState.html', {'response': response})
        return render(request, 'main/GetJobState.html', {'result': result})
    except PopbillException as PE:
        return render(request, 'main/exception.html', {'code': PE.code, 'message': PE.message})
def search(request):
    """
    거래내역의 수집 결과를 조회합니다.
    - https://docs.popbill.com/easyfinbank/python/api#Search
    """
    try:
        # 팝빌회원 사업자번호
        CorpNum = "6630801510"

        # 팝빌회원 아이디
        UserID = "metis08"

        # 수집요청(requestJob)시 발급받은 작업아이디
        JobID = "020082117000000004"

        # 거래유형 배열, [I-입금 / O-출금]
        TradeType = ["I", "O"]

        # 조회 검색어, 입금/출금액, 메모, 적요 like 검색
        SearchString = ""

        # 페이지번호
        Page = 1

        # 페이지당 목록개수, 최대값 1000
        PerPage = 10

        # 정렬방향 [D-내림차순 / A-오름차순]
        Order = "D"

        response = easyFinBankService.search(CorpNum, JobID, TradeType, SearchString,
            Page, PerPage, Order, UserID)

        #return render(request, 'main/Search.html', {'response': response})
        return render(request, 'main/Search.html', {'result': response})
    except PopbillException as PE:
        return render(request, 'main/exception.html', {'code': PE.code, 'message': PE.message})
#-------------------------------
# Create your views here.
def home(request):
    posts = Content.objects.all
    return render(request, 'main/home.html', {'posts_list':posts})
    
# def agreement(request):
#     return render(request, 'agreement.html')

# def private_info(request):
#     return render(request, 'private_info.html')
    
def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = ContentForm()
    return render(request, 'main/new.html', {'form': form})

def ask(request):
    posts = Content.objects.all
    return render(request, 'main/ask.html', {'posts_list':posts})

def detail(request, pk):
    post = get_object_or_404(Content, pk=pk)
    #post = super().save(Content, commit=False, pk=pk)
    # post.writer = request.user # <- 질문자만 수정/삭제 가능 + 답변하기 기능에 문제 생김!
    comment_list = Comment.objects.filter(post=post)
    answer_list = Answer.objects.filter(post=post)
    answer_count = len(answer_list)
    if request.method == "POST":
        comment_form = CommentForm(request.POST) 
        answer_form = AnswerForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            comment.published_date = timezone.now() 
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.writer = request.user
            answer.published_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('detail', pk=pk)
    else:
        comment_form = CommentForm()
        answer_form = AnswerForm()
    return render(request, 'main/detail.html', {'post': post, 'comment_list': comment_list, 'comment_form': comment_form, 'answer_list':answer_list, 'answer_form':answer_form, 'answer_count':answer_count})


def edit(request, index):
    post = get_object_or_404(Content, pk=index)
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'main/edit.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
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
    return render(request, 'main/payment.html')
