# Generated by Django 4.2.7 on 2024-04-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('body', models.TextField(verbose_name='Сообщение')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('active', models.BooleanField(default=False, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Короткая ссылка')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('content', models.TextField(verbose_name='Содержимое поста')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Посты',
                'verbose_name_plural': 'Пост',
            },
        ),
    ]
