from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import News, Comment
from .forms import NewsForm, CommentForm

class NewsView(View):
    def get(self, request):
        news = News.objects.order_by("-created_at").all()
        context = {'news': news}
        return render(request, 'news/all_news.html', context)

class Add_NewsView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'news/add_news.html', {'form': form})
    
    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:all_news'))

        return render(request, 'news/add_news.html', {'form': form})

class DetailVeiw(View):
    def get(self, request, news_id):
        news = get_object_or_404(News, pk=news_id)
        comments = Comment.objects.filter(news=news_id).order_by("-created_at").all()
        form = CommentForm()
        context = {'news': news, 'comments': comments, 'form': form}
        return render(request, 'news/detail.html', context)

class CommentView(View):
    def post(self, request, news_id):
        news = get_object_or_404(News, pk=news_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(content=form.cleaned_data['content'], news=news)
            comment.save()
            return redirect(reverse('news:detail', args=(news_id,)))
        
        comments = Comment.objects.filter(news=news_id).order_by("-created_at").all()
        context = {'news': news, 'comments': comments, 'form': form}
        return render(request, 'news/detail.html', context)
