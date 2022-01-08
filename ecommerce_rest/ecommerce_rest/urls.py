"""ecommerce_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.views import Login, Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='0.1',
      description="Documentacion publica de API de Ecommerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nico.zorzi@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuario/",include("apps.users.api.urls")),
    path("products/",include("apps.products.api.urls")),
    path("mercancias/",include("apps.mercancias.api.routers")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#retorna el token de acceso y de refresco para un usuario y contraceña que se envie
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#refresca el token que se utiliza para acceder
    #incluimos las rutas de swagger
    path('logout/', Logout.as_view(),name = "Logout"),
    path('login/', Login.as_view(),name ="Login-user"),
    #path("refresh-token/",UserToken.as_view(), name = "refresh-token"),
    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    re_path(
        r'^media/(?P<path>.*)$', serve, {
            "document_root": settings.MEDIA_ROOT,
        }
    )
]