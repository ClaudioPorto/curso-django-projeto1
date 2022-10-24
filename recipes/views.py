from django.shortcuts import render

from utils.recipes.factory import make_recipe

# Create your views here.


def home(request):
    return render(request, 'pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'pages/recipe_detail.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
