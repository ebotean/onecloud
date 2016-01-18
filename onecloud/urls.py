"""onecloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from servidores import views
from rest_framework.routers import SimpleRouter
from servidores.views import Index, ServidorViewSet, UsuarioViewSet

router = SimpleRouter()
router.register(r'api/v1/servidores', views.ServidorViewSet)
router.register(r'api/v1/usuarios', views.UsuarioViewSet)



# Lista de URLs a serem tratadas pelo roteador
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^servidores/', Index.as_view(), name="index"),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # url('^.*$', IndexView.as_view(), name='index'),   
]

urlpatterns += router.urls