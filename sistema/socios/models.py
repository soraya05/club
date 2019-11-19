from django.db import models

# Create your models here.
class Socio(models.Model):
	nombre = models.CharField(max_length=80)
	numero = models.CharField(max_length=80)
	

	def __str__(self):
		return self.nombre+" - "+self.numero

class Cuota(models.Model):
	año = models.IntegerField()
	mes = models.IntegerField()
	pagado = models.BooleanField()
	socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

	def __str__(self):
		return str (self.mes) +"/"+ str(self.año)+" - " + self.socio.nombre