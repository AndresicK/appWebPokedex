from django.contrib import admin
from pokemon.models import Pokemon
from pokemon.models import PokeMart
#Esta clase sirve para mostrar los pokémon en la interfaz de Django Admin
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipo','ataque_base_1','ataque_especial_1','dano_base','defensa_base']

class pokemartAdmin(admin.ModelAdmin):
    list_display = ['nombreObjeto', 'precio', 'cantidad', 'lugar', 'tipo', 'fechaCompra']


# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokeMart, pokemartAdmin)
