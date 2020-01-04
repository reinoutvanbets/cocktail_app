from django.shortcuts import render, redirect
from .models import Cocktail
from .forms import CocktailCreate
from django.http import HttpResponse


def index(request):
    return render(request, 'recipes/overview.html')


def cocktails(request):
    cocktail_list = Cocktail.objects.all()
    return render(request, 'recipes/cocktails.html', {'cocktail_list': cocktail_list})


def cocktail_detail(request, cocktail_id):
    cocktail_id = int(cocktail_id)
    try:
        cocktail = Cocktail.objects.get(id=cocktail_id)
    except Cocktail.DoesNotExist:
        return redirect('cocktails')
    return render(request, 'recipes/cocktail_detail.html', {'cocktail': cocktail})


def upload(request):
    upload = CocktailCreate()
    if request.method == 'POST':
        upload = CocktailCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('cocktails')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:
        return render(request, 'recipes/upload_form.html', {'upload_form': upload})


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
    return render(request, 'recipes/upload_form.html', {'upload_form': recipe_form})


def delete_cocktail(request, cocktail_id):
    cocktail_id = int(cocktail_id)
    try:
        cocktail_sel = Cocktail.objects.get(id=cocktail_id)
    except Cocktail.DoesNotExist:
        return redirect('cocktails')
    cocktail_sel.delete()
    return redirect('cocktails')
