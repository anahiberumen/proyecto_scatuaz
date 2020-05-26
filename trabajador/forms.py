from .models import Trabajador, OPCIONES_SEXO, OPCIONES_ESTUDIOS 
from django import forms


class TrabajadorForm(forms.ModelForm):
    # DATOS PERSONALES
    paterno = forms.CharField(
        required=True,
        label='Apellido Paterno',
        error_messages={
            'required': 'El campo Apellido Paterno es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    materno = forms.CharField(
        required=True,
        label='Apellido Materno',
        error_messages={
            'required': 'El campo Apellido Materno es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nombre = forms.CharField(
        required=True,
        label='Nombre',
        max_length=50,
        error_messages={
            'required': 'El campo Nombre es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    rfc = forms.CharField(
        required=True,
        label='RFC',
        max_length=13,
        error_messages={
            'required': 'El campo RFC es obligatorio',
            'max_length': 'La longitud maxima es de 13 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    curp = forms.CharField(
        required=True,
        label='CURP',
        max_length=18,
        min_length=18,
        error_messages={
            'required': 'El campo CURP es obligatorio',
            'min_length': 'La longitud debe ser de 18 caracteres',
            'max_length': 'La longitud debe ser de 18 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    sexo = forms.ChoiceField(
        required=True,
        label='Sexo',
        choices=OPCIONES_SEXO,
        error_messages={
            'required': 'El campo Sexo es obligatorio',
        },
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-input'},
        )
    )
    pais_residencia = forms.CharField(
        required=True,
        label='País de Residencia',
        error_messages={
            'required': 'El campo País de Residencia es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    estado_residencia = forms.CharField(
        required=True,
        label='Estado de Residencia',
        error_messages={
            'required': 'El campo Estado de Residencia es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    municipio_residencia = forms.CharField(
        required=True,
        label='Municipio de Residencia',
        error_messages={
            'required': 'El campo Municipio de Residencia es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    calle = forms.CharField(
        required=True,
        label='Calle de Residencia',
        error_messages={
            'required': 'El campo Calle de Residencia es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    numero = forms.CharField(
        required=True,
        label='Numero',
        error_messages={
            'required': 'El campo Numero es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    colonia = forms.CharField(
        required=True,
        label='Colonia de Residencia',
        error_messages={
            'required': 'El campo Colonia de Residencia es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    cp = forms.CharField(
        required=True,
        label='CP',
        error_messages={
            'required': 'El campo CP es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    telefono = forms.CharField(
        required=False,
        max_length=10,
        min_length=7,
        label='Teléfono',
        error_messages={
            'required': 'El campo Teléfono es obligatorio',
            'min_length': 'La longitud minima es de 7 caracteres',
            'max_length': 'La longitud maxima es de 10 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        required=False,
        label='Correo Electrónico',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    # DATOS LABORALES
    matricula_administrativo = forms.CharField(
        required=True,
        max_length=6,
        label='Matricula de Administrativo',
        error_messages={
            'required': 'El campo Matricula de Administrativo es obligatorio',
            'max_length': 'La longitud maxima es de 6 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    matricula_gremial = forms.CharField(
        required=True,
        max_length=6,
        label='Matricula Gremial',
        error_messages={
            'required': 'El campo Matricula Gremial es obligatorio',
            'max_length': 'La longitud maxima es de 6 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # DATOS ACADEMICOS
    grado_max_estudios = forms.ChoiceField(
        required=True,
        label='Grado Max de Estudios',
        choices=OPCIONES_ESTUDIOS, 
        error_messages={
            'required': 'El campo Grado Max de Estudios es obligatorio',
        },
        widget=forms.Select(
            attrs={'class': 'form-control'},
        )
    )
    # DATOS ISSSTE
    nss = forms.CharField(
        required=False,
        max_length=11,
        label='NSS',
        error_messages={
            'max_length': 'La longitud maxima es de 11 caracteres'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    no_issste = forms.CharField(
        required=False,
        label='No. de ISSSTE',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # REGISTROS
    validado_renapo = forms.BooleanField(
        required=False,
        label='Validado por RENAPO',
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        )
    )
    validado_siri = forms.BooleanField(
        required=False,
        label='Validado por SIRI',
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input',}
        )
    )
    

    class Meta:
        model = Trabajador
        exclude = ('alta_usuario',)
