from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Создание модели пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')
    name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    phone_number = models.CharField(max_length=20, **NULLABLE, verbose_name='Телефон')
    is_verified = models.BooleanField(default=False, verbose_name='Подтверждение')
    token = models.CharField(max_length=10, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
