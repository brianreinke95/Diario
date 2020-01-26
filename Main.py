from Switches import switch_principal
from clear import clear
from menues import menu
from Comprobacion_Seleccion import Comprobacion_seleccion

# El programa debe ir almacenando las actividades que realizo en el día.

# El día se compone desde el momento en que me despierto hasta el momento en que me voy a dormir. Es decir
# que un día puede estar compuesto por horas de distintas fechas.

# El programa debe tener una interfase donde primero uno carga el día de inicio registrando los límites de horarios.
# Es decir que si empiezo el jueves 21 a las 10 am pero me acuesto el viernes 22 a la 1 am se registra en el mismo dia




if '__main__':

    while True:
        clear()
        seleccion = menu()
        clear()
        if Comprobacion_seleccion([0, 1, 2, 3, 4], seleccion):
            if seleccion == 0:
                break
            else:
                switch_principal(seleccion)
