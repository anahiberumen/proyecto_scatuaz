Característica: Actualizar los datos de los trabajadores
    Como usuario del sistema SCATUAZ,
    Quiero modificar los datos de los trabajadores
    Para mantener sus datos actualizados

    Escenario: Modificar la direccion del trabajador BEGSHJSS56568
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/"
        Y doy click en el boton de editar del trabajador con rfc "BEGSHJSS56568"
        Cuando escribo los datos "pais_residencia": "Rusia", "estado_residencia": "Priviat", "cp": "33342"
        Y los datos "municipio_residencia": "Chernovyl", "calle": "Drafkasrt", "numero": "222", "colonia": "Perltov",
        Y de clic en el botón de guardar
        Entonces podre ir a ver detalles del trabajador
        Y observar los cambios hechos "pais_residencia": "Rusia", "estado_residencia": "Priviat", "cp": "33342"
        Y los nuevo datos "municipio_residencia": "Chernovyl", "calle": "Drafkasrt", "numero": "222", "colonia": "Perltov",