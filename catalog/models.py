from django.conf import settings
from django.db import models


class Category(models.Model):
    name_cat = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description_cat = models.TextField(
        verbose_name="Описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name_cat


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="product_image/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    category_product = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    price_to_buy = models.IntegerField(verbose_name="Сумма")
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(verbose_name='Опубликовано',default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category_product"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукцию"),
        ]

    def __str__(self):
        return f"{self.name} {self.category_product}"
