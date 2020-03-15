from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blog', views.BlogModelViewSet)
router.register('comment', views.CommentModelViewSet)
router.register('category', views.CategoryModelViewSet)
router.register('series', views.SeriesModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls
