from django.contrib import admin
from django.urls import path
from appUpload import views

urlpatterns = [
    path('list', views.index, name="/"),
    path('', views.home, name="home"),
    path('add-product', views.addProduct, name="add-prod"),
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
    path('delete-product/<str:pk>', views.deleteProduct, name="delete-prod"),
    path('contact', views.Contact),

]
