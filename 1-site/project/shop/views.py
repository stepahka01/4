from django.shortcuts import render

products = [
    {'id': 1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
    {'id': 2, 'title': 'Shorts', 'size': 'XL', 'price': 2400},
    {'id': 3, 'title': 'T-shirt', 'size': 'XXL', 'price': 4200},
    {'id': 4, 'title': 'Dress', 'size': 'S', 'price': 6200},
    {'id': 5, 'title': 'Cap', 'size': 'M', 'price': 5000},
]

def productsView(request):
    return render(request, 'shop/products.html', context={'products': products})

def product(request, id):
    product = products[id-1]
    return render(request, 'shop/product.html', context={'product': product})

def index(request):
    header = 'Данные пользователя'
    langs = ['C', 'C++', 'Python', 'java', 'JavaScript', 'Pascal']
    user = {'name': 'Vasilii', 'surname': 'Pupkin'}
    address = ('Mira', 12, 147)
    text = '<h4>My text</h4>'

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'shop/index.html', context=data)


def about(request):
    data = {'name': 'Ann', 'interests': 'programming'}
    return render(request, 'shop/about.html', context=data)


def contacts(request):
    return render(request, 'shop/contacts.html')