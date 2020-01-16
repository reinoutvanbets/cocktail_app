from django.urls import path

from recipes.views import FilteredIngredientListView
from . import views
from cocktail_app.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('cocktails/upload', views.upload_cocktail, name='upload-cocktail'),
    path('cocktails/<int:cocktail_id>', views.cocktail_detail),
    path('cocktails/update/<int:cocktail_id>', views.update_cocktail),
    path('cocktails/delete/<int:cocktail_id>', views.delete_cocktail),
    path('ingredients/upload', views.upload_ingredient, name='upload-ingredient'),
    path('ingredients/', FilteredIngredientListView.as_view(), name='ingredients')
]
# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
