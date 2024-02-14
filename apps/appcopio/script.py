from models.appium_class import NavigatorAppium
from appium.options.common.base import AppiumOptions

from apps.appcopio.tests.register_associate_lote import register_associate_lote, register_not_associate_lote

import time


def init_session(session: NavigatorAppium):

    session.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # Ingresar usuario
    session.type_from_multiple(0, 'fandia_acp')

    session.type_from_multiple(1, 'Agros-6776')

    session.click_element("Iniciar sesión", 'id')

    time.sleep(5)

    session.click_element("Ingresar", 'id')



def script_router_online_appcopio(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2",
        "appPackage": "com.example.appcopio",
        "appActivity": ".MainActivity",
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    time_to_wait_data_app = 50

    try:

        match test_name:

            case "REGISTRAR LOTE":

                # Inicio de sesion en la aplicacion
                init_session(app_session)

                time.sleep(time_to_wait_data_app)

                register_associate_lote(app_session)

            case 'REGISTRAR LOTE NO ASOCIADO':

                init_session(app_session)

                time.sleep(40)

                register_not_associate_lote(app_session)


        app_session.close_app()
        app_session.quit()

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()


def script_router_offline_appcopio(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2",
        "appPackage": "com.example.appcopio",
        "appActivity": ".MainActivity",
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    time_to_wait_data_app = 50

    try:

        match test_name:

            case "REGISTRAR LOTE":

                # Inicio de sesion en la aplicacion
                init_session(app_session)

                time.sleep(time_to_wait_data_app)

                app_session.toggle_wifi()

                register_associate_lote(app_session)

                app_session.toggle_wifi()

            case 'REGISTRAR LOTE NO ASOCIADO':

                init_session(app_session)

                time.sleep(time_to_wait_data_app)

                app_session.toggle_wifi()

                register_not_associate_lote(app_session)

                app_session.toggle_wifi()

        app_session.close_app()
        app_session.quit()

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()