from django import forms
from .models import Receta


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
                                       }),required=False)

    codigo_2 = forms.IntegerField(
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                       'id': 'codigo_2'
                                   }),required=False)

    kg_2 = forms.FloatField(
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'block rounded-t-lg px-2.5 pb-2.5 pt-5 text-sm text-gray-900 bg-gray-50 dark:bg-gray-700 border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-green-500 focus:outline-none focus:ring-0 focus:border-green-600 peer',
                                   'id': 'kg_2'
                               }),required=False)

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
