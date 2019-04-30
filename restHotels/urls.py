"""restHotels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from rest.views import hotelViewSet, pessoaViewSet, comentarioViewSet, amigosViewSet, interessesViewSet, vouchersViewSet, chatViewSet, linkServiceViewSet, isDebugViewSet, skinViewSet


router = routers.DefaultRouter()
router.register(r'hotel', hotelViewSet)
router.register(r'pessoa', pessoaViewSet)
router.register(r'comentario', comentarioViewSet)
router.register(r'interesses', interessesViewSet)
router.register(r'amigos', amigosViewSet)
router.register(r'vouchers', vouchersViewSet)
router.register(r'chat', chatViewSet)
router.register(r'links', linkServiceViewSet)
router.register(r'debug', isDebugViewSet)
router.register(r'skin', skinViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
