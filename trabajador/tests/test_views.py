from django.test import TestCase
from django.urls import reverse
from trabajador import forms
from trabajador.models import Trabajador
from django.contrib.auth.models import User


class TestViewBuscador(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='anahi',
            email='annie@gmail.com',
            password='berumen123'
        )
        self.client.login(
            username='anahi',
            password='berumen123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_lista_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_lista_trabajadores(self):
        response = self.client.get(reverse('lista_trabajador'))
        self.assertEqual(response.status_code, 200)

    def test_template_lista_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertTemplateUsed(response, 'lista_trabajador.html')

    def test_campo_buscador_existe_en_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertInHTML(
            '<input class="form-control mr-sm-2" type="text" placeholder="Buscar Trabajador" aria-label="Search" name="buscador" id="buscador" required="true">', response.content.decode("utf-8"))

    def test_resultado_busqueda_existente(self):
        trabajador1 = Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='LOQSY32231',
            curp='LOQS960920HNLRRL09'
        )

        response = self.client.get('/trabajador/buscar?buscador=Salvador')
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Salvador</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Loera</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Quiroz</a></td>', response.content.decode("utf-8"))
        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Salvador</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Loera</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Quiroz</a></td>', response.content.decode("utf-8"))
        response = self.client.get('/trabajador/buscar?buscador=Quiroz')
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Salvador</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Loera</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Quiroz</a></td>', response.content.decode("utf-8"))

    def test_no_hay_resultados(self):
        response = self.client.get(
            '/trabajador/buscar?buscador=Elseñornoexiste')
        self.assertInHTML('<h4>No hay resultados</h4>',
                          response.content.decode("utf-8"))

    def test_busqueda_vacia_regresa_cero_resultados(self):
        self.agregar_trabajador2

        response = self.client.get('/trabajador/buscar?buscador=')
        self.assertInHTML('<h4>No hay resultados</h4>',
                          response.content.decode("utf-8"))

    def test_varios_resultados(self):
        trabajador1 = self.agregar_trabajador1()
        trabajador2 = self.agregar_trabajador2()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Salvador</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Loera</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador1.id)+'">Quiroz</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador2.id)+'">Fatima Anahi</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador2.id)+'">Loera</a></td>', response.content.decode("utf-8"))
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador2.id)+'">Murillo</a></td>', response.content.decode("utf-8"))

    def test_muestra_rfc_en_resultados(self):
        trabajador = self.agregar_trabajador1()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td><a class="text-white" href="/trabajador/'+str(
            trabajador.id)+'">LOQSY32231</a></td>', response.content.decode("utf-8"))

    def test_muestra_cantidad_de_resultados(self):
        self.agregar_trabajador1()
        self.agregar_trabajador2()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<h4>2 resultados.</h4>',
                          response.content.decode("utf-8"))

    def agregar_trabajador1(self):
        return Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='LOQSY32231',
            curp='LOQS960920HNLRRL09',
            sexo='M',
            pais_residencia='Mexico',
            estado_residencia='Zacatecas',
            municipio_residencia='Zacatecas',
            calle='Morelos',
            numero='282',
            colonia='Centro',
            cp='28812',
            matricula_administrativo='271382',
            matricula_gremial='322188',
            grado_max_estudios='Doctorado',
            nss='12673126127',
            no_issste='87878789892',
            validado_renapo='True',
            validado_siri='False',
        )

    def agregar_trabajador2(self):
        return Trabajador.objects.create(
            nombre='Fatima Anahi',
            paterno='Loera',
            materno='Murillo',
            rfc='BMFA27182DS',
            curp='BMFA21873HJDSA98SS',
            sexo='F',
            pais_residencia='Mexico',
            estado_residencia='Zacatecas',
            municipio_residencia='Zacatecas',
            calle='Morelos',
            numero='282',
            colonia='Centro',
            cp='28812',
            matricula_administrativo='271311',
            matricula_gremial='322324',
            grado_max_estudios='Doctorado',
            nss='12673126122',
            no_issste='21321333322',
            validado_renapo='True',
            validado_siri='False',
        )


class TestViewAgregar(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='anahi',
            email='annie@gmail.com',
            password='berumen123'
        )
        self.client.login(
            username='anahi',
            password='berumen123'
        )

    def tearDown(self):
        self.client.logout()

    def test_url_agregar_trabajador(self):
        response = self.client.get('/trabajador/agregar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_agregar_trabajador(self):
        response = self.client.get(reverse('agregar_trabajador'))
        self.assertEqual(response.status_code, 200)

    def test_template_agregar_trabajador(self):
        response = self.client.get('/trabajador/agregar')
        self.assertTemplateUsed(response, 'agregar_trabajador.html')

    def test_prohibe_acceso_a_personal_no_autorizado(self):
        self.client.logout()

        response = self.client.get('/trabajador/agregar')
        self.assertTemplateNotUsed(response, 'agregar_trabajador.html')

    def test_muestra_todos_los_campos(self):
        response = self.client.get('/trabajador/agregar')
        form = forms.TrabajadorForm()
        for field in form:
            self.assertInHTML(str(field), response.content.decode("utf-8"))

    def test_agregar_trabajador_lo_muestra_en_lista_trabajador(self):
        credenciales = {
            'nombre': 'Shavota',
            'paterno': 'Loes',
            'materno': 'Arroz',
            'rfc': 'KDSJAF1909922',
            'curp': 'DHJFAKH898897D0921',
            'sexo': 'M',
            'pais_residencia': 'Mexico',
            'estado_residencia': 'Zacatecas',
            'municipio_residencia': 'Zacatecas',
            'calle': 'Morelos',
            'numero': '282',
            'colonia': 'Centro',
            'cp': '28812',
            'matricula_administrativo': '786899',
            'matricula_gremial': '992902',
            'grado_max_estudios': 'Doctorado',
            'nss': '12673126223',
            'no_issste': '212333322',
            'validado_renapo': 'True',
            'validado_siri': 'False',
        }
        response = self.client.post(
            '/trabajador/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(credenciales['nombre'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['paterno'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['materno'],
                          response.content.decode("utf-8"))
        self.assertInHTML(credenciales['rfc'],
                          response.content.decode("utf-8"))

    def test_muestra_error_cuando_campos_obligatorios_estan_vacios(self):
        credenciales = {
            'nombre': '',
            'paterno': '',
            'materno': '',
            'rfc': '',
            'curp': '',
            'sexo': '',
            'pais_residencia': '',
            'estado_residencia': '',
            'municipio_residencia': '',
            'calle': '',
            'numero': '',
            'colonia': '',
            'cp': '',
            'matricula_administrativo': '',
            'matricula_gremial': '',
            'grado_max_estudios': '',
            'nss': '',
            'no_issste': '',
            'validado_renapo': '',
            'validado_siri': '',
        }
        response = self.client.post(
            '/trabajador/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'El campo Grado Max de Estudios es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Matricula Gremial es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Matricula de Administrativo es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML('El campo CP es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Colonia de Residencia es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML('El campo Numero es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Calle de Residencia es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Municipio de Residencia es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo Estado de Residencia es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML(
            'El campo País de Residencia es obligatorio', response.content.decode("utf-8"))
        self.assertInHTML('El campo CURP es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML('El campo RFC es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML('El campo Nombre es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML('El campo Apellido Materno es obligatorio',
                          response.content.decode("utf-8"))
        self.assertInHTML('El campo Apellido Paterno es obligatorio',
                          response.content.decode("utf-8"))

    def test_agregar_trabajador_con_campos_unicos_repetidos(self):
        self.agregar_trabajador1()
        credenciales = {
            'nombre': 'Shavota',
            'paterno': 'Loes',
            'materno': 'Arroz',
            'rfc': 'KDSJAF1909922',
            'curp': 'LOQS960920HNLRRL09',
            'sexo': 'M',
            'pais_residencia': 'Mexico',
            'estado_residencia': 'Zacatecas',
            'municipio_residencia': 'Zacatecas',
            'calle': 'Morelos',
            'numero': '282',
            'colonia': 'Centro',
            'cp': '28812',
            'matricula_administrativo': '271382',
            'matricula_gremial': '322188',
            'grado_max_estudios': 'Doctorado',
            'nss': '12673126223',
            'no_issste': '212333322',
            'validado_renapo': 'True',
            'validado_siri': 'False',
        }
        response = self.client.post(
            '/trabajador/agregar',
            credenciales,
            follow=True
        )
        self.assertInHTML(
            'Ya existe un/a Trabajador con este/a Matricula gremial.', response.content.decode("utf-8"))
        self.assertInHTML(
            'Ya existe un/a Trabajador con este/a Matricula administrativo.', response.content.decode("utf-8"))
        self.assertInHTML(
            'Ya existe un/a Trabajador con este/a Curp.', response.content.decode("utf-8"))
        self.assertInHTML('Ya existe un/a Trabajador con este/a Rfc.',
                          response.content.decode("utf-8"))

    def agregar_trabajador1(self):
        return Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='KDSJAF1909922',
            curp='LOQS960920HNLRRL09',
            sexo='M',
            pais_residencia='Mexico',
            estado_residencia='Zacatecas',
            municipio_residencia='Zacatecas',
            calle='Morelos',
            numero='282',
            colonia='Centro',
            cp='28812',
            matricula_administrativo='271382',
            matricula_gremial='322188',
            grado_max_estudios='Doctorado',
            nss='12673126127',
            no_issste='87878789892',
            validado_renapo='True',
            validado_siri='False',
        )


class TestViewVer(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='anahi',
            email='annie@gmail.com',
            password='berumen123'
        )
        self.client.login(
            username='anahi',
            password='berumen123'
        )
        self.trabajador = self.agregar_trabajador1()

    def tearDown(self):
        self.client.logout()

    def test_url_agregar_trabajador(self):
        response = self.client.get('/trabajador/'+str(self.trabajador.id))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_agregar_trabajador(self):
        response = self.client.get(
            reverse('ver_trabajador', args=[self.trabajador.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_agregar_trabajador(self):
        response = self.client.get('/trabajador/'+str(self.trabajador.id))
        self.assertTemplateUsed(response, 'ver_trabajador.html')

    def test_muestra_historial_de_actualizaciones(self):
        datos = {
            'nombre': 'Salvador',
            'paterno': 'Loera',
            'materno': 'Quiroz',
            'rfc': 'KDSJAF1909922',
            'curp': 'LOQS960920HNLRRL09',
            'sexo': 'M',
            'pais_residencia': 'Mexico',
            'estado_residencia': 'Zacatecas',
            'municipio_residencia': 'Zacatecas',
            'calle': 'Morelos',
            'numero': '282',
            'colonia': 'Centro',
            'cp': '28812',
            'matricula_administrativo': '271382',
            'matricula_gremial': '322188',
            'grado_max_estudios': 'Doctorado',
            'nss': '12673126127',
            'no_issste': '87878789892',
            'validado_renapo': 'True',
            'validado_siri': 'False',
            'alta_usuario': self.user.id,
        }
        self.client.post('/trabajador/modificar/' +
                         str(self.trabajador.id), datos)
        response = self.client.get('/trabajador/'+str(self.trabajador.id))
        self.assertInHTML('Historial del Registro',
                          response.content.decode('utf-8'))

    def test_no_hay_historial_de_actualizaciones(self):
        response = self.client.get('/trabajador/'+str(self.trabajador.id))
        self.assertInHTML(
            '<h4>No hay historial de actualizaciones disponible</h4>', response.content.decode('utf-8'))

    def agregar_trabajador1(self):
        return Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='KDSJAF1909922',
            curp='LOQS960920HNLRRL09',
            sexo='M',
            pais_residencia='Mexico',
            estado_residencia='Zacatecas',
            municipio_residencia='Zacatecas',
            calle='Morelos',
            numero='282',
            colonia='Centro',
            cp='28812',
            matricula_administrativo='271382',
            matricula_gremial='322188',
            grado_max_estudios='Doctorado',
            nss='12673126127',
            no_issste='87878789892',
            validado_renapo='True',
            validado_siri='False',
            alta_usuario=self.user.id,
        )


class TestViewModificar(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='anahi',
            email='annie@gmail.com',
            password='berumen123'
        )
        self.client.login(
            username='anahi',
            password='berumen123'
        )
        self.trabajador = self.agregar_trabajador1()

    def tearDown(self):
        self.client.logout()

    def test_url_modificar_trabajador(self):
        response = self.client.get(
            '/trabajador/modificar/'+str(self.trabajador.id))
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_modificar_trabajador(self):
        response = self.client.get(
            reverse('modificar_trabajador', args=[self.trabajador.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_modificar_trabajador(self):
        response = self.client.get(
            '/trabajador/modificar/'+str(self.trabajador.id))
        self.assertTemplateUsed(response, 'modificar_trabajador.html')

    def agregar_trabajador1(self):
        return Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='KDSJAF1909922',
            curp='LOQS960920HNLRRL09',
            sexo='M',
            pais_residencia='Mexico',
            estado_residencia='Zacatecas',
            municipio_residencia='Zacatecas',
            calle='Morelos',
            numero='282',
            colonia='Centro',
            cp='28812',
            matricula_administrativo='271382',
            matricula_gremial='322188',
            grado_max_estudios='Doctorado',
            nss='12673126127',
            no_issste='87878789892',
            validado_renapo='True',
            validado_siri='False',
            alta_usuario=self.user.id,
        )
