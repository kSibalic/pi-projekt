from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter()
    context = {
        'items': items
    }

    return render(request, 'wishlist/index.html', context)

@login_required
def toggle_wishlist(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    if request.method=='POST' and request.user.is_authenticated:
        like=request.user.like_set.filter(item=item).first()
        if like:
            like.delete()
        else:
            like=Item(user=request.user, image=image)
            like.save()

    return render(request, 'wishlist/index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    context={
        'form': form,
        'title': 'New item',
    }
    return render(request, 'item/form.html', context)