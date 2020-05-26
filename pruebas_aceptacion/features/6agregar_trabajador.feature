Característica: Creación de un trabajador
    Como usuario del sistema SCATUAZ, quiero crear(dar de alta) un trabajador.

    Escenario: Crear un trabajador con campos obligatorios completos
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/agregar"
        Cuando escribo los datos "sexo": "M", "paterno": "Loera", "materno": "Quiroz",
        Y "rfc": "VECJ8803262XX", "curp": "BEMF980417MZSRRT06", "nombre": "Salvador", "pais_residencia": "México",
        Y "estado_residencia": "Zacatecas", "municipio_residencia": "Zacatecas", "calle": "Morelos", "numero": "123",
        Y "colonia": "Centro", "cp": "37122", "telefono": "4921234442", "email": "loera.q@gmail.com",
        Y "matricula_administrativo": "666643", "matricula_gremial": "123123", "grado_max_estudios": "Especialidad", "nss": "237189",
        Y "no_issste": "372812", "validado_renapo": "1", "validado_siri": "0"
        Cuando de clic en el botón crear "Agregar"
        Entonces podré ver el trabajador con RFC "VECJ8803262XX" en la lista de trabajador

    Escenario: Crear un trabajador con campos pasando la longitud maxima
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/agregar"
        Cuando escribo los datos "sexo": "F", "paterno": "Berumen", "materno": "Murillo",
        Y "rfc": "BEGSHJSS5656856568545", "curp": "BHJDHSBHKSGAHKDG67483267482", "nombre": "Fatima", "pais_residencia": "México",
        Y "estado_residencia": "Zacatecas", "municipio_residencia": "Zacatecas", "calle": "Morelos", "numero": "123",
        Y "colonia": "Centro", "cp": "37122", "telefono": "432432222222", "email": "anahi.b@gmail.com",
        Y "matricula_administrativo": "6546436", "matricula_gremial": "43243232", "grado_max_estudios": "Especialidad", "nss": "2371894375678342685",
        Y "no_issste": "372812", "validado_renapo": "1", "validado_siri": "0"
        Cuando de clic en el botón crear "Agregar"
        Entonces podré ver el trabajador con RFC "BEGSHJSS56568" en la lista de trabajador

    Escenario: Crear un trabajador con campos sin cumplir la longitud minima
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/agregar"
        Cuando escribo los datos "sexo": "M", "paterno": "Santana", "materno": "Guzman",
        Y "rfc": "HGD33", "curp": "VHXG222", "nombre": "Miguel Angel", "pais_residencia": "México",
        Y "estado_residencia": "Zacatecas", "municipio_residencia": "Zacatecas", "calle": "Morelos", "numero": "123",
        Y "colonia": "Centro", "cp": "37122", "telefono": "5676567", "email": "santana@gmail.com",
        Y "matricula_administrativo": "2223", "matricula_gremial": "8786", "grado_max_estudios": "Especialidad", "nss": "3213",
        Y "no_issste": "372812", "validado_renapo": "1", "validado_siri": "1"
        Cuando de clic en el botón crear "Agregar"
        Entonces seguire en la misma vista

    Escenario: Crear un trabajador con campos unicos duplicados
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/agregar"
        Cuando escribo los datos "sexo": "M", "paterno": "Varela", "materno": "Sosa",
        Y "rfc": "VECJ8803262XX", "curp": "BEMF980417MZSRRT06", "nombre": "Francisco Javier", "pais_residencia": "México",
        Y "estado_residencia": "Zacatecas", "municipio_residencia": "Zacatecas", "calle": "Morelos", "numero": "123",
        Y "colonia": "Centro", "cp": "37122", "telefono": "5676567", "email": "santana@gmail.com",
        Y "matricula_administrativo": "666643", "matricula_gremial": "123123", "grado_max_estudios": "Especialidad", "nss": "342345",
        Y "no_issste": "372812", "validado_renapo": "1", "validado_siri": "1"
        Cuando de clic en el botón crear "Agregar"
        Entonces seguire en la misma vista
        Y podre ver el mensaje de error "Trabajador with this Rfc already exists.", "Trabajador with this Curp already exists.", "Trabajador with this Matricula administrativo already exists.", "Trabajador with this Matricula gremial already exists."