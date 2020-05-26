Característica: Cambiar contraseña de un usuario del sistema
    Como administrador del sistema SCATUAZ,
    Quiero cambiar la contraseña de los usuarios
    Por si se llegara a olvidar

    Escenario: Cambiar contraseña del usuario Miguel Angel Santana Guzman
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de editar del usuario "guzman@gmail.com"
        Cuando de click en el boton de cambiar contraseña
        Y edito los campos de "new_password1": "santaclaus", "new_password2": "santaclaus"
        Y doy click en el boton de Guardar
        Entonces puedo cerrar sesion
        Y logearme con la nueva contraseña "santaclaus" y usuario "miguelG"
        Y podre acceder a lista de trabajadores
    
    Escenario: Cambiar contraseña del usuario Miguel Angel Santana Guzman sin estar igual
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de editar del usuario "guzman@gmail.com"
        Cuando de click en el boton de cambiar contraseña
        Y edito los campos de "new_password1": "pongame7", "new_password2": "pongame10"
        Y doy click en el boton de Guardar
        Entonces vere un mensaje de error