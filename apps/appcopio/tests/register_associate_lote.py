from models.appium_class import NavigatorAppium
import time
import random


def register_associate_lote(session: NavigatorAppium):

    lote_button_location = [270, 2880]

    # Boton de lotes
    session.click_by_coordinates(lote_button_location[0], lote_button_location[1])

    # Boton registrar lote
    session.click_element("Registrar Nuevo Lote", "id")

    time.sleep(1)

    # Boton de lote asociado
    session.click_element(
        '//android.widget.Button[@content-desc="Registrar Nuevo Lote"]', "xpath"
    )

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")
    # fecha

    # date_lote = f"{random.randint(1,25)}{random.randint(1,19)}20{random.randint(0,10)}"

    # session.type_from_multiple(0, date_lote)

    # Procedencia
    session.type_from_multiple(1, "Piura")

    # Click siguiente
    session.click_element("Siguiente", "id")

    # Certificacion
    session.click_element("Certificación*", "id")

    certification_options = ["FLO", "UTZ", "NOP", "UE", "GGN"]

    session.click_element(random.choice(certification_options), "id")

    # Click siguiente
    session.click_element("Siguiente", "id")

    # Numero de lote
    session.type_element(
        f"{random.randint(5000,9000)}", "//android.widget.EditText", "xpath"
    )

    # Estado de lote

    session.click_element("Estado del Lote", "id")

    lote_status = [
        "vacio",
        "completado",
        "baba",
        "cajon",
        "sabana",
        "ensacado",
        "transporte",
    ]

    session.click_element(random.choice(lote_status), "id")

    # Editar nombre de lote

    pencil_edit_location = [1300, 1600]

    session.click_by_coordinates(pencil_edit_location[0], pencil_edit_location[1])

    session.type_element("hola", "//android.widget.EditText[2]", "xpath")

    # Click siguiente
    session.click_element("Siguiente", "id")

    #Volver al inicio
    session.click_element("No, volver al inicio", "id")

    # # GENERAR TRANSACCION

    # # Sí, generar nueva transacción
    # # No, volver al inicio

    # session.click_element("Sí, generar nueva transacción", "id")

    # session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # #DNI
    # session.type_from_multiple(0, '73172642')

    # #Nombres
    # session.click_from_multiple(1)

    # session.type_from_multiple(1, 'Dario Jesus')

    # #Apellidos
    # session.type_from_multiple(2, 'Falcon Atarama')

    # #Numero telefonico
    # session.type_from_multiple(3, 968532084)

    # #Boton siguiente
    # session.click_element("Siguiente", 'id')

    # session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # #Cantidad
    # session.type_from_multiple(0, str(random.randint(100,2000)))

    # #Precio unitario
    # session.click_from_multiple(1, str(random.randint(1,20)))

    # #Click siguiente
    # session.click_element("Siguiente", "id")

def register_not_associate_lote(session: NavigatorAppium):

    lote_button_location = [270, 2880]

    # Boton de lotes
    session.click_by_coordinates(lote_button_location[0], lote_button_location[1])

    # Boton registrar lote
    session.click_element("Registrar Nuevo Lote", "id")

    time.sleep(1)

    # Boton de lote no asociado
    session.click_element("Registrar Lote no asociado", 'id')

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")
    # fecha

    # date_lote = f"{random.randint(1,25)}{random.randint(1,19)}20{random.randint(0,10)}"

    # session.type_from_multiple(0, date_lote)

    # Procedencia
    session.type_from_multiple(1, "Piura")

    # Click siguiente
    session.click_element("Siguiente", "id")

    # Certificacion
    session.click_element("Certificación*", "id")

    certification_options = ["FLO", "UTZ", "NOP", "UE", "GGN"]

    session.click_element(random.choice(certification_options), "id")

    # Click siguiente
    session.click_element("Siguiente", "id")

    # Numero de lote
    session.type_element(
        f"{random.randint(5000,9000)}", "//android.widget.EditText", "xpath"
    )

    # Estado de lote

    session.click_element("Estado del Lote", "id")

    lote_status = [
        "vacio",
        "completado",
        "baba",
        "cajon",
        "sabana",
        "ensacado",
        "transporte",
    ]

    session.click_element(random.choice(lote_status), "id")

    # Editar nombre de lote

    pencil_edit_location = [1300, 1600]

    session.click_by_coordinates(pencil_edit_location[0], pencil_edit_location[1])

    session.type_element("hola", "//android.widget.EditText[2]", "xpath")

    # Click siguiente
    session.click_element("Siguiente", "id")

    #Volver al inicio
    # session.click_element("No, volver al inicio", "id")

    # #Generar nueva transaccion
    # session.click_element("Sí, generar nueva transacción", "id")


    # GENERAR TRANSACCION

    # Sí, generar nueva transacción
    # No, volver al inicio

    # session.click_element("Sí, generar nueva transacción", "id")

    # session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # #DNI
    # session.type_from_multiple(0, '73172642')

    # #Nombres
    # session.click_from_multiple(1)

    # session.type_from_multiple(1, 'Dario Jesus')

    # #Apellidos
    # session.type_from_multiple(2, 'Falcon Atarama')

    # #Numero telefonico
    # session.type_from_multiple(3, 968532084)

    # #Boton siguiente
    # session.click_element("Siguiente", 'id')

    # session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # #Cantidad
    # session.type_from_multiple(0, str(random.randint(100,2000)))

    # #Precio unitario
    # session.type_from_multiple(1, str(random.randint(1,20)))

    # #Click siguiente
    # session.click_element("Siguiente", "id")