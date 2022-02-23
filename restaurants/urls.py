from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('restaurants/', views.restaurants, name="restaurants"),
    path('restaurant/<str:pk>/', views.restaurant, name="restaurant"),
    path('restaurants/create-ticket/', views.createTicket, name="create-ticket"),
    path('restaurants/update-ticket/<str:pk>/', views.updateTicket, name="update-ticket"),
    path('restaurants/delete-ticket/<str:pk>/', views.deleteTicket, name="delete-ticket"),
    path('restaurants/purchase/<str:pk>/', views.purchaseTicket, name="purchase-ticket"),
]