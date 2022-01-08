from django.urls import path
#from apps.users.api.api import UserAPIView
from apps.users.api.api import user_api_view
from apps.users.api.api import user_detail_api_view
"""
urlpatterns = [
    path("usuario/", UserAPIView.as_view(), name = "usuario_api")
]
"""

urlpatterns = [
    path("usuario/", user_api_view, name = "usuario_api"),
    path("usuario/<int:pk>", user_detail_api_view, name = "usuario_detail"),
]