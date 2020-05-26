from login.forms import LoginForm
from django.test import TestCase
from test_views import crear_usuario


class TestFormLogin(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        self.client.get('/cerrar')

    def test_login_con_campos_validos(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': 'tigre',
                'password': 'tigre123',
            }
        )
        self.assertTrue(form.is_valid())

    def test_login_con_campos_vacios(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': '',
                'password': 'tigre123',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['username']
                          [0], 'Este campo es obligatorio')

        form = LoginForm(
            data={
                'username': 'tigre',
                'password': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password']
                          [0], 'Este campo es obligatorio')

    def test_login_con_username_mayor_a_50_caracteres(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': 'tigretigretigretigretigretigretigretigretigretigretigre',
                'password': 'tigre123',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'][0],
                         'La longitud maxima es de 50')

    def test_login_con_username_menor_a_5_caracteres(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': 'tigr',
                'password': 'tigre123',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'][0],
                         'La longitud minima es de 5')

    def test_login_con_password_mayor_a_16_caracteres(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': 'tigre',
                'password': 'tigre1234567890tigre',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'][0],
                         'La longitud maxima es de 16')

    def test_login_con_password_menor_a_8_caracteres(self):
        crear_usuario(self)
        form = LoginForm(
            data={
                'username': 'tigre',
                'password': 'tigre12',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'][0],
                         'La longitud minima es de 8')
