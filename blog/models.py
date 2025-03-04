from django.db.models.signals import post_delete
import os
from django.dispatch import receiver
from django.db import models
from account.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Приоритет задачи "
    )

    class Meta:
        verbose_name = "Приоритет задачи "
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ManyToManyField(
        to=Category,
        related_name="posts",
        verbose_name="Приоритет задачи",
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    description = models.TextField(
        blank=True, null=True,
        max_length=255,
        verbose_name="Описание"
    )
    content = models.TextField(
        verbose_name="Содержание"
    )
    art_image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name="Изображение статьи"
    )
    bookmarks = models.ManyToManyField(
        to=User,
        related_name="bookmarks",
        blank=True,
        verbose_name="Закладки"
    )
    likes = models.ManyToManyField(
        to=User,
        related_name="like",
        blank=True,
        verbose_name="Нравится"
    )
    dislikes = models.ManyToManyField(
        to=User,
        related_name="dislikes",
        blank=True,
        verbose_name="Не нравится"
    )
    due_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} написал(-а) статью {self.title}'


class Comment(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Статья"
    )
    content = models.TextField(
        max_length=200,
        verbose_name="Текст комментария"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
            verbose_name = "Комментария"
            verbose_name_plural = "Комментарии"
            ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} написал(-а) комментарий {self.created_at}'


@receiver
def post_delete_receiver(sender, instance, **kwargs):
    if instance.art_image and os.path.isfile(instance.art_image.path):
        os.remove(instance.art_image.path)

