from django.shortcuts import render, get_object_or_404
from store.models import Product
# Create your views here.
def track(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'track/track.html', context)
