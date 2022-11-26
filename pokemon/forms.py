from django import forms
from pokemon.models import Pokemon

'''
Esta clase genera el formulario de registro de los pokemon. Al inicio de esta, se declaran las variables de los campos junto con su tipo de dato.
En la sub-clase Meta, se recibe el modelo de la BDD y luego se definen los campos en los que se escribiran los datos.
'''


class formulario_registro_pokemon(forms.ModelForm):
    nombre = forms.CharField()
    tipo = forms.CharField()
    ataque_base_1 = forms.CharField()
    ataque_especial_1 = forms.CharField()
    dano_base = forms.IntegerField()
    defensa_base = forms.IntegerField()

    class Meta:
        model = Pokemon
        fields = ['nombre','tipo','ataque_base_1','ataque_especial_1','dano_base','defensa_base']

    def clean_nombre(self):
        input_nombre = self.cleaned_data['nombre']
        if len(input_nombre) < 1:
            raise forms.ValidationError("No se ha ingresado un nombre de Pokemon!")
        return input_nombre

    def clean_tipo(self):
        input_tipo = self.cleaned_data['tipo']
        if len(input_tipo) < 1:
            raise forms.ValidationError("No se ha ingresado un tipo de Pokemon!")
        return input_tipo


    nombre.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    ataque_base_1.widget.attrs['class'] = 'form-control'
    ataque_especial_1.widget.attrs['class'] = 'form-control'
    dano_base.widget.attrs['class'] = 'form-control'
    defensa_base.widget.attrs['class'] = 'form-control'

    

        


    '''
    def clean(self):
        user_clean_data = super().clean()

        input_nombre = user_clean_data['nombre']
        if len(input_nombre) < 1:
            raise forms.ValidationError("Campo 'Nombre' vacio.")

    '''


