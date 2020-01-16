import django_tables2 as tables
from .models import Ingredient


class IngredientTable(tables.Table):
    class Meta:
        model = Ingredient
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("name", 'creator')
