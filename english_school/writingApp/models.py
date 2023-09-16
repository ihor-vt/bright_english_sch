from django.db import models
from django.utils.translation import gettext_lazy as _


class TextEditor(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Заголовок')
    )
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("Редактор тексту")
        verbose_name_plural = _("Редактор текстів")
