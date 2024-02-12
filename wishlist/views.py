from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item, Like

@login_required
def index(request):
    likes = Like.objects.filter(user=request.user)
    liked_posts = []

    for like in likes:
        liked_posts.append(like.item)
                
    context = {
       'liked_posts': liked_posts
    }

    return render(request, 'wishlist/index.html', context)