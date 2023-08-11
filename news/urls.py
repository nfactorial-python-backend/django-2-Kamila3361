from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.all_news, name='all_news'),
    path('<int:news_id>/', views.detail, name='detail'),
    path('add/', views.add_news, name='add_news'),
    path('<int:news_id>/add', views.add_comments, name='add_comments'),
]