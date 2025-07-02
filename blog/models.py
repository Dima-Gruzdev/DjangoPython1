from django.db import models


class Blog(models.Model):
    heading = models.CharField(
        max_length=50,
        verbose_name='Название заголовка',
        help_text='Введите название заголовка',
    )
    content = models.TextField(
        verbose_name='Описание содержимого контента', blank=True, null=True
    )
    image = models.ImageField(
        upload_to="blogs_image/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(verbose_name='Опубликовано',
        default=False
    )

    number_of_views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    class Meta:
        verbose_name = "<Блог>"
        verbose_name_plural = "Блоги"
        ordering = ["heading", "content"]

    def __str__(self):
        return f"{self.heading} {self.content}"
