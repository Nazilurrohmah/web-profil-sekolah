from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('ppdb/', views.ppdb, name='ppdb'),
    path('berita/', views.berita_list, name='berita_list'),
    path('berita/<int:pk>/', views.berita_detail, name='berita_detail'),
]
