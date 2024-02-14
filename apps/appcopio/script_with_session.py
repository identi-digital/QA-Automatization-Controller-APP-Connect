from models.appium_class import NavigatorAppium
from appium.options.common.base import AppiumOptions
from apps.appcopio.tests_with_session.register_associate_lote import (
    register_associate_lote,
    register_not_associate_lote,
)
from apps.appcopio.tests_with_session.register_transaction import generate_transaction
from apps.appcopio.tests_with_session.init_session import init_session


def script_router_with_session_appcopio(test_name: str):

    # selenium_grid_url = 'http://localhost:4444/'
    appium_url = "http://127.0.0.1:4723"

    capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        "automationName": "UiAutomator2",
    }

    capabilities = AppiumOptions().load_capabilities(capabilities)

    app_session = NavigatorAppium(command_executor=appium_url, options=capabilities)

    try:

        match test_name:

            case "REGISTRAR LOTE":

                register_associate_lote(app_session)

            case "REGISTRAR LOTE NO ASOCIADO":

                register_not_associate_lote(app_session)

            case "REGISTRAR TRANSACCION":

                generate_transaction(app_session)

            case "INICIAR SESION":

                init_session(app_session)

    except Exception as e:

        print("Hay un error")
        print(e)

        app_session.close_app()
        app_session.quit()
