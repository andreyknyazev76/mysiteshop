
from django.db import models
from users.models import User


STATUS = ((0, "Draft"),(1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True,verbose_name = 'Заголовок')
    slug = models.SlugField(max_length=200, unique=True,verbose_name = 'Короткая ссылка')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name = 'Автор'
    )
    updated_on = models.DateTimeField(auto_now=True,verbose_name = 'Обновлен')
    content = models.TextField(verbose_name = 'Содержимое поста')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name = 'Создан')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name = 'Статус')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Пост'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField( max_length=80,verbose_name = 'Имя' )
    email = models.EmailField(verbose_name = 'Адрес электронной почты')
    body = models.TextField(verbose_name = 'Сообщение')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name = 'Создан')
    active = models.BooleanField(default=False, verbose_name = 'Опубликован')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии' 

    
