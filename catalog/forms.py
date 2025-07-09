from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError


FORBIDDEN_WORDS = {
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'image', 'category_product', 'price_to_buy']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control'})

        self.fields['category_product'].widget.attrs.update({
            'class': 'form-control'})

        self.fields['price_to_buy'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Стоимость продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and any(word.lower() in name.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Название содержит запрещённые слова.")

        if description and any(word.lower() in description.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание содержит запрещённые слова.")

    def clean_price_to_buy(self):
        price = self.cleaned_data.get('price_to_buy')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        mime = image.content_type
        if mime not in ['image/jpeg', 'image/png']:
            raise ValidationError('Формат файла должен быть JPEG или PNG.')
        max_size = 5 * 1024 * 1024
        if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')
        return image
