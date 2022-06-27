from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('about/', views.about, name='home_about'),
    path('contact/', views.contact, name='home_contact'),
]