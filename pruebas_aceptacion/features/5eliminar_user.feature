Característica: Eliminar un usuario del sistema para negar su acceso
    Como administrador del sistema SCATUAZ,
    Quiero eliminar un usuario existente del sistema
    Para negar su acceso al sistema

    Escenario: Eliminar al usuario Miguel Angel Santana Guzman
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de eliminar del usuario "guzman@gmail.com"
        Cuando me encuentre en la vista de confirmar eliminacion
        Y doy click en "Eliminar"
        Entonces ya no vere "guzman@gmail.com" en la lista de usuarios
    
    Escenario: Eliminar al usuario Tigre
        Dado que soy un administrador logeado
        Y que ingreso a la vista de "usuario/"
        Y doy click en el boton de eliminar del usuario "tigre@gmail.com"
        Cuando me encuentre en la vista de confirmar eliminacion
        Entonces puedo ver la advertencia "¡CUIDADO! Estas por borrar tu propia cuenta" 