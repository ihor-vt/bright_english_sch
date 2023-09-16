from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WritingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'writingApp'
    verbose_name = _("Редактор")
