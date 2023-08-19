from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .models import News, Comment
from .forms import NewsForm, CommentForm, SignUpForm

class NewsView(View):
    def get(self, request):
        news = News.objects.order_by("-created_at").all()
        context = {'news': news}
        return render(request, 'news/all_news.html', context)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
@method_decorator(permission_required('news.add_news', login_url='/login/'), name='dispatch')
class Add_NewsView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'news/add_news.html', {'form': form})
    
    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.auth = request.user
            news.save()
            return redirect(reverse('news:all_news'))

        return render(request, 'news/add_news.html', {'form': form})

class DetailVeiw(View):
    def get(self, request, news_id):
        news = get_object_or_404(News, pk=news_id)
        comments = Comment.objects.filter(news=news_id).order_by("-created_at").all()
        form = CommentForm()
        context = {'news': news, 'comments': comments, 'form': form}
        return render(request, 'news/detail.html', context)

@method_decorator(login_required(login_url='/login/'), name='dispatch')
@method_decorator(permission_required('news.add_comment', login_url='/login/'), name='dispatch')
class CommentView(View):
    def post(self, request, news_id):
        news = get_object_or_404(News, pk=news_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.auth = request.user
            comment.save()
            return redirect(reverse('news:detail', args=(news_id,)))
        
        comments = Comment.objects.filter(news=news_id).order_by("-created_at").all()
        context = {'news': news, 'comments': comments, 'form': form}
        return render(request, 'news/detail.html', context)

@permission_required('news.delete_news', login_url='/login/')
def delete_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        if news.auth == request.user or request.user.has_perm('news.delete_news'):
            news.delete()
    return redirect(reverse('news:all_news'))

@permission_required('news.delete_comment', login_url='/login/')
def delete_comment(request, news_id, comment_id):
    news = get_object_or_404(News, pk=news_id)
    comment = get_object_or_404(Comment, pk=comment_id, news=news)
    if request.method == 'POST':
        if comment.auth == request.user or request.user.has_perm('news.delete_comment'):
            comment.delete()
    return redirect(reverse('news:detail', args=(news_id,)))

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/sign-up.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='defult')
            group.user_set.add(user)
            login(request, user)
            return redirect(reverse('news:all_news'))
        return render(request, 'registration/sign-up.html', {'form': form})
    