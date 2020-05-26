Característica: Modificar datos de un usuario del sistema
    Como administrador del sistema SCATUAZ,
    Quiero modificar los datos existentes de un usuario
    Para mantener su informacion actualizada

    Escenario: Modificar al usuario Miguel Angel Santana Guzman
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de editar del usuario "elmickey@gmail.com"
        Cuando me encuentre en la vista de modificar usuario
        Y edito los campos de "username": "miguelG", "email": "guzman@gmail.com"
        Y doy click en el boton de Guardar
        Entonces vere "guzman@gmail.com" y "miguelG" en la lista de usuarios
    
    Escenario: Modificar al usuario Miguel Angel Santana Guzman con datos invalidados
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de editar del usuario "guzman@gmail.com"
        Cuando me encuentre en la vista de modificar usuario
        Y edito los campos de "username": "angel", "email": "guzmangmail.com"
        Y doy click en el boton de Guardar
        Entonces me mantendre en la vista de modificar usuario