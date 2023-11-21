from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import PostListSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)