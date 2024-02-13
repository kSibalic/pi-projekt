from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Item, Category, Like
from .forms import NewItemForm, EditItemForm

# Create your views here.

def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(dostupno=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    }

    return render(request, 'item/items.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(kategorija=item.kategorija, dostupno=False).exclude(pk=pk)[0:3]
    liked = item.liked_by(request.user)

    context = {
        'item': item,
        'related_items': related_items,
        'liked': liked,
    }
    return render(request, 'item/detail.html', context)

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

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    context={
        'form': form,
        'title': 'Edit item',
    }
    return render(request, 'item/form.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()

    return redirect('dashboard:index')

@login_required
def toggle_like(request, pk):
    item=get_object_or_404(Item, pk=pk)
    if request.method=='POST' and request.user.is_authenticated:
        like=request.user.like_set.filter(item=item).first()
        if like:
            like.delete()
        else:
            like=Like(user=request.user, item=item)
            like.save()

    return HttpResponseRedirect(
        reverse('item:detail', args=(pk,))
    )