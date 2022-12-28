from django import forms
from .models import Receta,Producto
from materials.models import Materia

class FormularioMateria2(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

    codigo = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo'
                                   }))

    nombre = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'nombre'
                                        }))

    descripcion = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'descripcion'
                                        }), required=False) 

    existencia = forms.FloatField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'existencia', 
                                            
                                        }), required=False)


class FormularioReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

    producto = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'w-80 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'producto'
                                   }))

    componente_1 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_1'
                                       }))

    codigo_1 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_1',
                                   }),)

    kg_1 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_1',
                               }))

    componente_2 = forms.CharField(max_length=20,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'producto'
                                       }),required=True)

    codigo_2 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_2'
                                   }),required=True)

    kg_2 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_2'
                               }),required=True)

    componente_3 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_3'
                                       }),required=False)

    codigo_3 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_3'
                                   }),required=False)

    kg_3 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_3'
                               }),required=False)

    componente_4 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_4'
                                       }),required=False)

    codigo_4 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_4'
                                   }),required=False)

    kg_4 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_4'
                               }),required=False)

    componente_5 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_5'
                                       }),required=False)

    codigo_5 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_5'
                                   }),required=False)

    kg_5 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_5'
                               }),required=False)

    componente_6 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_6'
                                       }),required=False)

    codigo_6 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_6'
                                   }),required=False)

    kg_6 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_6'
                               }),required=False)

    componente_7 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_7'
                                       }),required=False)

    codigo_7 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_7'
                                   }),required=False)

    kg_7 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_7'
                               }),required=False)

    componente_8 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_8'
                                       }),required=False)

    codigo_8 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_8'
                                   }),required=False)

    kg_8 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_8'
                               }),required=False)

    componente_9 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_9'
                                       }),required=False)

    codigo_9 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_9'
                                   }),required=False)

    kg_9 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_9'
                               }),required=False)

    componente_10 = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'componente_10'
                                        }),required=False)

    codigo_10 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_10'
                                       'max_len'
                                   }),required=False)

    kg_10 = forms.FloatField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'kg_10'
                                   }),required=False)



class FormularioFabricacion(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    lote = forms.IntegerField(widget=forms.TextInput(
                                   attrs={
                                       'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'lote'
                                   }))

    producto = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'producto'
                                   }))

    componente_1 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_1'
                                       }))

    codigo_1 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_1',
                                   }),)

    kg_1 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_1',
                               }))

    NI1_1 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_1'
                                       'max_len'
                                   }),required=False)

    NI2_1 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_1'
                                       'max_len'
                                   }),required=False)

    componente_2 = forms.CharField(max_length=20,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_2'
                                       }),required=True)

    codigo_2 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_2'
                                   }),required=True)

    kg_2 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_2'
                               }),required=True)

    NI1_2 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_2'
                                       'max_len'
                                   }),required=False)

    NI2_2 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_2'
                                       'max_len'
                                   }),required=False)

    componente_3 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_3'
                                       }),required=False)

    codigo_3 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_3'
                                   }),required=False)

    kg_3 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_3'
                               }),required=False)

    NI1_3 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_3'
                                       'max_len'
                                   }),required=False)

    NI2_3 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_3'
                                       'max_len'
                                   }),required=False)

    componente_4 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_4'
                                       }),required=False)

    codigo_4 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_4'
                                   }),required=False)

    kg_4 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_4'
                               }),required=False)

    NI1_4 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_4'
                                       'max_len'
                                   }),required=False)

    NI2_4 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_4'
                                       'max_len'
                                   }),required=False)

    componente_5 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_5'
                                       }),required=False)

    codigo_5 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_5'
                                   }),required=False)

    kg_5 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_5'
                               }),required=False)

    NI1_5 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_5'
                                       'max_len'
                                   }),required=False)

    NI2_5 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_5'
                                       'max_len'
                                   }),required=False)

    componente_6 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_6'
                                       }),required=False)

    codigo_6 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_6'
                                   }),required=False)

    kg_6 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_6'
                               }),required=False)
    
    NI1_6 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_6'
                                       'max_len'
                                   }),required=False)

    NI2_6 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_6'
                                       'max_len'
                                   }),required=False)

    componente_7 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_7'
                                       }),required=False)

    codigo_7 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_7'
                                   }),required=False)
                        
    NI1_7 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_7'
                                       'max_len'
                                   }),required=False)

    NI2_7 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_7'
                                       'max_len'
                                   }),required=False)

    kg_7 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_7'
                               }),required=False)

    componente_8 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_8'
                                       }),required=False)

    codigo_8 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_8'
                                   }),required=False)

    kg_8 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_8'
                               }),required=False)

    NI1_8 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_8'
                                       'max_len'
                                   }),required=False)

    NI2_8 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_8'
                                       'max_len'
                                   }),required=False)

    componente_9 = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                           'id': 'componente_9'
                                       }),required=False)

    codigo_9 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_9'
                                   }),required=False)

    kg_9 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_9'
                               }),required=False)

    NI1_9 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_9'
                                       'max_len'
                                   }),required=False)

    NI2_9 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_9'
                                       'max_len'
                                   }),required=False)

    componente_10 = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-55 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'componente_10'
                                        }),required=False)

    codigo_10 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_10'
                                       'max_len'
                                   }),required=False)

    kg_10 = forms.FloatField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'kg_10'
                                   }),required=False)

    NI1_10 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI1_10'
                                       'max_len'
                                   }),required=False)

    NI2_10 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-24 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'NI2_10'
                                       'max_len'
                                   }),required=False)
    
    observacion = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'observacion'
                                        }),required=False)