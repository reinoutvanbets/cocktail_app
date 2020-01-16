from django import forms
from .models import Cocktail
from .models import Ingredient


class CocktailCreate(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = '__all__'


class IngredientCreate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
