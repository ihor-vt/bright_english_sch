from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"main-courses", views.MainPageCourseViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"medias", views.MainPageViewSet)
router.register(r"contacts", views.ContactViewSet)
router.register(r"subscriptions", views.SubscriptionEmailViewSet)
router.register(r"teachers", views.TeacherViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.index, name="index"),
    path("create_backup/", views.create_backup, name="create_backup"),
]
