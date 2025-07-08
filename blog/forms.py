from django import forms
from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('heading', 'content', 'image', 'is_published')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['heading'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название блога'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control'})

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'})

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })
