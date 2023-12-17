from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    contact = {'list': ['My phone number: 89083041524', 'My Telegram: @Nastttat']}
    return render(request, "contacts.html", contact)
