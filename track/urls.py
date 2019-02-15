from django.urls import path, include
from . import views


app_name = 'track'
urlpatterns = [
    path('<slug>/', views.track, name='track'),
]
