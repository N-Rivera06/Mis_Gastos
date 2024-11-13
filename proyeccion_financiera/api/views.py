from rest_framework.viewsets import ModelViewSet
from proyeccion_financiera.models import ProyeccionFinanciera
from proyeccion_financiera.api.serializers import ProyeccionFinancieraSerializers
from proyeccion_financiera.api.permissions import IsAdminReadOnly


class ProyeccionFinancieraApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class= ProyeccionFinancieraSerializers
    queryset = ProyeccionFinanciera.objects.all()
