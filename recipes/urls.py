from django.urls import path
from . import views
from cocktail_app.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('upload/', views.upload, name='upload-recipe'),
    path('cocktails/<int:cocktail_id>', views.cocktail_detail),
    path('cocktails/update/<int:cocktail_id>', views.update_cocktail),
    path('cocktails/delete/<int:cocktail_id>', views.delete_cocktail)
]
# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
