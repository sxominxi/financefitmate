from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'user')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)