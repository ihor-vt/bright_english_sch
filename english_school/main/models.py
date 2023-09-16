import cloudinary

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from cloudinary.models import CloudinaryField
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            max_length=200,
            verbose_name=_("Назва")
        ),
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        blank=True
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='categories_created',
        null=True,
        blank=True,
        verbose_name=_("Створив(ла)"),
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='categories_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )

    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    def __str__(self) -> str:
        return self.name


class Course(TranslatableModel):
    category = models.ForeignKey(
        Category,
        related_name="course",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Категорія"),
    )
    translations = TranslatedFields(
        name=models.CharField(
            max_length=200,
            verbose_name=_("Назва")
            ),
        time=models.CharField(
            max_length=200,
            verbose_name=_("Період")
            ),
        model=models.CharField(
            max_length=200,
            verbose_name=_("Модулів")
            ),
        group=models.CharField(
            max_length=200,
            verbose_name=_("Група")
            ),
        format=models.CharField(
            max_length=200,
            verbose_name=_("Формат")
            )
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        blank=True
        )
    image = models.ImageField(
        upload_to="images/",
        null=True,
        verbose_name=_("Зображення"))
    price_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Ціна загальна")
    )
    price_mounth = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Ціна за місяць")
    )
    message = models.CharField(
        max_length=200,
        verbose_name=_("Заклик")
        )
    available = models.BooleanField(
        default=True,
        verbose_name=_("Наявність")
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='products_created',
        null=True,
        blank=True,
        verbose_name=_("Створив(ла)"),
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='products_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Час створення")
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Час обновлення")
        )

    def delete(self, *args, **kwargs):
        if self.image:
            # Get the public_id of the image from the Cloudinary URL
            public_id = self.image.name.split('/')[-1].split('.')[0]
            cloudinary.uploader.destroy(public_id)

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курси")
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    content = models.TextField(
        max_length=600,
        verbose_name=_("Відгук")
        )
    author = models.CharField(
        max_length=100,
        verbose_name=_("Автор")
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='comments_created',
        null=True,
        blank=True,
        verbose_name=_("Створив(ла)"),
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='comments_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )

    class Meta:
        verbose_name = _("Коментар")
        verbose_name_plural = _("Коментарі")
        indexes = [
            models.Index(fields=["author"]),
        ]

    def __str__(self) -> str:
        return f"{self.author} {self.author}"


class Service(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Назва")
        )
    token = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Токен")
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='services_created',
        null=True,
        blank=True,
        verbose_name=_("Створив(ла)"),
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='services_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Сервіс")
        verbose_name_plural = _("Сервіси")


class MainPage(models.Model):
    image = models.ImageField(
        upload_to="images/mainpage",
        null=True,
        blank=True,
        verbose_name=_("Зображення")
        )
    video = CloudinaryField(
        resource_type="video",
        null=True,
        blank=True,
        verbose_name=_("Відео")
    )
    available = models.BooleanField(
        default=True,
        verbose_name=_("Актуальне")
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='mainpages_created',
        null=True,
        blank=True,
        verbose_name=_("Створив(ла)"),
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='mainpages_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Час створення")
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Час обновлення")
        )

    def __str__(self) -> str:
        return f"{self.id}"

    def delete(self, *args, **kwargs):
        if self.image and self.image.url:
            # Get the public_id of the image from the Cloudinary URL
            public_id = self.image.name.split('/')[-1].split('.')[0]
            cloudinary.uploader.destroy(public_id)
        if self.video:
            public_id = self.video.public_id
            cloudinary.uploader.destroy(public_id)

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _("Головне медіа")
        verbose_name_plural = _("Головні медіа")


class Contact(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name=_("Ім'я")
        )
    email = models.EmailField(
        verbose_name=_("Електрона пошта")
    )
    mobile_phone = models.CharField(
        max_length=15,
        verbose_name=_("Мобільний телефон")
        )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name=_("Примітка")
        )
    done = models.BooleanField(
        default=False,
        verbose_name=_("Оброблено")
    )
    comment = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name=_("Записка")
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Час створення")
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Час обновлення")
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='contacts_updated',
        null=True,
        blank=True,
        verbose_name=_("Обновив(ла)"),
        )

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.mobile_phone}"

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакти")


class Subscrabe_email(models.Model):
    email = models.EmailField(
        verbose_name=_("Електрона пошта")
        )

    class Meta:
        verbose_name = _("Підписка на розсилку")
        verbose_name_plural = _("Підписки на розсилку")

    def __str__(self):
        return self.email
