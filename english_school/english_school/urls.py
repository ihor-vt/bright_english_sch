"""
URL configuration for english_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from jet.dashboard.dashboard_modules import google_analytics_views

urlpatterns = i18n_patterns(
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("set-language/", set_language, name="set_language"),
    path('tinymce/', include('tinymce.urls')),
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _("Адмін-панель")
admin.site.site_title = _("Адмін-панель")
admin.site.index_title = _("Ласкаво просимо до адмін-панелі сайту")
