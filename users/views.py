from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать!'
        message = 'Здравствуйте! Спасибо за регистрацию на нашем сайте.'
        from_email = 'nubile4446@mail.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


def home_view(request):
    return render(request, 'home.html')