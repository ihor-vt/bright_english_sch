from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import TextEditor


class textEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
                'widget': TinyMCE()
            }
    }


admin.site.register(TextEditor, textEditorAdmin)
