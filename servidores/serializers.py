from rest_framework import serializers
from servidores.models import Servidor
from django.contrib.auth.models import User

# Criação do serializador de dados dos servidores
class ServidorSerializer(serializers.HyperlinkedModelSerializer):
	criador = serializers.ReadOnlyField(source='criador.username')

	class Meta:
		model = Servidor
		fields = ('created','url','nome', 'host', 'cpu', 'ram', 'hd', 'preco', 'criador')

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
	servidores = serializers.HyperlinkedRelatedField(many=True, view_name='servidor-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'username', 'servidores')