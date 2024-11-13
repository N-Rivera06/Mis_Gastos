from django.db import models
from Users.models import User
#from django.utils.html import format_html aqui también va lo de la imagen

# Create your models here.

class ProyeccionFinanciera(models.Model):
    SEMANAL = 'Semanal'
    QUINCENAL = 'Quincenal'
    MENSUAL = 'Mensual'
    ANUAL = 'Anual'

    PERIODO_CHOICES = [
        (SEMANAL, 'Semanal'),
        (QUINCENAL, 'Quincenal'),
        (MENSUAL, 'Mensual'),
        (ANUAL, 'Anual'),
    ]
    
    id_proyeccion = models.AutoField(primary_key=True)
    fecha_proyeccion = models.DateField()
    
    periodo_proyectado = models.CharField(
        max_length=10,
        choices=PERIODO_CHOICES,
        default=MENSUAL,  
    )
    nombre_proyeccion = models.CharField(max_length=255)
    informe = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)
    #imagen = models.ImageField(upload_to='proyeccion/', null=True, blank=True) esto también es para la imagen- pero ojo tambien se debe crear en el php la opcion IMAGEN EN LA TABLA
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'proyeccion_financiera'

# este es el proceso para poner una imagen 

    #def mostrar_imagen(self):
        #if self.imagen:
            #return format_html('<img src="{}" width="80" height="70">'.format(self.imagen.url))
        #else:
            #return ''
    #mostrar_imagen.short_description= 'Imagen'

  
