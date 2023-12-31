from django.urls import path

from .views import NewsView, DetailVeiw, Add_NewsView, CommentView, SignUpView, delete_news, delete_comment, ApiNewsView, api_news_detail

app_name = 'news'
urlpatterns = [
    path('', NewsView.as_view(), name='all_news'),
    path('<int:news_id>/', DetailVeiw.as_view(), name='detail'),
    path('add/', Add_NewsView.as_view(), name='add_news'),
    path('<int:news_id>/add', CommentView.as_view(), name='add_comments'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('<int:news_id>/delete', delete_news, name='delete'),
    path('<int:news_id>/<int:comment_id>/delete', delete_comment, name='delete_comment'),
    path('api/news', ApiNewsView.as_view(), name='Apiaddnews'),
    path('api/news/<int:pk>', api_news_detail.as_view(), name='api_news_detail'),

]