from django.db import models

# Create your models here.
 #'...'
    #def __init__(self, verbose_name=None, name=None, primary_key=False,
                # max_length=None, unique=False, blank=False, null=False,
                # db_index=False, rel=None, default=NOT_PROVIDED, editable=True,
                # serialize=True, unique_for_date=None, unique_for_month=None,
                # unique_for_year=None, choices=None, help_text='',
                # db_column=None, db_tablespace=None, auto_created=False):
        #'...'


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome', help_text='Digite seu nome')
    cpf = models.IntegerField(blank=True, null=True, verbose_name='CPF', help_text='Digite seu CPF')
    email = models.EmailField(max_length=60, blank=True, null=True, verbose_name='E-mail', help_text='Digite seu e-mail')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço', help_text='Digite seu endereço')
    telefone = models.IntegerField(blank=True, null=True, verbose_name='Nº telefone celular', help_text='Digite seu telefone')
    idade = models.IntegerField(blank=True, null=True, verbose_name='Idade', help_text='Digite sua idade')

    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    musica = models.CharField(max_length=100, verbose_name='Nome da Música')
    compositor = models.CharField(max_length=100, verbose_name='Compositor')

    def __str__(self):
        return self.musica



class Produtos(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return self.nome



