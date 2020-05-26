from django.test import TestCase
from trabajador.models import Trabajador
from trabajador.forms import TrabajadorForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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

    def test_si_el_formulario_es_valido(self):
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
        trabajador_uno = Trabajador.objects.first()
        self.assertEqual(trabajador, trabajador_uno)

    def test_si_el_formulario_es_invalido_sin_nombre(self):

        data = {
            'nombre': '',
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

        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_invalido_mas_de_50_caracteres_en_nombre(self):

        data = {
            'nombre': 'Salvadoooooooooooooooooooooooooooooooooooooooooooooor',
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

        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())

    def test_si_el_formulario_es_invalido_mas_de_13_caracteres_en_rfc(self):

        data = {
            'nombre': 'Salvadoooooooooooooooooooooooooooooooooooooooooooooor',
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

        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())
