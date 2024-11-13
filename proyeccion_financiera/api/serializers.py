from rest_framework import serializers
from proyeccion_financiera.models import ProyeccionFinanciera
from Users.models import User


class ProyeccionFinancieraSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProyeccionFinanciera
        fields=[ 'id_proyeccion', 'nombre_proyeccion', 'fecha_proyeccion', 'periodo_proyectado',  'informe', 'id_user']  