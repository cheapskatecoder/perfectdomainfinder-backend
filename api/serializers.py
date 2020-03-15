from blog.models import Blog, Series, Comment, Category
from rest_framework.serializers import ModelSerializer



class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        depth = 1
        fields = '__all__'


class SeriesModelSerializer(ModelSerializer):
    class Meta:
        model = Series
        depth = 1
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = '__all__'
