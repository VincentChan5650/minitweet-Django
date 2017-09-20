from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (TweetDetailView,
                    TweetListView,
                    TweetCreateView,
                    TweetUpdateView,
                    TweetDeleteView,
                    RetweetView)

app_name = 'tweet'

urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/')),
    url(r'^search/',TweetListView.as_view(), name='search'),
    url(r'^create/$',TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/retweet/$',RetweetView.as_view(), name='retweet'),
    url(r'^(?P<pk>\d+)/edit/$',TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(), name='delete'),

]