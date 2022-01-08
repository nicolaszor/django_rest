from django.urls import path


from apps.mercancias.api.views.general_views import MeasureUnitListAPIView,CategoryMercanciaUnitListAPIView,IndicadorListAPIView



urlpatterns = [
    path("measure_unit/",MeasureUnitListAPIView.as_view(),name = "measure-unit"),
    path("category-mercancias/",CategoryMercanciaUnitListAPIView.as_view(),name = "category-mercancias"),
    path("indicadores/",IndicadorListAPIView.as_view(),name = "indicador"),
        
]

