# Generated by Django 4.1 on 2023-09-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextEditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField()),
                ('is_selected', models.BooleanField(default=False, verbose_name='Обрано для надсилання')),
            ],
            options={
                'verbose_name': 'Редактор тексту',
                'verbose_name_plural': 'Редактор текстів',
            },
        ),
    ]
