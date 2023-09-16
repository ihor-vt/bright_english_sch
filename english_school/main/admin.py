from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.crypto import get_random_string

from parler.admin import TranslatableAdmin

from .models import Category, Course, Service, Comment, MainPage, Contact


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "token", "created_by", "updated_by"]
    readonly_fields = ["token", "created_by", "updated_by"]
    actions = ["generate_new_token"]

    def save_model(self, request, obj, form, change):
        if not obj.token:
            token = get_random_string(length=32)
            obj.token = token

        if not obj.id:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)

    def generate_new_token(self, request, queryset):
        for service in queryset:
            token = get_random_string(length=32)
            service.token = token
            service.save()

    generate_new_token.short_description = "Генерація нового токену"


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name", "created_by", "updated_by"]
    readonly_fields = ["created_by", "updated_by"]
    search_fields = ["name"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(Course)
class CourseAdmin(TranslatableAdmin):
    list_display = [
        "name",
        "display_image",
        "category",
        "time",
        "model",
        "group",
        "format",
        "price_total",
        "price_mounth",
        "message",
        "available",
        "created",
        "updated",
        ]

    readonly_fields = [
        "created_by",
        "updated_by"
        ]

    list_display_links = [
        "name",
        "display_image",
        "category",
        "time",
        "model",
        "group",
        ]

    def display_image(self, obj):
        image = obj.image.url
        if image:
            return mark_safe(
                f'<img src="{image}" width="80" height="100"\
                    style="margin-right: 10px;" />'
            )
        return "-"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}

    list_filter = [
        "category", "available", "price_total", "message"
        ]

    search_fields = [
        "name",
        "category__name",
        "time",
        "price_total",
        "message"
        ]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "created_by", "updated_by"]
    readonly_fields = ["created_by", "updated_by"]
    list_filter = ["author"]
    search_fields = ["content", "author"]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = [
        "media_thumbnail",
        "available",
        "created_by",
        "updated_by",
        "created",
        "updated"
        ]

    readonly_fields = [
        "created_by",
        "updated_by"
        ]

    list_display_links = [
        "media_thumbnail",
        "available",
        "created",
        "updated",
        ]

    def media_thumbnail(self, obj):
        if obj.video:
            if obj.video.resource_type == 'video':
                return mark_safe(f'<video width="200" height="200" controls>\
                                <source src="{obj.video.url}" \
                                type="video/mp4"></video>')
        elif obj.image:
            return mark_safe(f'<img src="{obj.image.url}"\
                            width="200" height="200"\
                style="margin-right: 10px;" />')
        return "-"

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)

    media_thumbnail.allow_tags = True
    media_thumbnail.short_description = "Медіа"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "mobile_phone",
        "description",
        "comment",
        "done",
        "created",
        "updated",
        "updated_by"
        ]

    list_filter = [
        "done",
        "created",
        "updated",
        "updated_by"
        ]

    search_fields = [
        "name",
        "mobile_phone",
        "comment",
        "description"
        ]

    readonly_fields = [
        "created",
        "updated",
        "updated_by"
        ]

    list_display_links = [
        "name",
        "email",
        "mobile_phone",
        "updated_by",
        ]

    actions = ["mark_as_processed"]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def mark_as_processed(self, request, queryset):
        for contact in queryset:
            contact.done = True
            contact.save()

    mark_as_processed.short_description = "Позначити, як оброблені"
