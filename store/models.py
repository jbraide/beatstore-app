from django.db import models
from django.urls import reverse




# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    genre = models.ForeignKey(Genre, related_name='products', on_delete  = models.CASCADE)
    available= models.BooleanField(default=True)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length = 100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.CharField(max_length=30)
    bpm = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image/',blank=True)
    beat_file = models.FileField(upload_to='audio/', blank=True)



    class Meta:
        ordering = ('title',)
        index_together = (('id','slug'))

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse("track:track", args=[self.slug])
