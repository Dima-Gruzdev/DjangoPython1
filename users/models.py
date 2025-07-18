from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True,
                                    help_text='Введите номер телефона')
    image = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите свое фото",
    )
    area = models.CharField(max_length=30, verbose_name='Страна', blank=True, null=True,
                            help_text='Введите страну в которой проживаете')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
