"""homeflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Página admin site
    path('', include('filme.urls', namespace='filme')),  # Configurando a página padrão do site (inclui todas as URL do projeto com o nome 'filme')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Instrução para o admin incluir imagens e arquivos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Instrução, para o usuário incluir imagens e arquivos