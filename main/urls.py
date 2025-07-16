from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produto.urls')),  # Inclui as rotas do app produto
    path('', include('produto.urls')),

    
   
]

