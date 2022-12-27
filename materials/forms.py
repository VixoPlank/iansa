from django import forms
from .models import Materia, Entradas

class FormularioMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

    codigo = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo'
                                   }))

    nombre = forms.CharField(max_length=100,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
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
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'existencia', 
                                            'readonly': 'readonly'
                                        }), required=False)



class FormularioEntradas(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = '__all__'

    ni = forms.IntegerField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'ni',
                                            'disabled': 'disabled'
                                        }), required=False)

    cantidad = forms.FloatField(
                                    widget=forms.NumberInput(
                                        attrs={
                                            'class': 'w-80 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'cantidad',
                                            'pattern':'^[0-9]+'
                                        }))

    fecha_ingreso = forms.CharField(
                                    widget=forms.DateTimeInput(
                                        attrs={
                                            'class': 'w-60 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'fecha_ingreso',
                                            'type': 'datetime-local'
                                        }))

    fecha_vencimiento = forms.CharField(
                                    widget=forms.DateInput(
                                        attrs={
                                            'class': 'w-80 block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                            'id': 'fecha_vencimiento',
                                            'type': 'date'
                                        })) 