from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"courses/main", views.CourseMainPageViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"medias", views.MainPageViewSet)
router.register(r"contacts", views.ContactViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
]
