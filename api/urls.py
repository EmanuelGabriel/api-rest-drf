from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet, MusicaViewSet, ProdutoViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'musicas', MusicaViewSet)
router.register(r'produtos', ProdutoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))

]
