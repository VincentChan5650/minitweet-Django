from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views import View


from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

# Create
class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin, CreateView):
    template_name = 'tweets/create_view.html'
    form_class = TweetModelForm
    login_url = '/admin/'

# update
class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/'
    login_url = '/admin/'

# delete
class TweetDeleteView(LoginRequiredMixin,UserOwnerMixin,DeleteView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/delete_confirm.html'
    model = TweetModelForm
    success_url = reverse_lazy('home')
    login_url = '/admin/'



# retrieve
class TweetDetailView(DetailView):
    # set the template path and name, overring the default
    template_name = 'tweets/detail_view.html'
    # retrieve all the objects in model/db
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)
# list
class TweetListView(LoginRequiredMixin, ListView):
    template_name = 'tweets/list_view.html'
    login_url = '/login/'
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(tweet.get_absolute_url)
