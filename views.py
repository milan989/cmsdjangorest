from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes,APIView
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .models import User,Post,Likes
from .serializers import UserSerializer, PostSerializer ,LikesSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

class view_posts(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def view_likes(request):
    likes = Likes.objects.all()
    serializer = LikesSerializer(likes, many=True)
    return Response(serializer.data)

class view_all(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        likes = Likes.objects.all()
        serializer1 = LikesSerializer(likes, many=True)
        return Response(serializer.data + serializer1.data)



@api_view(['POST'])
def add_posts(request):
    posts = PostSerializer(data=request.data)
    if posts.is_valid():
        posts.save()
        return Response(posts.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_likes(request):
    likes = LikesSerializer(data=request.data)
    if likes.is_valid():
        likes.save()
        return Response(likes.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_user(request, id):
    users = User.objects.get(id=id)
    data = UserSerializer(instance=users, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def update_post(request, id):
    posts = Post.objects.get(id=id)
    data = PostSerializer(instance=posts, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    posts = Post.objects.get(id=id)
    posts.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def update_like(request, id):
    likess = Likes.objects.get(id=id)
    data = LikesSerializer(instance=likess, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_like(request, id):
    likess = Likes.objects.get(id=id)
    likess.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


