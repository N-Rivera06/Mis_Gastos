from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from Users.models import User

@admin.register(User)
#Registre yout models here.
class UserAdmin(BaseUserAdmin):
    pass


admin.site.site_header = _("Mi panel de Administración")
admin.site.site_title =_("Mi Sitio de Administración")
admin.site.index_title= _('Bienvenido al Panel de Administración')