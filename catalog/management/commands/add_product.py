from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test product to the Database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Все существующие продукты удалены'))
        category, _ = Category.objects.get_or_create(name_cat='Орехи')


        products = [
            {"name": 'Фисташки', "description": "Полезен жирами и углеводами", "category_product": category, "price_to_buy": 300},
            {"name": 'Пекан', "description": "Полезен витамином Е", "category_product": category, "price_to_buy": 200},
            {"name": 'Кешью', "description": "Богат минералами", "category_product": category, "price_to_buy": 150},
        ]


        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully add product: {product.name}'))
            else:
                self.stdout.write(self.style.WARRNING(f'product already exist: {product.name}'))
