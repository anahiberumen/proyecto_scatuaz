from django.db import models
from django.core.validators import MinLengthValidator


OPCIONES_SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

OPCIONES_ESTUDIOS = (
    ('Primaria', 'Primaria'),
    ('Secundaria', 'Secundaria'),
    ('Bachillerato o Preparatoria', 'Bachillerato o Preparatoria'),
    ('Carrera Comercial', 'Carrera Comercial'),
    ('Carrera Técnica', 'Carrera Técnica'),
    ('Normal', 'Normal'),
    ('Normal Superior', 'Normal Superior'),
    ('Licenciatura', 'Licenciatura'),
    ('Pasante de Carrera Profesional', 'Pasante de Carrera Profesional'),
    ('Especialidad', 'Especialidad'),
    ('Maestría', 'Maestría'),
    ('Doctorado', 'Doctorado'),
    ('Pasante de Maestría', 'Pasante de Maestría'),
    ('Candidato a Doctor', 'Candidato a Doctor'),
    ('Postdoctorado', 'Postdoctorado'),
)
# Create your models here.


class Trabajador(models.Model):

    # DATOS PERSONALES
    nombre = models.CharField(
        max_length=100
    )
    paterno = models.CharField(
        max_length=100
    )
    materno = models.CharField(
        max_length=100
    )
    rfc = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            MinLengthValidator(
                13, 'Debe tener longitud de 13 caracteres'
            )
        ]
    )
    curp = models.CharField(
        max_length=18,
        unique=True)
    sexo = models.CharField(
        max_length=1,
        choices=OPCIONES_SEXO,
    )
    pais_residencia = models.CharField(
        max_length=100,
    )
    estado_residencia = models.CharField(
        max_length=100,
    )
    municipio_residencia = models.CharField(
        max_length=100,
    )
    calle = models.CharField(
        max_length=100,
    )
    numero = models.CharField(
        max_length=10,
    )
    colonia = models.CharField(
        max_length=100,
    )
    cp = models.CharField(
        max_length=6,
    )
    telefono = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=50,
    )
    # DATOS LABORALES
    matricula_administrativo = models.CharField(
        max_length=6,
        unique=True
    )
    matricula_gremial = models.CharField(
        max_length=6,
        unique=True
    )
    # DATOS ACADEMICOS
    grado_max_estudios = models.CharField(
        max_length=60,
        choices=OPCIONES_ESTUDIOS
    )
    # DATOS ISSSTE
    nss = models.CharField(
        max_length=11
    )
    no_issste = models.CharField(
        max_length=50
    )
    validado_renapo = models.BooleanField(
        null=True
    )
    validado_siri = models.BooleanField(
        null=True
    )
    # DATOS DE ALTA
    alta_usuario = models.CharField(
        max_length=150
    )
    alta_fecha = models.DateField(
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre


class Actualizacion(models.Model):

    id_trabajador = models.ForeignKey(
        'Trabajador',
        on_delete=models.CASCADE,
    )
    usuario = models.CharField(
        max_length=150
    )
    fecha = models.DateField(
        auto_now=False,
        auto_now_add=True
    )
