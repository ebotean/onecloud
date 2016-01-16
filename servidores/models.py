from django.db import models

# Criação da classe Servidor e seus atributos
class Servidor(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	nome = models.CharField(max_length=150, blank=False)
	host = models.CharField(max_length=100, blank=False)
	cpu = models.IntegerField(default=1)
	ram = models.IntegerField(default=1)
	hd = models.IntegerField(default=1)
	preco = models.DecimalField(max_digits=7, decimal_places=2)
	criador = models.ForeignKey('auth.User', related_name='servidores')

	# Classe meta para ordenação interna
	class Meta:
		ordering = ('preco',)
