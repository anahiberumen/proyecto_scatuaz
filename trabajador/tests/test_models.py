from django.test import TestCase
from trabajador.models import Trabajador
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.test import TestCase


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='joan1',
            email='joan@gmail.com',
            password='joanteto123'
        )
        self.client.login(
            username='joan1',
            password='joanteto123'
        )

    def tearDown(self):
        self.client.logout()

    def test_return_object_trabajador(self):
        trabajador = Trabajador(
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
        trabajador.save()
        self.assertEqual(trabajador.nombre, trabajador.__str__())

    def test_max_length_en_nombre(self):

        trabajador = Trabajador(
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

        self.assertLess(len(trabajador.nombre), 50)

    def test_mas_de_la_max_length_en_nombre(self):

        trabajador = Trabajador(
            nombre='Salvadoooooooooooooooooooooooooooooooooooooooooooooooooooooooooor',
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

        self.assertGreater(len(trabajador.nombre), 50)

    def test_insercion_del_trabajador(self):
        trabajador = Trabajador(
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
        trabajador.save()

        self.assertEqual(Trabajador.objects.all()[0], trabajador)
