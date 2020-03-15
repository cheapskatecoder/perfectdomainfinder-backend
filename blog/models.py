from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Series(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = RichTextField()
    blog = models.ForeignKey('blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    meta = RichTextField()
    blog = RichTextField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    series = models.ManyToManyField(Series, related_name='toseries')
    category = models.ManyToManyField(Category, related_name='tocategory')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
