from rest_framework import serializers
from servidores.models import Servidor

# Criação do serializador de dados dos servidores
class ServidorSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	nome = serializers.CharField(required=True, allow_blank=False, max_length=150)
	host = serializers.CharField(max_length=100, allow_blank=False)
	cpu = serializers.IntegerField(default=1)
	ram = serializers.IntegerField(default=1)
	hd = serializers.IntegerField(default=1)
	preco = serializers.DecimalField(max_digits=7, decimal_places=2)

	# Cria e retorna as instancias da classe
	def create(self, validated_data):
		return Servidor.objects.create(**validated_data)

	# Atualiza e retorna a instancia alterada
	def update(self, instance, validated_data):
		instance.nome = validated_data.get('nome', instance.nome)
		instance.host = validated_data.get('host', instance.host)
		instance.cpu = validated_data.get('cpu', instance.cpu)
		instance.ram = validated_data.get('ram', instance.ram)
		instance.hd = validated_data.get('hd', instance.hd)
		instance.preco = validated_data.get('preco', instance.preco)
		instance.save()
		return instance