from models.appium_class import NavigatorAppium
from appium.options.common.base import AppiumOptions
from apps.agros_connect.tests_with_session.form_all_params import fill_multiple_option_form, fill_photo_form, fill_text_form
from apps.agros_connect.tests_with_session.register_producer import register_producer
from apps.agros_connect.tests_with_session.register_productive_unit import register_productive_unit

def script_router_online_with_session(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2"
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    try:

        match test_name:

            case "REGISTRAR PRODUCTOR":

                for e in range(0,20):

                    register_producer(app_session)
                    register_productive_unit(app_session, False)

            case "FORMULARIO FOTOS":

                fill_photo_form(app_session)

            case "FORMULARIO TEXTO":

                fill_text_form(app_session)

            case "FORMULARIO OPCION MULTIPLE":

                fill_multiple_option_form(app_session)

        app_session.close_app()
        app_session.quit()

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()