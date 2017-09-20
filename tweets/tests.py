from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
from .models import Tweet

User = get_user_model()
class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='vin1111')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content='some content for testing'
        )
        self.assertTrue(self,obj.content == 'some random content')
        self.assertTrue(self,obj.id == 1)
