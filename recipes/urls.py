from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="recipes-list"),
    path('recipes/<int:id>', views.recipe, name="recipes-detail"),
]
