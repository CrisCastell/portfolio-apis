from django.urls import path
from . import views

urlpatterns = [
    path("char-list", views.charList, name="char-list"),
    path("house-list", views.houseList, name="house-list"),
    path("characters/<int:pk>", views.characters, name="characters")
]