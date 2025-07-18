from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название почты'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Придумайте пароль'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите повторно пароль'
        })

        self.fields['area'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите номер телефона (необязательно)'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'image', 'area', 'phone_number')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр.')
        return phone_number
