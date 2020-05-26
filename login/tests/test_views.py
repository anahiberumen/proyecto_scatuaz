from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class TestViewLogin(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        self.client.get('/cerrar')

    def test_status_ingresar(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_template_ingresar(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login/iniciar.html')

    def test_muestra_campos_del_form(self):
        response = self.client.get('/')
        self.assertInHTML(
            '<input type="text" name="username" class="form-control" placeholder="Nombre de usuario" maxlength="50" minlength="5" required id="id_username">', response.content.decode("utf-8"))
        self.assertInHTML(
            '<input type="password" name="password" class="form-control" placeholder="Contraseña" maxlength="16" minlength="8" required id="id_password">', response.content.decode("utf-8"))

    def test_redirecciona_a_login_sin_estar_logeado(self):
        response = self.client.get('/trabajador/')
        self.assertRedirects(response, '/?next=/trabajador/')
        response = self.client.get('/trabajador/agregar')
        self.assertRedirects(response, '/?next=/trabajador/agregar')
        response = self.client.get('/trabajador/eliminar/1')
        self.assertRedirects(response, '/?next=/trabajador/eliminar/1')
        response = self.client.get('/trabajador/modificar/1')
        self.assertRedirects(response, '/?next=/trabajador/modificar/1')

    def test_login_redirecciona_a_lista_trabajadores(self):
        crear_usuario(self)
        response = self.client.post('/', self.credentials, follow=True)
        self.assertTemplateUsed(response, 'lista_trabajador.html')

    def test_no_muestra_inicio_sesion_si_ya_se_esta_iniciado(self):
        crear_usuario(self)
        response = self.client.post('/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout_manda_a_inicio_de_sesion(self):
        crear_usuario(self)
        self.client.post('/', self.credentials)
        response = self.client.get('/cerrar', follow=True)
        self.assertTemplateUsed(response, 'login/iniciar.html')

    def test_credenciales_incorrectas_regresa_a_login(self):
        response = self.client.post('/', {
            'username': 'tigre',
            'password': '1234567890'
        }, follow=True)
        self.assertTemplateUsed(response, 'login/iniciar.html')

    def test_mostrar_error_de_credenciales_incorrectas(self):
        response = self.client.post('/', {
            'username': 'tigre',
            'password': 'tigre12345'
        }, follow=True)
        self.assertInHTML(
            '<li class="text-danger">Credenciales invalidas</li>', response.content.decode("utf-8"))

    def test_mostrar_error_de_campo_obligatorio(self):
        response = self.client.post('/', {
            'username': 'tigre',
            'password': ''
        }, follow=True)
        self.assertInHTML(
            '<li class="text-danger">Este campo es obligatorio</li>', response.content.decode("utf-8"))
        response = self.client.post('/', {
            'username': '',
            'password': 'tigre123'
        }, follow=True)
        self.assertInHTML(
            '<li class="text-danger">Este campo es obligatorio</li>', response.content.decode("utf-8"))

    def test_cerrar_sesion_sin_estar_logeado_manda_a_inicio_de_sesion(self):
        response = self.client.get('/cerrar', follow=True)
        self.assertTemplateUsed(response, 'login/iniciar.html')

    def test_no_mostrar_inicio_de_sesion_cuando_ya_se_esta_logeado(self):
        crear_usuario(self)
        self.client.post('/', self.credentials)
        response = self.client.get('/')
        self.assertTemplateNotUsed(response, 'login/iniciar.html')


def crear_usuario(self):
    self.credentials = {
        'username': 'tigre',
        'password': 'tigre123'
    }
    User.objects.create_user(**self.credentials)
