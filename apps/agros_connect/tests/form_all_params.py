from models.appium_class import NavigatorAppium
import time
import uuid
import random

def fill_text_form(sesion: NavigatorAppium, offline: bool):

    #     NUM -> TEXT -> android.widget.EditText
    sesion.click_by_coordinates(674, 1100)

    # Ficha de productor
    sesion.click_element("Recolección de datos", "id")

    # Fomularios
    sesion.select_multiple_elements_by_XPATH("//android.widget.Button")
    sesion.click_from_multiple(1)

    time.sleep(5)

    #Buscador de fotos
    sesion.select_multiple_elements_by_XPATH("//android.widget.EditText")
    sesion.type_from_multiple(0, "TEST TEXT FIELDS")

    #Seleccionar el formulario
    sesion.click_element("TEST TEXT FIELDS", "ui-desc")

    time.sleep(2)

    for e in range(1, 6):

        sesion.type_element(str(uuid.uuid4()),f'{e}. TEST {e}', 'ui-text')

    sesion.type_element(random.randint(5, 100), f'8. TEST 8', 'ui-text')

    sesion.type_element(random.randint(5, 100), f'6. TEST 6', 'ui-text')
    sesion.type_element(random.randint(5, 100), f'7. TEST 7', 'ui-text')
    sesion.type_element(random.randint(5, 100), f'9. TEST 9', 'ui-text')
    sesion.type_element(random.randint(5, 100), f'10. TEST 10', 'ui-text')


    sesion.click_element("Guardar", "ui-desc")

    
    # Pemiso almacenamiento
    sesion.click_element("Allow all", "ui-text")
    time.sleep(2)
    #Permiso musica
    sesion.click_by_coordinates(704, 1653)



    #Guardar
    sesion.click_element("Guardar", "ui-desc")
    sesion.click_element("ACEPTAR", "id")

    for i in range(0,10):

        time.sleep(2)

        #Seleccionar el formulario
        sesion.click_element("TEST TEXT FIELDS", "ui-desc")

        time.sleep(2)

        for e in range(1, 6):

            sesion.type_element(str(uuid.uuid4()),f'{e}. TEST {e}', 'ui-text')

        sesion.type_element(random.randint(5, 100), f'8. TEST 8', 'ui-text')

        sesion.type_element(random.randint(5, 100), f'6. TEST 6', 'ui-text')
        sesion.type_element(random.randint(5, 100), f'7. TEST 7', 'ui-text')
        sesion.type_element(random.randint(5, 100), f'9. TEST 9', 'ui-text')
        sesion.type_element(random.randint(5, 100), f'10. TEST 10', 'ui-text')

        sesion.click_element("Guardar", "ui-desc")
        sesion.click_element("ACEPTAR", "id")

def fill_multiple_option_form(sesion:NavigatorAppium, offline:bool):

        #     NUM -> TEXT -> android.widget.EditText
    sesion.click_by_coordinates(674, 1100)

    # Ficha de productor
    sesion.click_element("Recolección de datos", "id")

    # Fomularios
    sesion.select_multiple_elements_by_XPATH("//android.widget.Button")
    sesion.click_from_multiple(1)

    time.sleep(5)

    #Buscador de fotos
    sesion.select_multiple_elements_by_XPATH("//android.widget.EditText")
    sesion.type_from_multiple(0, "TEST MULTIPLE OPTION")

    #Seleccionar el formulario
    sesion.click_element("TEST MULTIPLE OPTION", "ui-desc")

    time.sleep(2)

    sesion.click_element('1. TEST 1', 'ui-desc')
    sesion.click_element('OP 1', 'id')

    sesion.click_element('2. TEST 2', 'ui-desc')
    sesion.click_element('OP 2 2', 'id')

    sesion.click_element('3. TEST 3', 'ui-desc')
    sesion.click_element('OP 3 3', 'id')

    sesion.click_element('4. TEST 4', 'ui-desc')
    sesion.click_element('OP 2 4', 'id')

    sesion.click_element('5. TEST 5', 'ui-desc')
    sesion.click_element('OP 3 5', 'id')

    sesion.click_element('6. TEST 6', 'ui-desc')
    sesion.click_element('OP 3 6', 'id')


    sesion.click_element("Guardar", "ui-desc")

    
    # Pemiso almacenamiento
    sesion.click_element("Allow all", "ui-text")
    time.sleep(2)
    #Permiso musica
    sesion.click_by_coordinates(704, 1653)

    #Guardar
    sesion.click_element("Guardar", "ui-desc")
    sesion.click_element("ACEPTAR", "id")

    for e in range(0, 10):

        time.sleep(2)

        #Seleccionar el formulario
        sesion.click_element("TEST MULTIPLE OPTION", "ui-desc")

        time.sleep(2)

        sesion.click_element('1. TEST 1', 'ui-desc')
        sesion.click_element('OP 1', 'id')

        sesion.click_element('2. TEST 2', 'ui-desc')
        sesion.click_element('OP 2 2', 'id')

        sesion.click_element('3. TEST 3', 'ui-desc')
        sesion.click_element('OP 3 3', 'id')

        sesion.click_element('4. TEST 4', 'ui-desc')
        sesion.click_element('OP 2 4', 'id')

        sesion.click_element('5. TEST 5', 'ui-desc')
        sesion.click_element('OP 3 5', 'id')

        sesion.click_element('6. TEST 6', 'ui-desc')
        sesion.click_element('OP 3 6', 'id')

        #Guardar
        sesion.click_element("Guardar", "ui-desc")
        sesion.click_element("ACEPTAR", "id")



def fill_photo_form(sesion:NavigatorAppium, offline: bool):

    time_to_wait_photos = 5

    #     NUM -> TEXT -> android.widget.EditText
    sesion.click_by_coordinates(674, 1100)

    # Ficha de productor
    sesion.click_element("Recolección de datos", "id")

    # Fomularios
    sesion.select_multiple_elements_by_XPATH("//android.widget.Button")
    sesion.click_from_multiple(1)

    time.sleep(3)

    #Buscador de fotos
    sesion.select_multiple_elements_by_XPATH("//android.widget.EditText")
    sesion.type_from_multiple(0, "TEST FOTOS")

    #Seleccionar el formulario
    sesion.click_element("TEST FOTOS", "ui-desc")


    #Primera foto
    sesion.click_element('//android.view.View[@content-desc="1. FOTO 1 "]', "xpath")

    # Permisos
    sesion.click_element("While using the app", "ui-text")
    time.sleep(5)
    sesion.click_element("While using the app", "ui-text")
    
    #Captura de la foto
    time.sleep(5)
    sesion.click_by_coordinates(710, 2800)
    time.sleep(5)

    # Foto 2
    sesion.click_element('//android.view.View[@content-desc="2. FOTO 2 "]', "xpath")


    # Captura de la foto
    time.sleep(5)
    sesion.click_by_coordinates(710, 2800)
    time.sleep(5)

    sesion.click_element("Guardar", "ui-desc")

    
    # Pemiso almacenamiento
    sesion.click_element("Allow all", "ui-text")
    time.sleep(2)
    #Permiso musica
    sesion.click_by_coordinates(704, 1653)



    #Guardar
    sesion.click_element("Guardar", "ui-desc")
    sesion.click_element("ACEPTAR", "id")

    print('Se ha termino la rutina inicial')

    for e in range(0,10):

        print(f'Iteracion {e}')

        time.sleep(2)

        sesion.click_element("TEST FOTOS", "ui-desc")

        sesion.click_element('//android.view.View[@content-desc="1. FOTO 1 "]', "xpath")
        time.sleep(time_to_wait_photos)
        sesion.click_by_coordinates(710, 2800)
        time.sleep(time_to_wait_photos)

        print('Foto 1 completada')

        sesion.click_element('//android.view.View[@content-desc="2. FOTO 2 "]', "xpath")
        time.sleep(time_to_wait_photos)
        sesion.click_by_coordinates(710, 2800)
        time.sleep(time_to_wait_photos)

        print('Foto 2 completada')

        sesion.click_element("Guardar", "ui-desc")
        sesion.click_element("ACEPTAR", "id")