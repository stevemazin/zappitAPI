from rest_framework import serializers
from .models import Post, Vote

class PostSerializer (serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()


    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'votes', 'url', 'poster', 'poster_id', 'timestamp']


class VoteSerializer (serializers.ModelSerializer):
    class Meta:
        """These are the fields that the user can set from the frontend"""
        model = Vote
        fields = ['id']