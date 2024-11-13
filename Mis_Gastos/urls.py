"""
URL configuration for Mis_Gastos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#importación de apis propias
from categoria.api.router import router_categoria
from gastos.api.router    import router_gastos
from proyeccion_financiera.api.router    import router_proyecccion_financiera
from meta_ahorro.api.router  import router_Meta_Ahorro

schema_view = get_schema_view(
   openapi.Info(
      title="MisGastos API",
      default_version='v1',
      description="Documentación Api del proyecto Mis Gastos",
      terms_of_service="",
      contact=openapi.Contact(email="ncamayorive1112@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
  path('admin/', admin.site.urls),
  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  path('api/', include('Users.api.router')),
  path('api/', include(router_categoria.urls)),
  path('api/', include(router_gastos.urls)),
  path('api/', include(router_proyecccion_financiera.urls)),
  path('api/', include(router_Meta_Ahorro.urls)),
  
  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

