import os
import logging
import subprocess

from datetime import datetime

from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail, BadHeaderError
from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import (
    Category,
    Course,
    Comment,
    MainPage,
    Contact,
    SubscriptionEmail,
    Teacher
)
from .serializers import (
    CategorySerializer,
    CourseSerializer,
    CommentSerializer,
    MainPageSerializer,
    ContactSerializer,
    SubscriptionEmailSerializer,
    TeacherSerializer
)
from .authentication import (
    ServiceOnlyAuthentication,
    ServiceOnlyAuthorizationSite
)
from .mail_messsage_generator import (
    contact_form_message,
    sumscribe_welcome_message
)


logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 30))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class MainPageCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(
        available=True,
        main_page=True,
        )
    serializer_class = CourseSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data

        for item in data:
            course_id = item["id"]
            course = Course.objects.get(pk=course_id)
            category = course.category
            category_serializer = CategorySerializer(
                category, context={"request": request}
            )
            item["category"] = category_serializer.data

        return Response(data)

    @method_decorator(cache_page(60 * 30))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            context={"request": request})
        data = serializer.data

        category = instance.category
        category_serializer = CategorySerializer(
            category, context={"request": request}
        )
        data["category"] = category_serializer.data

        return Response(data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(
        available=True
        )
    serializer_class = CourseSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data

        for item in data:
            course_id = item["id"]
            course = Course.objects.get(pk=course_id)
            category = course.category
            category_serializer = CategorySerializer(
                category, context={"request": request}
            )
            item["category"] = category_serializer.data

        return Response(data)

    @method_decorator(cache_page(60 * 30))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            context={"request": request})
        data = serializer.data

        category = instance.category
        category_serializer = CategorySerializer(
            category, context={"request": request}
        )
        data["category"] = category_serializer.data

        return Response(data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.filter(available=True)
    serializer_class = MainPageSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 30))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            context={"request": request})
        data = serializer.data

        return Response(data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.none()
    serializer_class = ContactSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send email
        time_now = datetime.now()
        formatted_datetime = time_now.strftime("%d.%m.%Y - %H:%M")
        subject = _("Форму з сайту заповнив клієнт")
        name = serializer.data.get('name', "-")
        email = serializer.data.get('email', "-")
        mobile_phone = serializer.data.get('mobile_phone', "-")
        description = serializer.data.get('description', "-")
        message = contact_form_message(
            formatted_datetime, name, email, mobile_phone, description
            )

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError as e:
            logger.error(f"Invalid header found: {e}")
        except Exception as e:
            logger.error(f">>> Failed to send email: {e}")

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)


class SubscriptionEmailViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionEmail.objects.none()
    serializer_class = SubscriptionEmailSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['post']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            if SubscriptionEmail.objects.filter(email=email).exists():
                return Response(
                    {'detail': _('Ця електронна адреса вже підписана.')},
                    status=status.HTTP_400_BAD_REQUEST)

            SubscriptionEmail.objects.create(email=email)

            # Send email
            subject = _(
                "Ласкаво просимо до Bright Language School інформаційну підписку!"
                )
            message = sumscribe_welcome_message(
                email,
                )

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
            except BadHeaderError as e:
                logger.error(f"Invalid header found: {e}")
            except Exception as e:
                logger.error(f">>> Failed to send email: {e}")

            return Response(
                {'detail': 'You successfully subscribe for newsletters.'},
                status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [ServiceOnlyAuthentication]
    permission_classes = [ServiceOnlyAuthorizationSite]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


def index(request):
    api_url = reverse("api-root")
    admin_url = reverse("admin:index")

    context = {
        "api_url": api_url,
        "admin_url": admin_url,
    }

    return render(request, "main/index.html", context)


def create_backup(request):
    db_path = settings.DATABASES.get("default").get("NAME")

    time_now = datetime.now()
    time_now_str = time_now.strftime("%Y-%m-%d-%H-%M")
    backup_filename = f"{time_now_str}_backup.sql"

    sqlite3_path = "/usr/bin/sqlite3"

    try:
        try:
            subprocess.run(
                f"{sqlite3_path} {db_path} .dump > {backup_filename}",
                shell=True, check=True)
        except subprocess.CalledProcessError as e:
            return HttpResponse(
                f"Error create buackup: {e}", status=500)
        else:
            with open(backup_filename, "rb") as backup_file:
                response = HttpResponse(
                    backup_file.read(), content_type="application/sql")
                response["Content-Disposition"] = f'attachment; filename="{backup_filename}"'
    except Exception as e:
        response = HttpResponse(str(e), content_type="text/plain")

    try:
        if os.path.exists(backup_filename):
            os.remove(backup_filename)
    except Exception:
        ...

    return response
