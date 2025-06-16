from django.shortcuts import render

def home(requests):
    if requests.method == 'GET':
        return render(requests, 'home.html')


def contacts(requests):
    if requests.method == 'GET':
        return render(requests, 'contacts.html')