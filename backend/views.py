from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from .cart import Cart
from .models import *
from django.urls import reverse
from .forms import CartForm, CartFormEn, CartFormUz
from rest_framework import generics
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse

import requests

TOKEN = "6976030713:AAFQOJeZUDfooAz1OCDjATZoqlfNNjlZpU8"

chat_id = "-1002183304076"

from django.contrib.sessions.models import Session
from django.utils import timezone


def cart_form_processor(request):
    return {
        'cart_form': CartForm(),
        'cart_form_en': CartFormEn(),
        'cart_form_uz': CartFormUz()
    }


# Create your views here.
def index(request):
    items = Item.objects.all()
    collections = Collection.objects.all()

    context = {
        'items': items,
        'collections': collections
    }

    return render(request, 'index.html', context)


def second_page(request):
    collections = Collection.objects.all()

    context = {
        'collections': collections
    }

    return render(request, 'second_page.html', context)


def third_page(request, pk):
    item = Item.objects.get(pk=pk)

    collection = Collection.objects.get(pk=item.collection.pk)

    items = Item.objects.filter(collection=collection)

    context = {
        'item': item,
        'items': items
    }

    return render(request, 'third_page.html', context)


def fourth_page(request):
    count_about = CountBlogAbout.objects.all()

    index_len = len(count_about) * 3

    index_list = [ind for ind in range(1, index_len + 1)]

    context = {
        'count_about': count_about,
        'index_len': index_len,
        'index_list': index_list
    }

    return render(request, 'fourth_page.html', context)


def search_collections(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name__icontains=query) if query else Collection.objects.all()
    return render(request, 'search_page.html', {'collections': collections})


def api_search_collections(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name__icontains=query) if query else Collection.objects.all()
    results = [{'id': collection.id, 'name': collection.name} for collection in collections]
    return JsonResponse(results, safe=False)


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(product=item)

    print('Корзина')

    return redirect(reverse('third_page', args=(item_id,)))


def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)

    return redirect('index')


@csrf_protect
def save_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():

            try:
                send_mail('Пробник', 'Тест',
                          'timurabdulvohidov@gmail.com',
                          ['timurabdulvohidov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')

            cd = form.cleaned_data

            cart = Cart(request)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            contact = form.cleaned_data['contact']

            print(country)

            message = f'''Запрос
            
Имя:  {first_name}
Фамилия:  {last_name}
Страна:  {country}
Контакты:  {contact}

Корзина:

'''

            print(cart)
            for cart_item in cart:
                print(cart_item)
                print(cart.get_total_price())
                message += f'Товар: {cart_item["product"]}, цена: {cart_item["price"]:.0f}, количество: {cart_item["quantity"]}\n'

            message += f'\nОбщая цена: {cart.get_total_price()}'

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

            cart.clear()

            print(cart)
            messages.success(request, 'Ваш заказ отправлен успешно, мы свяжемся с вами в ближайшее время!')
        else:
            messages.error(request, 'Ошибка в данных формы. Пожалуйста, проверьте и попробуйте снова.')
    else:

        form = CartForm()
    return redirect('index')


# en


def index_en(request):
    items = Item.objects.all()
    collections = Collection.objects.all()

    context = {
        'items': items,
        'collections': collections
    }

    return render(request, 'index_en.html', context)


def second_page_en(request):
    collections = Collection.objects.all()

    context = {
        'collections': collections
    }

    return render(request, 'second_page_en.html', context)


def third_page_en(request, pk):
    item = Item.objects.get(pk=pk)

    collection = Collection.objects.get(pk=item.collection.pk)

    items = Item.objects.filter(collection=collection)

    context = {
        'item': item,
        'items': items
    }

    return render(request, 'third_page_en.html', context)


def fourth_page_en(request):
    count_about = CountBlogAbout.objects.all()

    index_len = len(count_about) * 3

    index_list = [ind for ind in range(1, index_len + 1)]

    context = {
        'count_about': count_about,
        'index_len': index_len,
        'index_list': index_list
    }

    return render(request, 'fourth_page_en.html', context)


def search_collections_en(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name_en__icontains=query) if query else Collection.objects.all()
    return render(request, 'search_page_en.html', {'collections': collections})


def api_search_collections_en(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name_en__icontains=query) if query else Collection.objects.all()
    results = [{'id': collection.id, 'name': collection.name_en} for collection in collections]
    return JsonResponse(results, safe=False)


@require_POST
def cart_add_en(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(product=item)

    print('Корзина')

    return redirect(reverse('third_page_en', args=(item_id,)))


def cart_remove_en(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)

    return redirect('index_en')


@csrf_protect
def save_cart_en(request):
    if request.method == 'POST':
        form = CartFormEn(request.POST)
        if form.is_valid():

            try:
                send_mail('Пробник', 'Тест',
                          'timurabdulvohidov@gmail.com',
                          ['timurabdulvohidov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')

            cd = form.cleaned_data

            cart = Cart(request)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            contact = form.cleaned_data['contact']

            print(country)

            message = f'''Запрос

Имя:  {first_name}
Фамилия:  {last_name}
Страна:  {country}
Контакты:  {contact}

Корзина:

'''

            print(cart)
            for cart_item in cart:
                print(cart_item)
                print(cart.get_total_price())
                message += f'Товар: {cart_item["product"]}, цена: {cart_item["price"]:.0f}, количество: {cart_item["quantity"]}\n'

            message += f'\nОбщая цена: {cart.get_total_price()}'

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

            cart.clear()

            print(cart)
            messages.success(request, 'Your order has been sent successfully, we will contact you shortly!')
        else:
            messages.error(request, 'There is an error in the form data. Please check and try again.')
    else:
        form = CartFormEn()
    return redirect('index_en')


# uz

def index_uz(request):
    items = Item.objects.all()
    collections = Collection.objects.all()

    context = {
        'items': items,
        'collections': collections
    }

    return render(request, 'index_uz.html', context)


def second_page_uz(request):
    collections = Collection.objects.all()

    context = {
        'collections': collections
    }

    return render(request, 'second_page_uz.html', context)


def third_page_uz(request, pk):
    item = Item.objects.get(pk=pk)

    collection = Collection.objects.get(pk=item.collection.pk)

    items = Item.objects.filter(collection=collection)

    context = {
        'item': item,
        'items': items
    }

    return render(request, 'third_page_uz.html', context)


def fourth_page_uz(request):
    count_about = CountBlogAbout.objects.all()

    index_len = len(count_about) * 3

    index_list = [ind for ind in range(1, index_len + 1)]

    context = {
        'count_about': count_about,
        'index_len': index_len,
        'index_list': index_list
    }

    return render(request, 'fourth_page_uz.html', context)


def search_collections_uz(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name_uz__icontains=query) if query else Collection.objects.all()
    return render(request, 'search_page_uz.html', {'collections': collections})


def api_search_collections_uz(request):
    query = request.GET.get('search')
    collections = Collection.objects.filter(name_uz__icontains=query) if query else Collection.objects.all()
    results = [{'id': collection.id, 'name': collection.name_uz} for collection in collections]
    return JsonResponse(results, safe=False)


@require_POST
def cart_add_uz(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(product=item)

    print('Корзина')

    return redirect(reverse('third_page_uz', args=(item_id,)))


def cart_remove_uz(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=item_id)
    cart.remove(product)

    return redirect('index_uz')


@csrf_protect
def save_cart_uz(request):
    if request.method == 'POST':
        form = CartFormUz(request.POST)
        if form.is_valid():

            try:
                send_mail('Пробник', 'Тест',
                          'timurabdulvohidov@gmail.com',
                          ['timurabdulvohidov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')

            cd = form.cleaned_data

            cart = Cart(request)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            contact = form.cleaned_data['contact']

            print(country)

            message = f'''Запрос

Имя:  {first_name}
Фамилия:  {last_name}
Страна:  {country}
Контакты:  {contact}

Корзина:

'''

            print(cart)
            for cart_item in cart:
                print(cart_item)
                print(cart.get_total_price())
                message += f'Товар: {cart_item["product"]}, цена: {cart_item["price"]:.0f}, количество: {cart_item["quantity"]}\n'

            message += f'\nОбщая цена: {cart.get_total_price()}'

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

            cart.clear()

            print(cart)
    else:
        form = CartFormUz()
    return redirect('index_uz')
