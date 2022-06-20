from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_page, name="search_page"),
    path("new", views.new_page, name="new_page"),
    path("new/<str:operation>", views.create_page, name="create_page"),
    path("random", views.random_page, name="random_page"),
    path("wiki/<str:title>", views.get_page, name="get_page"),
    path("wiki/<str:title>/edit", views.edit_page, name="edit_page"),
    path("wiki/<str:title>/edit/<str:operation>", views.update_page, name="update_page")
]
