from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import empty_conent

# Create your models here.
class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators = [empty_conent])
    timestamp = models.DateTimeField(auto_now_add=True)
    linked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, related_name='linked')
    updated = models.DateTimeField(auto_now=True)

    #set the content display in admin page
    def __str__(self):
        return str(self.content)

    # ser redirect page
    def get_absolute_url(self):
        return reverse('tweet:detail', kwargs={'pk':self.pk})

    # the order of the tweet
    class Meta:
        ordering = ['-timestamp']
