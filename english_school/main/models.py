import cloudinary

from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Назва"
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
        verbose_name="Створив(ла)",
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='categories_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="course",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категорія",
    )
    name = models.CharField(max_length=200, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    image = models.ImageField(
        upload_to="images/",
        null=True,
        verbose_name="Зображення")
    time = models.CharField(max_length=200, verbose_name="Період")
    model = models.CharField(
        max_length=200, verbose_name="Період")
    group = models.CharField(
        max_length=200, verbose_name="Група")
    format = models.CharField(
        max_length=200, verbose_name="Формат")
    price_total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ціна загальна"
    )
    price_mounth = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ціна за місяць"
    )
    message = models.CharField(
        max_length=200, verbose_name="Заклик")
    available = models.BooleanField(
        default=True,
        verbose_name="Наявність")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='products_created',
        null=True,
        blank=True,
        verbose_name="Створив(ла)",
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='products_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Час створення")
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Час обновлення")

    def delete(self, *args, **kwargs):
        if self.image:
            # Get the public_id of the image from the Cloudinary URL
            public_id = self.image.name.split('/')[-1].split('.')[0]
            cloudinary.uploader.destroy(public_id)

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        indexes = [
            models.Index(fields=["id", "name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    content = models.TextField(max_length=600, verbose_name="Відгук")
    author = models.CharField(max_length=100, verbose_name="Автор")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='comments_created',
        null=True,
        blank=True,
        verbose_name="Створив(ла)",
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='comments_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        indexes = [
            models.Index(fields=["author"]),
        ]

    def __str__(self) -> str:
        return f"{self.author} {self.author}"


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    token = models.CharField(max_length=255, unique=True, verbose_name="Токен")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='services_created',
        null=True,
        blank=True,
        verbose_name="Створив(ла)",
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='services_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервіс"
        verbose_name_plural = "Сервіси"


class MainPage(models.Model):
    image = models.ImageField(
        upload_to="images/mainpage",
        null=True,
        blank=True,
        verbose_name="Зображення")
    video = CloudinaryField(
        resource_type="video",
        null=True,
        blank=True,
        verbose_name="Відео"
    )
    available = models.BooleanField(
        default=True,
        verbose_name="Актуальне")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='mainpages_created',
        null=True,
        blank=True,
        verbose_name="Створив(ла)",
        )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='mainpages_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Час створення")
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Час обновлення")

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
        verbose_name = "Головне медіа"
        verbose_name_plural = "Головні медіа"


class Contact(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Ім'я")
    email = models.EmailField(
        verbose_name="Email"
    )
    mobile_phone = models.CharField(
        max_length=15,
        verbose_name="Мобільний телефон")
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Примітка"
        )
    done = models.BooleanField(
        default=False,
        verbose_name="Оброблено"
    )
    comment = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name="Записка"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Час створення")
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Час обновлення")
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='contacts_updated',
        null=True,
        blank=True,
        verbose_name="Обновив(ла)",
        )

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.mobile_phone}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти "


class Subscrabe_email(models.Model):
    email = models.EmailField(verbose_name="email")
