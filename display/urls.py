from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.index),
    path('', views.fight_club, name='Photography-Fight-Club-Display'),
    path('fight-club', views.fight_club, name='Photography-Fight-Club-Display'),
    ]
