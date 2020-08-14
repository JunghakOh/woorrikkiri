from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content, Comment, FAQ, Answer
from .forms import ContentForm, CommentForm, FAQForm, AnswerForm
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    posts = Content.objects.all
    return render(request, 'main/home.html', {'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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
    comment_list = Comment.objects.filter(post=post)
    answer_list = Answer.objects.filter(post=post)
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
            answer.published_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('detail', pk=pk)
    else:
        comment_form = CommentForm()
        answer_form = AnswerForm()
    return render(request, 'main/detail.html', {'post': post, 'comment_list': comment_list, 'comment_form': comment_form, 'answer_list':answer_list, 'answer_form':answer_form})


def edit(request, index):
    post = get_object_or_404(Content, pk=index)
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', index=post.pk)
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

def faq(request):
    faq = FAQ.objects.all
    return render(request, 'main/faq.html', {'faq_list':faq})

def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'main/faq_detail.html', {'faq':faq})

def payment(request):
    return render(request, 'main/payment.html')