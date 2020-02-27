import django_filters
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django_tables2 import LazyPaginator
from django_tables2.views import SingleTableMixin

from .forms import CocktailCreate, IngredientCreate
from .models import Cocktail, Ingredient
from .tables import IngredientTable


class IngredientFilter(django_filters.FilterSet):
    class Meta:
        model = Ingredient
        fields = {
            'name': ['contains']
        }


class FilteredIngredientListView(SingleTableMixin, FilterView):
    model = Ingredient
    table_class = IngredientTable
    template_name = 'recipes/ingredients.html'
    paginator_class = LazyPaginator
    filterset_class = IngredientFilter


def index(request):
    return render(request, 'recipes/overview.html')


def cocktails(request):
    cocktail_list = Cocktail.objects.all()
    return render(request, 'recipes/cocktails.html', {'cocktail_list': cocktail_list})


def ingredients(request):
    ingredient_list = Ingredient.objects.all()
    return render(request, 'recipes/ingredients.html', {'ingredient_list': ingredient_list})


def cocktail_detail(request, cocktail_id):
    cocktail_id = int(cocktail_id)
    try:
        cocktail = Cocktail.objects.get(id=cocktail_id)
    except Cocktail.DoesNotExist:
        return redirect('cocktails')
    return render(request, 'recipes/cocktail_detail.html', {'cocktail': cocktail})


def ingredient_detail(request, ingredient_id):
    ingredient_id = int(ingredient_id)
    try:
        ingredient = Ingredient.objects.get(id=ingredient_id)
    except Ingredient.DoesNotExist:
        return redirect('ingredients')
    return render(request, 'recipes/ingredient_detail.html', {'ingredient': ingredient})


def upload_cocktail(request):
    upload = CocktailCreate()
    if request.method == 'POST':
        upload = CocktailCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('cocktails')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:
        return render(request, 'recipes/upload_cocktail.html', {'upload_form': upload})


def upload_ingredient(request):
    upload = IngredientCreate()
    if request.method == 'POST':
        upload = IngredientCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('ingredients')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:
        return render(request, 'recipes/upload_ingredient.html', {'upload_form': upload})


def update_cocktail(request, cocktail_id):
    cocktail_id = int(cocktail_id)
    try:
        recipe_sel = Cocktail.objects.get(id=cocktail_id)
    except Cocktail.DoesNotExist:
        return redirect('cocktails')
    recipe_form = CocktailCreate(request.POST or None, instance=recipe_sel)
    if recipe_form.is_valid():
        recipe_form.save()
        return redirect('cocktails')
    return render(request, 'recipes/upload_cocktail.html', {'upload_form': recipe_form})


def update_ingredient(request, ingredient_id):
    ingredient_id = int(ingredient_id)
    try:
        ingredient_sel = Ingredient.objects.get(id=ingredient_id)
    except Ingredient.DoesNotExist:
        return redirect('ingredients')
    recipe_form = IngredientCreate(request.POST or None, instance=ingredient_sel)
    if recipe_form.is_valid():
        recipe_form.save()
        return redirect('ingredients')
    return render(request, 'recipes/upload_ingredient.html', {'upload_form': recipe_form})


def delete_cocktail(request, cocktail_id):
    cocktail_id = int(cocktail_id)
    try:
        cocktail_sel = Cocktail.objects.get(id=cocktail_id)
    except Cocktail.DoesNotExist:
        return redirect('cocktails')
    cocktail_sel.delete()
    return redirect('cocktails')


def delete_ingredient(request, ingredient_id):
    ingredient_id = int(ingredient_id)
    try:
        ingredient_sel = Ingredient.objects.get(id=ingredient_id)
    except Ingredient.DoesNotExist:
        return redirect('ingredients')
    ingredient_sel.delete()
    return redirect('ingredients')
