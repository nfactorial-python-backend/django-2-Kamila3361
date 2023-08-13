from django.test import TestCase
from django.urls import reverse

from .models import News, Comment

# Create your tests here.

class NewsModelTests(TestCase):
    def test_has_comments_true(self):
        news = News(title='Is Kamila exist?', content='I do not think so!')
        news.save()
        news.comment_set.create(content='Me too')
        self.assertIs(True, news.has_comments())
        
    def test_has_comments_false(self):
        news = News(title='Is Kamila exist?', content='I do not think so!')
        news.save()
        self.assertIs(False, news.has_comments())

class NewsViewsTest(TestCase):
    def test_all_news(self):
        news1 = News(title='Is Kamila exist?', content='I do not think so!')
        news2 = News(title='Is Madina exist?', content='I think so!')
        news3 = News(title='Stary Kids', content='Stray Kids is the 4th generation idols')

        news1.save()
        news2.save()
        news3.save()

        response = self.client.get(reverse('news:all_news'))

        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual([news3, news2, news1], response.context['news'])
        
    def test_detail(self):
        news = News.objects.create(title='Stary Kids', content='Stray Kids is the 4th generation idols',)
        response = self.client.get(reverse('news:detail', args=(news.id,)))
        self.assertEqual(200, response.status_code)
        self.assertEqual(news, response.context['news'])

    def test_detail(self):
        news = News.objects.create(title='Stary Kids', content='Stray Kids is the 4th generation idols',)
        comment1 = news.comment_set.create(content='Stray kids one love')
        comment2 = news.comment_set.create(content='Stray kids + Stay = Forever')
        comment3 = news.comment_set.create(content='Stray kids one love')

        response = self.client.get(reverse('news:detail', args=(news.id,)))
        self.assertEqual(200, response.status_code)
        self.assertEqual(news, response.context['news'])
        self.assertQuerysetEqual([comment3, comment2, comment1], response.context['comments'])
