from models.selenium_class import Navigator
import time

def test_perhusa_create_user(session:Navigator):

    #Ingresar al modulo
    session.click_element('Ventas', 'text')

    #Registrar venta
    session.click_element('Registrar venta', 'text')

    #Archivos
    entry_file = './files/entrada.xlsx'
    salida_file = './files/salida.xlsx'
    proceso_file = './files/proceso.xlsx'
    despacho_file = './files/despacho.xlsx'

    files = [entry_file, salida_file, proceso_file, despacho_file]

    #Location

    input_location = "//input[@type='file' and @accept='.xlsx,.xls']"

    # Ciclo de archivos

    for file in files:

        #Editamos la etiqueta
        session.edit_style_element('xpath', input_location, 'display', 'inline')

        #Enviamos los datos
        session.element.send_keys(file)

        #Guardamos
        session.click_element('Guardar y continuar', 'text')
        session.save_screenshot('Hola5.png')

    session.click_element('OK', 'text')

    # session.select_element_by_XPATH("//input[@type='file' and @accept='.xlsx,.xls']")

    # session.execute_script("arguments[0].style.display = 'inline';", session.element)

    # session.element.send_keys(file)
    # session.save_screenshot('hola3.png')