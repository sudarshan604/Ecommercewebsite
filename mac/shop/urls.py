
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='shopHome'),
    path("about/", views.about, name='AboutUs'),
    path('content/', views.content, name='contactUS'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('productview/', views.productView, name='productView'),
    path('checkout/', views.checkout, name='Checkout'),
]
