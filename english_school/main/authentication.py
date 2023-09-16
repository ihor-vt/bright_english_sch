import logging

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from .models import Service
from english_school.settings import env


logger = logging.getLogger(__name__)


class ServiceOnlyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                token = token.split(" ")[1]
                service = Service.objects.get(token=token)
                if token == service.token:
                    return (service, None)
            except Service.DoesNotExist:
                logger.info(f"Service with token '{token}' does not exist.")
                pass
        raise AuthenticationFailed("Invalid service token.")

    def authenticate_header(self, request):
        return "Bearer"


class ServiceOnlyAuthorizationSite(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, Service):
            service_name = request.user.name
            if service_name == env("SERVICE_SITE_NAME"):
                return True
        return False
