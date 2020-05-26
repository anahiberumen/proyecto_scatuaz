Característica: Inicio de sesión de un usuario
    Como usuario del sistema SCATUAZ, 
    Quiero iniciar sesion haciendo uso de mis credenciales
    Para acceder a las funciones del sistema

    Escenario: Iniciar sesion con usuario tigre y con contraseña tigre123
        Dado que ingreso a la vista de " "
        Y ingreso el usuario "tigre" con la contraseña "tigre123"
        Cuando se realiza un inicio de sesion
        Entonces puedo ver un mensaje de "Lista de Trabajadores"
    
    Escenario: Iniciar sesion erroneamente con usuario tigre y con contraseña ti542234
        Dado que ingreso a la vista de " "
        Y ingreso el usuario "tigre" con la contraseña "ti542234"
        Cuando se realiza un inicio de sesion
        Entonces puedo ver un mensaje de error "Credenciales invalidas"
    
    Escenario: Iniciar sesion sin usuario y contraseña 
        Dado que ingreso a la vista de " "
        Y no ingreso usuario ni contraseña
        Cuando se realiza un inicio de sesion
        Entonces me mantengo en la misma vista
