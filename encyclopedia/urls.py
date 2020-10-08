from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.get_page, name="get_page"),
    path("<str:sub>_search_result", views.search_result, name="search_result"),
    path("create_new_page", views.create_new_page, name="create_new_page"),
    path("<str:entry>_edit", views.edit_page, name="edit_page"),
    path("wiki", views.random_page, name="random_page")
]
