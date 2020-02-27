import django_tables2 as tables
from .models import Ingredient


class IngredientTable(tables.Table):
    detail = tables.TemplateColumn('''<a href="/ingredients/{{ record.id }}">Detail</a>''')

    class Meta:
        model = Ingredient
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("name", 'brand', 'dateCreated')
