from models.appium_class import NavigatorAppium
import time

def init_session(session: NavigatorAppium):

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # Ingresar usuario
    session.type_from_multiple(0, 'fandia_acp')

    session.type_from_multiple(1, 'Agros-6776')

    session.click_element("Iniciar sesión", 'id')

    time.sleep(5)

    session.click_element("Ingresar", 'id')