Característica: Registrar un nuevo usuario para la administracion de trabajadores
    Como administrador del sistema SCATUAZ,
    Quiero registrar un nuevo usuario al sistema
    Para que pueda consultar, agregar, eliminar, y modificar datos de un trabajador

    Escenario: Registrar a Miguel Angel Santana como nuevo usuario
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/agregar"
        Cuando ingreso los datos de "username": "elmickey", "password": "guzman123", "email": "elmickey@gmail.com"
        Y doy click en "Agregar"
        Entonces puedo ver "elmickey@gmail.com" en la lista de usuarios
    
    Escenario: Registrar a Miguel Angel Santana como nuevo administrador
        Dado que soy un administrador logeado
        Y que el usuario con correo "elmickey@gmail.com" no existe
        Y que ingreso a la vista de "usuario/agregar"
        Cuando ingreso los datos de "username": "elmickey", "password": "guzman123", "email": "elmickey@gmail.com"
        Y selecciono la casilla de administrador
        Y doy click en "Agregar"
        Entonces puedo ver "elmickey@gmail.com" en la lista de usuarios
        Y puedo ver que la casilla de "admin" esta checada