from rest_framework.routers import    DefaultRouter
from proyeccion_financiera.api.views    import ProyeccionFinancieraApiViewSet

router_proyecccion_financiera= DefaultRouter()
router_proyecccion_financiera.register(prefix='Proyeccion_Financiera', basename='Proyeccion_Financiera', viewset= ProyeccionFinancieraApiViewSet)


