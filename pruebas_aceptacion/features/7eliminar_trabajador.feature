Característica: Eliminar un trabajador
    Como usuario del sistema SCATUAZ, eliminar un trabajador que haya sido dado de alta por accidente.

    Escenario: Seleccionar un trabajador y eliminarlo
        Dado que soy un usuario logeado
        Y que ingreso a la vista de "trabajador/"
        Cuando encuentre el trabajador con rfc "VECJ8803262XX"
        Y de click en el boton de eliminar
        Y confirme la eliminacion
        Entonces Ya no vere el trabajador con rfc "VECJ8803262XX"