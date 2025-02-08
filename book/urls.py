from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("book-list/", views.book_list , name = "book_list" ),
    path("create/", views.book_create, name = "book_create"),
    path("<int:book_id>/edit/", views.book_edit, name = "book_edit"),
    path("<int:book_id>/book-details/", views.post, name= 'book_details'),
    path("<int:book_id>/delete/", views.book_delete, name = "book_delete"),
    path("register/", views.register, name = "register"),
    path ("@<str:username>/", views.userProfile, name="user_profile"),

]
