from models.appium_class import NavigatorAppium
from appium.options.common.base import AppiumOptions
from apps.agros_connect.tests.register_producer import register_producer
from apps.agros_connect.tests.register_productive_unit import register_productive_unit
from apps.agros_connect.tests.form_all_params import (
    fill_text_form,
    fill_photo_form,
    fill_multiple_option_form,
)

import time


def init_session(session: NavigatorAppium):

    # Ingresar usuario
    session.type_element(
        "qa_app_user", '(//android.widget.EditText[@text="Usuario"])[2]', "xpath"
    )

    # Ingresar contraseña
    session.type_element(
        "agROS_2023!", '(//android.widget.EditText[@text="Contraseña"])[2]', "xpath"
    )

    # Click Iniciar
    session.click_element('//android.widget.Button[@content-desc="Ingresar"]', "xpath")


def script_router_online(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2",
        # "appPackage": "global.identi.stage",
        # "appActivity": "tech.agros.connect.MainActivity",
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    time_to_wait_data_app = 50

    try:

        match test_name:

            case "REGISTRAR PRODUCTOR":

                # Inicio de sesion en la aplicacion
                init_session(app_session)

                time.sleep(5)

                register_producer(app_session)
                register_productive_unit(app_session, False)

            case "FORMULARIO FOTOS":

                # init_session(app_session)

                # time.sleep(time_to_wait_data_app)

                fill_photo_form(app_session, False)

            case "FORMULARIO TEXTO":

                # init_session(app_session)

                # time.sleep(time_to_wait_data_app)

                fill_text_form(app_session, False)

            case "FORMULARIO OPCION MULTIPLE":

                # init_session(app_session)

                # time.sleep(time_to_wait_data_app)

                fill_multiple_option_form(app_session, False)

        app_session.close_app()
        app_session.quit()

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()


def script_router_offline(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2",
        "appPackage": "global.identi.stage",
        "appActivity": "tech.agros.connect.MainActivity",
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    try:

        match test_name:

            case "REGISTRAR PRODUCTOR":

                # Inicio de sesion en la aplicacion
                init_session(app_session)

                time.sleep(2)

                register_producer(app_session)
                register_productive_unit(app_session, True)

            case "FORMULARIO FOTOS":

                init_session(app_session)

                time.sleep(22)

                app_session.toggle_wifi()

                fill_text_form(app_session)

                app_session.toggle_wifi()

        app_session.close_app()
        app_session.quit()

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()
