from django.utils.timesince import timesince
from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer

# class ParentTweetModelSerializer(serializers.ModelSerializer):
#     user = UserDisplaySerializer(read_only=True)
#     date_display = serializers.SerializerMethodField()
#     timesince = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Tweet
#         fields = [
#             'id',
#             'user',
#             'content',
#             'timestamp',
#             'date_display',
#             'timesince',
#         ]
#
#     def get_date_display(self, obj):
#         return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")
#
#     def get_timesince(self, obj):
#         return timesince(obj.timestamp) +' ago'
#
#     def get_is_retweet(self, obj):
#         if obj.parent:
#             return True
#         return False


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    # parent = ParentTweetModelSerializer()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) +' ago'

    def get_is_retweet(self, obj):
        if obj.parent:
            return True
        return False