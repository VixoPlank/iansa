from django import forms
from .models import Materia, Entradas

class FormularioMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

    codigo = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo',
                                   }))

    nombre = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'nombre'
                                        }))

    descripcion = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'descripcion'
                                        })) 

    existencia = forms.FloatField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'existencia'
                                        }), required=False)




class FormularioEntradas(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = '__all__'


    ni = forms.IntegerField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'ni',
                                            'min':'1000'
                                        }), required=False)

    cantidad = forms.FloatField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'cantidad',
                                            'min':'1',
                                        }))

    oc = forms.IntegerField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'oc',
                                        }))

    nlote = forms.CharField(
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'nlote'
                                        }))

    fecha_ingreso = forms.CharField(
                                    widget=forms.DateTimeInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'fecha_ingreso',
                                            'type': 'date'
                                        }))

    fecha_vencimiento = forms.CharField(
                                    widget=forms.DateInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'fecha_vencimiento',
                                            'type': 'date'
                                        })) 

    proveedor = forms.CharField(max_length=50,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'proveedor',
                                            'style':'text-transform: uppercase'
                                        }))
    

class FormularioMateriaVista(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

    codigo = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo',
                                       'readonly':'readonly'
                                   }))

    nombre = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'nombre',
                                            'readonly':'readonly'
                                        }))

    descripcion = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'descripcion',
                                            'readonly':'readonly'
                                        })) 

    existencia = forms.FloatField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-64 h-16 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'existencia',
                                            'readonly':'readonly'
                                        }), required=False)
