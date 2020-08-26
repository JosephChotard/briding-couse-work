from django.shortcuts import redirect, render
from lists.models import Item


def lists_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists')

    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})
