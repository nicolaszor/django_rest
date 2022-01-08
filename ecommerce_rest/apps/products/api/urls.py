from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView,CategoryProductUnitListAPIView,IndicadorListAPIView
from apps.products.api.views.product_views import (ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path("measure_unit/",MeasureUnitListAPIView.as_view(),name = "measure-unit"),
    path("category_products/",CategoryProductUnitListAPIView.as_view(),name = "category-products"),
    path("indicadores/",IndicadorListAPIView.as_view(),name = "indicador"),
    #path("product/list/",ProductListAPIView.as_view(),name = "product_list"),
    path("product/",ProductListCreateAPIView.as_view(),name = "product-create"),
    path("product/retrieve-update-destroy/<int:pk>/",ProductRetrieveUpdateDestroyAPIView.as_view(),name = "product_retrieve_update_destroy"),
    #path("product/destroy/<int:pk>/",ProductDestroyAPIView.as_view(),name = "product_destroy"),
    #path("product/update/<int:pk>/",ProductUpdateAPIView.as_view(),name = "product_update"),
    
]
