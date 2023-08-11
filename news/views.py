from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import News, Comment

# Create your views here.

def all_news(request):
    news = News.objects.order_by("-created_at").all()
    context = {'news': news}
    return render(request, 'news/all_news.html', context)

def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    comments = get_list_or_404(Comment, news=news)
    context = {'news': news, 'comments': comments}
    return render(request, 'news/detail.html', context)

def add_news(request):
    news_title = request.POST["title"]
    news_content = request.POST["content"]

    news = News(title=news_title, content=news_content)
    news.save()
    return HttpResponseRedirect(reverse('news:all_news'))

def add_comments(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    new_content = request.POST['content']
    news.comment_set.create(content=new_content)
    return HttpResponseRedirect(reverse('news:detail', args=str(news_id)))