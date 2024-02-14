from models.appium_class import NavigatorAppium
import time
import random

def generate_transaction(session:NavigatorAppium):

    # GENERAR TRANSACCION

    # Sí, generar nueva transacción
    # No, volver al inicio

    # session.click_element("Sí, generar nueva transacción", "id")

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    #DNI
    session.type_from_multiple(0, '73172642')

    #Nombres
    session.click_from_multiple(1)

    session.type_from_multiple(1, 'Dario Jesus')

    #Apellidos
    session.type_from_multiple(2, 'Falcon Atarama')

    #Numero telefonico
    session.type_from_multiple(3, 968532084)

    #Boton siguiente
    session.click_element("Siguiente", 'id')

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    #Cantidad
    session.type_from_multiple(0, str(random.randint(100,2000)))

    #Precio unitario
    session.type_from_multiple(1, str(random.randint(1,20)))

    #Click siguiente
    session.click_element("Siguiente", "id")