from django.contrib.auth.models import User
from usuario.forms import UsuarioForm, CambiarContrasenaForm
from django.test import TestCase


class TestFormUsuario(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_crear_usuario_con_campos_validos(self):
        credenciales = {
            'username': 'salvador',
            'email': 'loera@gmail.com',
            'password1': 'loera123',
            'password2': 'loera123',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertTrue(form.is_valid())

    def test_crear_usuario_con_campos_vacios(self):
        credenciales = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['username']
                          [0], 'El campo Usuario es obligatorio')
        self.assertEquals(form.errors['email'][0],
                          'El campo Correo Electrónico es obligatorio')
        self.assertEquals(form.errors['password1']
                          [0], 'El campo Contraseña es obligatorio')
        self.assertEquals(form.errors['password2'][0],
                          'El campo Repita Contraseña es obligatorio')

    def test_crear_usuario_con_username_mayor_a_50(self):
        credenciales = {
            'username': 'salvadorsalvadorsalvadorsalvadorsalvadorsalvadorsalvador',
            'email': 'loera@gmail.com',
            'password1': 'loera123',
            'password2': 'loera123',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['username']
                          [0], 'La longitud maxima es de 50')

    def test_crear_usuario_con_username_menor_a_5(self):
        credenciales = {
            'username': 'salv',
            'email': 'loera@gmail.com',
            'password1': 'loera123',
            'password2': 'loera123',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['username']
                          [0], 'La longitud minima es de 5')

    def test_crear_usuario_con_email_mayor_a_50(self):
        credenciales = {
            'username': 'salvador',
            'email': 'loeraloeraloeraloeraloeraloeraloeraloeraloera@gmail.com',
            'password1': 'loera123',
            'password2': 'loera123',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['email'][0],
                          'La longitud maxima es de 50')

    def test_crear_usuario_con_email_invalido(self):
        credenciales = {
            'username': 'salvador',
            'email': 'email@invalido',
            'password1': 'loera123',
            'password2': 'loera123',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['email'][0],
                          'Introduzca una dirección de correo electrónico válida.')

    def test_crear_usuario_con_password_mayor_a_16_caracteres(self):
        credenciales = {
            'username': 'salvador',
            'email': 'loera@gmail.com',
            'password1': 'loera1234567890loera',
            'password2': 'loera1234567890loera',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password1']
                          [0], 'La longitud maxima es de 16')
        self.assertEquals(form.errors['password2']
                          [0], 'La longitud maxima es de 16')

    def test_crear_usuario_con_password_menor_a_8_caracteres(self):
        credenciales = {
            'username': 'salvador',
            'email': 'loera@gmail.com',
            'password1': 'loera',
            'password2': 'loera',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password1']
                          [0], 'La longitud minima es de 8')
        self.assertEquals(form.errors['password2']
                          [0], 'La longitud minima es de 8')

    def test_crear_usuario_con_username_ya_existente(self):
        User.objects.create_user(
            username='salvador',
            email='shava@gmail.com',
            password='loera123'
        )
        credenciales = {
            'username': 'salvador',
            'email': 'loera@gmail.com',
            'password1': 'loera',
            'password2': 'loera',
            'is_superuser': 'True',
        }
        form = UsuarioForm(
            data=credenciales
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['username'][0],
                          'Ya existe un usuario con ese nombre.')

    def test_solo_almacenar_un_nuevo_usuario(self):
        user = User.objects.create_user(
            username='salvador',
            email='shava@gmail.com',
            password='loera123'
        )

        self.assertEquals(user, User.objects.first())
        self.assertEquals(1, User.objects.all().count())


class TestFormCambiarContrasena(TestCase):

    def setUp(self):
        self.usuario = User.objects.create(
            username='salvador',
            email='shava@gmail.com',
            password='loera123'
        )
        self.data = {
            'new_password1': '123456789',
            'new_password2': '123456789'
        }

    def tearDown(self):
        pass

    def test_cambiar_contrasena_con_campos_vacios(self):
        self.data['new_password1'] = ''
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors['new_password1'][0], 'El campo Nueva Contraseña es obligatorio')

        self.data['new_password2'] = ''
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors['new_password1'][0], 'El campo Nueva Contraseña es obligatorio')
        self.assertEquals(form.errors['new_password2'][0],
                          'El campo Repita Nueva Contraseña es obligatorio')

    def test_cambiar_contrasena_con_password_mayor_a_16(self):
        self.data['new_password1'] = 'loeraloeraloeralo'
        self.data['new_password2'] = 'loeraloeraloeralo'
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['new_password1']
                          [0], 'La longitud maxima es de 16')
        self.assertEquals(form.errors['new_password2']
                          [0], 'La longitud maxima es de 16')

    def test_cambiar_contrasena_con_password_menor_a_8(self):
        self.data['new_password1'] = 'loera'
        self.data['new_password2'] = 'loera'
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['new_password1']
                          [0], 'La longitud minima es de 8')
        self.assertEquals(form.errors['new_password2']
                          [0], 'La longitud minima es de 8')

    def test_cambiar_contrasena_con_contrasenas_no_coincidentes(self):
        self.data['new_password1'] = 'loera123'
        self.data['new_password2'] = 'loera321'
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertFalse(form.is_valid())

    def test_cambiar_contrasena_valida(self):
        self.data['new_password1'] = 'loera1234'
        self.data['new_password2'] = 'loera1234'
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertTrue(form.is_valid())

    def test_cambio_de_contrasena_reflejado(self):
        self.data['new_password1'] = 'loera1234'
        self.data['new_password2'] = 'loera1234'
        form = CambiarContrasenaForm(
            self.usuario,
            data=self.data
        )
        self.assertTrue(form.is_valid())

        form.save()
        self.client.login(
            username=self.usuario.username,
            password='loera1234'
        )
        self.assertTrue(self.usuario.is_authenticated)
