from django.shortcuts import render
from blog.models import Blog, Series, Category, Comment
from rest_framework.viewsets import ModelViewSet
from api.serializers import (BlogModelSerializer, CommentModelSerializer, SeriesModelSerializer, CategoryModelSerializer)
from rest_framework.permissions import AllowAny, IsAuthenticated



class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    permission_classes = [AllowAny, ]


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny, ]



class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny, ]



class SeriesModelViewSet(ModelViewSet):
    serializer_class = SeriesModelSerializer
    queryset = Series.objects.all()
    permission_classes = [AllowAny, ]
