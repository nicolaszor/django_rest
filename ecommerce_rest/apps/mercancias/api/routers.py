from rest_framework.routers import DefaultRouter
from apps.mercancias.api.views.mercancias_views import MercanciaViewSet
from apps.mercancias.api.views.general_views import CategoryMercanciaUnitListAPIView,IndicadorListAPIView,MeasureUnitListAPIView

router = DefaultRouter()
router.register(r"mercancias",MercanciaViewSet, basename="mercancias")
router.register(r"measure-unit",MeasureUnitListAPIView, basename="measure_unit_mecancias")
router.register(r"indicadores",IndicadorListAPIView, basename="indicadores_mercancias")
router.register(r"category-mercancias",CategoryMercanciaUnitListAPIView, basename="category_mercancias")

urlpatterns = router.urls #enviamos las routas cradas en router al urlpatterns