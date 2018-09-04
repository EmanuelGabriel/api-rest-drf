from rest_framework import serializers

from .models import Cliente, Musica, Produtos

# Serializers define the API representation.


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # neste caso ‘__all__’ significa que todos os campos serão serializados.
        fields = '__all__'
        # É possível especificar campos, como no código abaixo
        # ('id', 'nome', 'cpf', 'email', 'endereco', 'telefone', 'idade')


# Serializar  a classe MusicaSerializers
class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


