from django.shortcuts import render, get_object_or_404
from .models import Genre, Product

# Create your views here.
def index(request, category_slug=None):
    genre = None
    genres = Genre.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        products = Product.objects.filter(genre=genre)
    context = {
        'genre':genre,
        'genres':genres,
        'products':products
    }
    return render(request,'store/product/index.html', context)
