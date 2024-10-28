from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', second_page, name='second_page'),
    path('product/<int:pk>', third_page, name='third_page'),
    path('about/', fourth_page, name='fourth_page'),
    path('search/', search_collections, name='search_collections'),
    path('api/search_collections/', api_search_collections, name='api_search_collections'),

    

    # en
    path('index_en', index_en, name='index_en'),
    path('catalog_en/', second_page_en, name='second_page_en'),
    path('product_en/<int:pk>', third_page_en, name='third_page_en'),
    path('about_en/', fourth_page_en, name='fourth_page_en'),
    path('search_en/', search_collections_en, name='search_collections_en'),
    path('api/search_collections_en/', api_search_collections_en, name='api_search_collections_en'),

    # uz
    path('index_uz', index_uz, name='index_uz'),
    path('catalog_uz/', second_page_uz, name='second_page_uz'),
    path('product_uz/<int:pk>', third_page_uz, name='third_page_uz'),
    path('about_uz/', fourth_page_uz, name='fourth_page_uz'),
    path('search_uz/', search_collections_uz, name='search_collections_uz'),
    path('api/search_collections_uz/', api_search_collections_uz, name='api_search_collections_uz'),

    # actions with cart
    path('add/<item_id>\)', cart_add, name='cart_add'),
    path('remove/<item_id>', cart_remove, name='cart_remove'),
    path('save_cart/', save_cart, name='save_cart'),

    # actions with cart en
    path('add_en/<item_id>\)', cart_add_en, name='cart_add_en'),
    path('remove_en/<item_id>', cart_remove_en, name='cart_remove_en'),
    path('save_cart_en/', save_cart_en, name='save_cart_en'),

    # actions with cart uz
    path('add_uz/<item_id>\)', cart_add_uz, name='cart_add_uz'),
    path('remove_uz/<item_id>', cart_remove_uz, name='cart_remove_uz'),
    path('save_cart_uz/', save_cart_uz, name='save_cart_uz')

]
