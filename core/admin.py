from django.contrib import admin

from .models import Cliente, Musica, Produtos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Musica)
admin.site.register(Produtos)
