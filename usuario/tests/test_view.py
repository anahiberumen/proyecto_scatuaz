from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from usuario import forms


class TestViewListaUsuario(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='santana',
            email='santana@gmail.com',
            password='elmickey123'
        )
        self.client.login(
            username='santana',
            password='elmickey123'
        )

    def tearDown(self):
        self.client.logout()

    def test_muestra_bloque_usuario_en_base(self):
        response = self.client.get('/trabajador/')
        self.assertInHTML(
            '<a class="nav-link" href="/usuario/">Usuarios</a>', response.content.decode("utf-8"))

    def test_url_lista_usuario(self):
        response = self.client.get('/usuario/')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_lista_usuario(self):
        response = self.client.get(reverse('lista_usuario'))
        self.assertEqual(response.status_code, 200)

    def test_template_lista_usuario(self):
        response = self.client.get('/usuario/')
        self.assertTemplateUsed(response, 'lista_usuario.html')

    def test_prohibe_acceso_a_no_administradores(self):
        self.client.logout()
        self.user = User.objects.create_user(
            username='fatima',
            email='fatima@gmail.com',
            password='fatima123'
        )
        self.client.login(
            username='fatima',
            password='fatima123'
        )
        response = self.client.get('/usuario/')
        self.assertTemplateNotUsed(response, 'lista_usuario.html')

    def test_muestra_el_usuario_registrado(self):
        response = self.client.get('/usuario/')
        self.assertInHTML(self.user.username, response.content.decode("utf-8"))

    def test_muestra_usuarios_no_admin(self):
        user2 = User.objects.create_user(
            username='shava',
            email='shava@gmail.com',
            password='loera123'
        )
        response = self.client.get('/usuario/')
        self.assertInHTML(self.user.username, response.content.decode("utf-8"))
        self.assertInHTML(user2.username, response.content.decode("utf-8"))

    def test_muestra_usuario_correo_y_si_es_admin(self):
        response = self.client.get('/usuario/')
        self.assertInHTML(self.user.username, response.content.decode("utf-8"))
        self.assertInHTML(self.user.email, response.content.decode("utf-8"))
        self.assertInHTML(
            '<td class="text-center">Si</td>', response.content.decode("utf-8"))

    def test_muestra_botones_para_eliminar_y_modificar(self):
        response = self.client.get('/usuario/')
        self.assertInHTML('<a href="/usuario/eliminar/'+str(self.user.id) +
                          '" class="btn btn-danger btn-sm">Eliminar</a>', response.content.decode("utf-8"))
        self.assertInHTML('<a href="/usuario/modificar/'+str(self.user.id) +
                          '" class="btn btn-primary btn-sm mr-4">Editar</a>', response.content.decode("utf-8"))


class TestViewAgregarUsuario(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='santana',
            email='santana@gmail.com',
            password='elmickey123'
        )
        self.client.login(
            username='santana',
            password='elmickey123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_agregar_usuario(self):
        response = self.client.get('/usuario/agregar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_agregar_usuario(self):
        response = self.client.get(reverse('agregar_usuario'))
        self.assertEqual(response.status_code, 200)

    def test_template_agregar_usuario(self):
        response = self.client.get('/usuario/agregar')
        self.assertTemplateUsed(response, 'agregar_usuario.html')

    def test_prohibe_acceso_a_no_administradores(self):
        self.client.logout()
        self.user = User.objects.create_user(
            username='fatima',
            email='fatima@gmail.com',
            password='fatima123'
        )
        self.client.login(
            username='fatima',
            password='fatima123'
        )
        response = self.client.get('/usuario/agregar')
        self.assertTemplateNotUsed(response, 'lista_usuario.html')

    def test_muestra_todos_los_campos(self):
        response = self.client.get('/usuario/agregar')
        form = forms.UsuarioForm()
        for field in form:
            self.assertInHTML(str(field), response.content.decode("utf-8"))

    def test_agregar_usuario_lo_muestra_en_lista_usuario(self):
        credenciales = {
            'username': 'miguel',
            'email': 'mickey@hotmail.com',
            'password1': 'angel123',
            'password2': 'angel123',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(credenciales['username'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['email'],
                          response.content.decode("utf-8"))

    def test_muestra_error_cuando_contrasenas_no_coinciden(self):
        credenciales = {
            'username': 'miguel',
            'email': 'mickey@hotmail.com',
            'password1': 'angel1235',
            'password2': 'angel1234',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('Las contraseñas no coinciden',
                          response.content.decode("utf-8"))

    def test_muestra_error_con_longitud_de_contrasena(self):
        credenciales = {
            'username': 'miguel',
            'email': 'mickey@hotmail.com',
            'password1': 'angel',
            'password2': 'angel',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('La longitud minima es de 8',
                          response.content.decode("utf-8"))

        credenciales['password1'] = 'angelsantana1234567890'
        credenciales['password2'] = 'angelsantana1234567890'
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('La longitud maxima es de 16',
                          response.content.decode("utf-8"))

    def test_muestra_mensaje_error_con_campos_vacios(self):
        credenciales = {
            'username': '',
            'email': 'mickey@hotmail.com',
            'password1': 'angel',
            'password2': 'angel',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Usuario es obligatorio',
                          response.content.decode("utf-8"))

        credenciales['username'] = 'pablito'
        credenciales['email'] = ''
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Correo Electrónico es obligatorio',
                          response.content.decode("utf-8"))

        credenciales['email'] = 'pablo@gmail.com'
        credenciales['password1'] = ''
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Contraseña es obligatorio',
                          response.content.decode("utf-8"))

        credenciales['password1'] = 'pabloelhombre'
        credenciales['password2'] = ''
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'El campo Repita Contraseña es obligatorio', response.content.decode("utf-8"))

        credenciales['password2'] = 'pabloelhombre'
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(credenciales['username'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['email'],
                          response.content.decode("utf-8"))

    def test_agregar_usuario_con_username_repetido(self):
        credenciales = {
            'username': 'santana',
            'email': 'mickey@hotmail.com',
            'password1': 'angel123',
            'password2': 'angel123',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'Ya existe un usuario con ese nombre.', response.content.decode("utf-8"))


class TestViewEliminarUsuario(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='santana',
            email='santana@gmail.com',
            password='elmickey123'
        )
        self.client.login(
            username='santana',
            password='elmickey123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_eliminar_usuario(self):
        response = self.client.get('/usuario/eliminar/'+str(self.user.id))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_eliminar_usuario(self):
        response = self.client.get(
            reverse('eliminar_usuario', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_eliminar_usuario(self):
        response = self.client.get('/usuario/eliminar/'+str(self.user.id))
        self.assertTemplateUsed(response, 'confirm_delete_user.html')

    def test_muestra_username_de_quien_se_eliminara(self):
        usuario1 = User.objects.create_user(
            username='fatima',
            email='fatima@gmail.com',
            password='fatima123'
        )
        response = self.client.get('/usuario/eliminar/'+str(usuario1.id))
        self.assertInHTML(usuario1.username, response.content.decode("utf-8"))

    def test_usuario_eliminado_no_se_muestra_en_la_lista_usuario(self):
        usuario = User.objects.create_user(
            username='fatima',
            email='fatima@gmail.com',
            password='fatima123'
        )
        response = self.client.post(
            '/usuario/eliminar/'+str(usuario.id), follow=True)
        self.assertNotIn(response.content.decode("utf-8"), usuario.username)
        self.assertNotIn(response.content.decode("utf-8"), usuario.email)

    def test_muestra_advertencia_cuando_se_eliminara_el_usuario_logeado(self):
        response = self.client.get('/usuario/eliminar/'+str(self.user.id))
        self.assertInHTML(
            '¡CUIDADO! Estas por borrar tu propia cuenta',  response.content.decode("utf-8"))


class TestViewModificarUsuario(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='santana',
            email='santana@gmail.com',
            password='elmickey123'
        )
        self.client.login(
            username='santana',
            password='elmickey123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_modificar_usuario(self):
        response = self.client.get('/usuario/modificar/'+str(self.user.id))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_modificar_usuario(self):
        response = self.client.get(
            reverse('modificar_usuario', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_modificar_usuario(self):
        response = self.client.get('/usuario/modificar/'+str(self.user.id))
        self.assertTemplateUsed(response, 'modificar_usuario.html')

    def test_se_muestran_los_campos_del_form(self):
        response = self.client.get('/usuario/modificar/'+str(self.user.id))
        form = forms.ModificarUsuarioForm(instance=self.user)

        self.assertInHTML(str(form['username']),
                          response.content.decode("utf-8"))
        self.assertInHTML(str(form['email']), response.content.decode("utf-8"))
        self.assertInHTML(str(form['is_superuser']),
                          response.content.decode("utf-8"))

    def test_los_campos_son_llenados(self):
        response = self.client.get('/usuario/modificar/'+str(self.user.id))
        self.assertInHTML('<input type="text" name="username" value="'+self.user.username +
                          '" placeholder="Escribe el usuario" class="form-control form-control-sm" maxlength="50" minlength="5" required id="id_username">', response.content.decode("utf-8"))
        self.assertInHTML('<input type="email" name="email" value="'+self.user.email +
                          '" placeholder="Escribe el correo" class="form-control form-control-sm" required id="id_email">', response.content.decode("utf-8"))
        self.assertInHTML(
            '<input type="checkbox" name="is_superuser" class="form-check-input" id="id_is_superuser" checked>', response.content.decode("utf-8"))

    def test_modificaciones_se_ven_reflajadas_en_lista_usuario(self):
        credenciales = {
            'username': 'santanaplus',
            'email': 'elnuevocorreo@gmail.com',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/modificar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML(credenciales['username'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['email'],
                          response.content.decode("utf-8"))

    def test_se_muestra_error_si_los_campos_estan_vacios(self):
        credenciales = {
            'username': '',
            'email': 'elnuevocorreo@gmail.com',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/modificar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Usuario es obligatorio',
                          response.content.decode("utf-8"))

        credenciales = {
            'username': 'santana',
            'email': '',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/modificar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Correo Electrónico es obligatorio',
                          response.content.decode("utf-8"))

    def test_cambiar_username_a_un_username_existente(self):
        usuario = User.objects.create_superuser(
            username='shava',
            email='shava@gmail.com',
            password='loera123'
        )
        credenciales = {
            'username': 'santana',
            'email': 'shava@gmail.com',
            'is_superuser': 'True'
        }
        response = self.client.post(
            '/usuario/modificar/'+str(usuario.id),
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'Ya existe un usuario con ese nombre.', response.content.decode("utf-8"))


class TestViewCambiarContraseña(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='santana',
            email='santana@gmail.com',
            password='elmickey123'
        )
        self.client.login(
            username='santana',
            password='elmickey123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_cambiar_contrasena(self):
        response = self.client.get('/usuario/cambiar/'+str(self.user.id))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_cambiar_contrasena(self):
        response = self.client.get(
            reverse('cambiar_contrasena', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_cambiar_contrasena(self):
        response = self.client.get('/usuario/cambiar/'+str(self.user.id))
        self.assertTemplateUsed(response, 'cambiar_contrasena.html')

    def test_se_muestran_los_campos_del_form(self):
        form = forms.CambiarContrasenaForm(self.user)
        response = self.client.get('/usuario/cambiar/'+str(self.user.id))
        for field in form:
            self.assertInHTML(str(field), response.content.decode("utf-8"))

    def test_muestra_error_con_campos_vacios(self):
        credenciales = {
            'new_password1': '',
            'new_password2': '',
        }
        response = self.client.post(
            '/usuario/cambiar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Nueva Contraseña es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Repita Nueva Contraseña es obligatorio', response.content.decode("utf-8"))

        credenciales = {
            'new_password1': 'santana1234',
            'new_password2': '',
        }
        response = self.client.post(
            '/usuario/cambiar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'El campo Repita Nueva Contraseña es obligatorio', response.content.decode("utf-8"))

        credenciales = {
            'new_password1': '',
            'new_password2': 'santana1234',
        }
        response = self.client.post(
            '/usuario/cambiar/'+str(self.user.id),
            credenciales,
            follow=True
        )
        self.assertInHTML('El campo Nueva Contraseña es obligatorio',
                          response.content.decode("utf-8"))

    def test_cambiar_contrasena_se_ve_reflejado(self):
        credenciales = {
            'new_password1': 'miguelsantana',
            'new_password2': 'miguelsantana',
        }
        response = self.client.post(
            '/usuario/cambiar/'+str(self.user.id),
            credenciales
        )
        self.client.login(
            username='santana',
            password='miguelsantana'
        )
        self.assertTrue(self.user.is_authenticated)
