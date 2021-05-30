from django.urls import path
from finditems.views import (search_page,
                             create_page,
                             item_page,
                             del_item,
                             my_items)

urlpatterns = [
    path('', search_page, name='search_page'),
    path('create/', create_page, name='create_page'),
    path('item-page/<int:item_id>/', item_page, name='item_page'),
    path('my-items/', my_items, name='my_items'),
    path('del_item/', del_item, name='del_item')
]
