from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    person = {
        'first_name': 'Pero',
        'last_name': 'PEric',
    }
    return render(request, 'pages/home.html', person)


def about_us(request):
    return render(request, 'pages/about-us.html')


def contact_us(request):
    return render(request, 'pages/contact-us.html')
