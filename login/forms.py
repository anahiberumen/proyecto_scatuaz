from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        min_length=5,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'La longitud maxima es de 50',
            'min_length': 'La longitud minima es de 5'
        }
    )
    password = forms.CharField(
        max_length=16,
        min_length=8,
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Contraseña',
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'La longitud maxima es de 16',
            'min_length': 'La longitud minima es de 8'
        }
    )

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Credenciales invalidas'
        super().__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
