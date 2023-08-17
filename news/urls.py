from django.urls import path

from .views import NewsView, DetailVeiw, Add_NewsView, CommentView

app_name = 'news'
urlpatterns = [
    path('', NewsView.as_view(), name='all_news'),
    path('<int:news_id>/', DetailVeiw.as_view(), name='detail'),
    path('add/', Add_NewsView.as_view(), name='add_news'),
    path('<int:news_id>/add', CommentView.as_view(), name='add_comments'),
]