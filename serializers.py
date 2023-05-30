from django.db.models import fields
from rest_framework import serializers
from .models import User, Post , Likes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField("like_count")
    class Meta:
        model = Post
        fields = "__all__"

    def like_count(self, obj):
        total_like = Likes.objects.filter(post_id=obj.id).count()
        return total_like


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
