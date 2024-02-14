from models.appium_class import NavigatorAppium
import time
import random

def register_producer(sesion: NavigatorAppium):


    fecha_location = '//android.view.View[@content-desc="1. Nombres (Obligatorio)\nIngrese los primeros nombres del productor\n2. Apellidos (Obligatorio)\nColoque el primer y segundo apellido del productor\n3. DNI (Obligatorio)\nIngrese su número DNI\n4. Celular principal (Obligatorio)\n 5. Fecha de nacimiento (Opcional)\n6. Operador (Opcional)\n7. Celular secundario (Opcional)\n8. Número de WhatsApp (Opcional)\n9. Tipo de celular (Botones, Táctil) (Opcional)\n10. Género (Opcional)\n11. Dirección del productor (Centro poblado, Comunidad, etc.) (Opcional)\n12. Departamento (Opcional)\n13. Provincia (Opcional)\n14. Distrito (Opcional)"]/android.view.View'

    widgets = '//android.widget.EditText | //android.widget.Button'

    # Darle click al boton registrar
    sesion.click_element("Registrar nuevo productor", "id")

    time.sleep(5)

    sesion.select_multiple_elements_by_XPATH(widgets)

    # Nombres
    sesion.type_from_multiple(1, "Prueba 2")

    # Apellidos
    sesion.type_from_multiple(2, "Prueba 2")

    # DNI

    DNI = random.randint(400,500)
    DNI = str(DNI).zfill(8)

    sesion.type_from_multiple(3, DNI)

    # Numero
    sesion.type_from_multiple(4, "911111111")

    # Fecha
    sesion.click_element(fecha_location, "xpath")
    sesion.click_element("12, lunes, 12 de febrero de 2024", "id")
    sesion.click_element("ACEPTAR", "id")

    #Operador
    sesion.click_from_multiple(5)
    sesion.click_element('Bitel', 'id')
    
    sesion.movement_in_view(45)

    # Celular y numero de whatsapp
    sesion.select_multiple_elements_by_XPATH(widgets)

    # Celular secundario
    sesion.type_from_multiple(1, "911111111")

    # Whatsapp
    sesion.type_from_multiple(2, "911111111")

    # Tipo de celular
    sesion.click_from_multiple(3)
    sesion.click_element("Botones", "id")

    # Genero
    sesion.click_from_multiple(4)
    sesion.click_element("Masculino", "id")

    # Direccion
    sesion.type_from_multiple(5, "Direccion generica")

    # Departamento
    sesion.click_from_multiple(6)
    sesion.click_element("Amazonas", "id")

    sesion.movement_in_view(45)

    sesion.select_multiple_elements_by_XPATH(widgets)

    # Provincia
    sesion.click_from_multiple(1)
    sesion.click_element("Bongará", "id")

    # Distrito
    sesion.click_from_multiple(2)
    sesion.click_element("Churuja", "id")

    # Estado civil
    sesion.click_from_multiple(3)
    sesion.click_element("Opcion 2 Divorciado", "id")

    # Nombre pareja
    sesion.type_from_multiple(4, "Pareja")

    # Numero hijos
    sesion.type_from_multiple(5, '20')

    # Pregunta multiple
    sesion.click_from_multiple(6)
    sesion.click_element("Opcion EDITADA 3", "id")

    #Siguiente
    sesion.click_element("Siguiente", 'id')

    #Aceptar
    sesion.click_element("ACEPTAR", 'id')