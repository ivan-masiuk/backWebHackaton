import json

from django.http import HttpResponse
from django.shortcuts import render
from finditems.models import Item
from finditems.forms import CreateItem
from account.models import Profile


def search_page(request):
    items = Item.objects.all()
    context = {'items': items}
    if request.POST:
        query = request.POST.get('q')
        items = Item.objects.filter(title__icontains=query)
        context.update({'items': items})
    return render(request, 'search-page.html', context)


def create_page(request):
    if request.POST:
        form = CreateItem(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            new_item.user = Profile.objects.get(user=request.user)
            new_item.save()
    return render(request, 'create-item.html')


def item_page(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item}
    return render(request, 'item-page.html', context)


def my_items(request):
    profile = Profile.objects.get(user=request.user)
    items = Item.objects.filter(user=profile)
    context = {'items': items}

    return render(request, 'my-items.html', context)


def del_item(request):
    if request.POST:
        item = Item.objects.get(id=request.POST.get('item'))
        print(request.POST.get('item'))
        item.delete()
        data_response = {'success': True}
        return HttpResponse(json.dumps(data_response), content_type='application/json')
