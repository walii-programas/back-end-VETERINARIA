from django.contrib import admin

from veterinaria.models import Cliente 
from veterinaria.models import Veterinario
from veterinaria.models import Tipo_Vacuna
from veterinaria.models import Mascota
from veterinaria.models import Tarjeta_Vacuna
from veterinaria.models import Servicio_Simple
from veterinaria.models import Servicio_Completo
from veterinaria.models import ServicioCI
from veterinaria.models import Servicios
from veterinaria.models import Blog



# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veterinario)
admin.site.register(Tipo_Vacuna)
admin.site.register(Mascota)
admin.site.register(Tarjeta_Vacuna)
admin.site.register(Servicio_Simple)
admin.site.register(Servicio_Completo)
admin.site.register(ServicioCI)
admin.site.register(Servicios)
admin.site.register(Blog)



    