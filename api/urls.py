from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', views.registerUser),
    
    path('restaurants/', views.getRestaurants),
    path('restaurants/<str:pk>/', views.getRestaurant),
    path('tickets/', views.createTicket),
    path('ticket/<str:pk>/', views.manageTicket),
    path('purchase/<str:pk>/', views.purchaseTicket),
]