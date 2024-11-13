from django.contrib import admin
from proyeccion_financiera.models  import  ProyeccionFinanciera
# Register your models here.

@admin.register( ProyeccionFinanciera)

class  ProyeccionFinanciera(admin.ModelAdmin):
    list_display= ['id_proyeccion','nombre_proyeccion','fecha_proyeccion',
                   'periodo_proyectado','informe','id_user']#'mostrar_imagen'