from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продукта"""

    product_name = models.CharField(max_length=50, verbose_name='Название продукта')
    product_description = models.TextField(verbose_name='Описание продукта', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}, {self.product_description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Network(models.Model):
    """Модель сети"""
    link_types = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    apartment = models.CharField(max_length=30, verbose_name='Номер дома')
    products = models.ManyToManyField(Product, related_name='networks')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность перед поставщиком р., кк.',
                               default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    link_type = models.IntegerField(choices=link_types, verbose_name='Уровень в иерархии')

    def __str__(self):
        return f'{self.name}: {self.email}, {self.country}, {self.city}, {self.supplier}, {self.debt}, {self.link_type}'

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'

