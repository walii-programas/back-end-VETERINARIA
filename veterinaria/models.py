from django.db import models
from datetime import date
from django.utils.translation import gettext as _



class Cliente(models.Model):
    """
        Modelo CLIENTE
    """   
    Nombre_Apellidos = models.CharField(max_length = 150, verbose_name = _('Nombres'))
    DNI = models.CharField(max_length = 8, verbose_name = _("DNI"))
    Telefono_Celular = models.CharField(max_length = 10, verbose_name = _("Teléfono celular"))
    Foto = models.ImageField("Foto de perfil", upload_to='Cliente', blank=True)
    Direccion = models.TextField(verbose_name = _('Dirección'))
    Correo_User = models.EmailField(max_length =200, verbose_name = _("Correo usuario"))
    Contrasenia = models.CharField(max_length = 100,verbose_name = _("Contraseña"))    
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Cliete")
        verbose_name_plural =_("Clientes")
    def __str__(self): 
        return self.Nombre_Apellidos

class Veterinario(models.Model):
    """
    modelo VETERINARIO
    """
    CMVP = models.CharField(max_length = 10 , verbose_name = _('CMPV'))
    Nombre_Apellidos = models.CharField(max_length = 150, verbose_name = _("Nombres"))
    DNI = models.CharField(max_length = 8, verbose_name = _("DNI"))
    Telefono_Celular = models.CharField(max_length = 10, verbose_name = _("Teléfono celular"))
    Direccion = models.TextField(verbose_name = _('Dirección'))
    CorreoUser = models.EmailField(max_length =200, verbose_name = _("Correo usuario"))
    Contrasenia = models.CharField(max_length = 100, verbose_name = _("Contraseña"))
    Foto = models.ImageField("Foto de perfil", upload_to='Veterinario', blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Veterinario")
        verbose_name_plural =_("Veterinarios")
    def __str__(self): 
        return self.Nombre_Apellidos

class Tipo_Vacuna(models.Model):
    """
    modelo TIPO VACUNA
    """    
    Nombre = models.CharField(max_length = 150, verbose_name = _("Nombre"))
    Descripcion = models.TextField(verbose_name = _('Descripción'))
    Cantidad = models.IntegerField( verbose_name = _("Cantidad"), default = 0)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Tipo Vacuna")
        verbose_name_plural =_("Tipo Vacunas")
    def __str__(self): 
        return self.Nombre

class Mascota(models.Model):
    """
    modelo MASCOTA
    """
    Nombre = models.CharField(max_length = 100, verbose_name = _("Nombre"))
    Especie = models.CharField(max_length = 100, verbose_name = _("Especie"))
    Raza = models.CharField(max_length = 100, verbose_name = _("Raza"))
    Edad = models.IntegerField(verbose_name = _('Edad en meses'), default = 0)
    Color = models.CharField(max_length =100, verbose_name = _("Color"))   
    Peso = models.IntegerField(verbose_name = _('Peso en Gramo'), default = 0)
    Temperatura_C = models.IntegerField(verbose_name = _('Temperatura Corporal'), default = 0)
    Observaciones = models.CharField(max_length =300, verbose_name = _("Observaciones"))
    Fecha_Nacimiento = models.DateField(_("Fecha nacimiento"), auto_now=False, auto_now_add=False)    
    Foto = models.ImageField(_("Foto de perfil"), upload_to='Mascota', blank=True)


    Cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)   
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)     

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Mascota")
        verbose_name_plural =_("Mascotas")
    def __str__(self): 
         return self.Nombre
         return 'C:{} -> M: {}'.format(self.Cliente.NombreA_pellidos, self.NombreA_pellidos)
        

class Tarjeta_Vacuna(models.Model):
    """
    modelo TARJETA VACUNA
    """    
    Fecha_Programada = models.DateField(_("Fecha Programada"), auto_now=False, auto_now_add=False)   
    Descripcion = models.TextField(verbose_name = _('Descripción'))
    Fecha_Aplicada = models.DateField(_("Fecha Aplicada"), auto_now=False, auto_now_add=False, blank=True) 
    Costo = models.IntegerField(verbose_name = _('Costo en soles S/'), default = 0) 


    Mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    Tipo_Vacuna = models.ForeignKey('Tipo_Vacuna', on_delete=models.CASCADE)
    Veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)
       

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Tarjeta vacuna")
        verbose_name_plural =_("Tarjeta vacunas")
    def __str__(self): 
         return self.Descripcion
         return 'M:{} -> T: {}'.format(self.Mascota.Nombre, self.Nombre)
         return 'T:{} -> T: {}'.format(self.Tipo_Vacuna.Nombre, self.Nombre)
         return 'M:{} -> S: {}'.format(self.Veterinario.Nombre_Apellidos, self.Nombre_Apellidos)


class Servicio_Simple(models.Model):
    """
    modelo SERVICIO SIMPLE
    """    
    Fecha = models.DateField(_("Fecha del servicio"), auto_now=False, auto_now_add=False)   
    Descripcion = models.TextField(verbose_name = _('Descripción'))
    Costo = models.IntegerField(verbose_name = _('Costo en soles S/'), default = 0)
   


    Mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    Veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)
    
   

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Servicio simple")
        verbose_name_plural =_("Servicios simples")
    def __str__(self): 
         return self.Descripcion
         return 'M:{} -> T: {}'.format(self.Mascota.Nombre, self.Nombre)
         return 'M:{} -> S: {}'.format(self.Veterinario.Nombre_Apellidos, self.Nombre_Apellidos)


class Servicio_Completo(models.Model):
    """
    modelo SERVICIO COMPLETO
    """
    Sintomas = models.TextField(verbose_name = _('Sintomas'))
    Diagnostico = models.TextField(verbose_name = _('Diagnostico'))    
    Tratamiento = models.TextField(verbose_name = _('Tratamiento'))
    Descripcion = models.TextField(verbose_name = _('Descripción'), blank=True)
    Costo = models.IntegerField(verbose_name = _('Costo en soles S/'), default = 0)   


    Mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    Veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)
   

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Servicio completo")
        verbose_name_plural =_("Servico completos")
    def __str__(self): 
        return self.Sintomas
        return 'M:{} -> T: {}'.format(self.Mascota.Nombre, self.Nombre)
        return 'M:{} -> S: {}'.format(self.Veterinario.Nombre_Apellidos, self.Nombre_Apellidos)
       




class ServicioCI(models.Model):
    """
    modelo SERVICIO COMPLETO INTERNADO
    """
    Fecha_Internado = models.DateField(_("Fecha internado"), auto_now=False, auto_now_add=False)  
    Sintomas = models.TextField(verbose_name = _('Sintomas'))
    Diagnostico = models.TextField(verbose_name = _('Diagnostico'))    
    Tratamiento = models.TextField(verbose_name = _('Tratamiento'))
    Mejora_Descripcion = models.TextField(verbose_name = _('Mejora en los días internado'))
    Costo = models.IntegerField(verbose_name = _('Costo en soles S/'), default = 0)   


    Mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    Veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)
   

    class Meta:
        ordering=["Creado"]
        verbose_name = _("Servicio IC")
        verbose_name_plural =_("Servico IC's")
    def __str__(self): 
        return self.Mejora_Descripcion
        return 'M:{} -> T: {}'.format(self.Mascota.Nombre, self.Nombre)
        return 'M:{} -> S: {}'.format(self.Veterinario.Nombre_Apellidos, self.Nombre_Apellidos)

    
class Servicios(models.Model):
    """
    modelo SERVICIO
    """    
    Nombre = models.CharField(max_length = 150, verbose_name = _("Nombre"))
    Descripcion = models.TextField(verbose_name = _('Descripción'))
    Foto = models.ImageField(_("Foto de perfil"), upload_to='Mascota', blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=["Creado"]
        verbose_name = _("Servicio")
        verbose_name_plural =_("Servicios")
    def __str__(self): 
        return self.Nombre
       
class Blog(models.Model):
    """
    modelo BLOG
    """    
    Nombre = models.CharField(max_length = 150, verbose_name = _("Nombre"))
    Descripcion = models.TextField(verbose_name = _('Descripción'))
    Foto = models.ImageField(_("Foto de perfil"), upload_to='Mascota', blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=["Creado"]
        verbose_name = _("Blog")
        verbose_name_plural =_("Tipo Blog")
    def __str__(self): 
        return self.Nombre
       



