from models.selenium_class import Navigator
from selenium import webdriver
import time


def execute_script_perhusa(test):

    selenium_grid_url = "http://localhost:4444/wd/hub"
    perhusa_link = "https://perhusa.qa.identi.digital"

    options = webdriver.ChromeOptions()

    try:

        nav_session = Navigator(command_executor=selenium_grid_url, options=options)

        nav_session.init_session(perhusa_link)

        # Ingresar credenciales
        nav_session.type_element(
            location="username", type_location="id", content="perhusa_test"
        )
        nav_session.type_element(
            location="password", type_location="id", content="Perhusa-6776"
        )
        nav_session.click_element(location="Ingresar", type_location="text")

        test(nav_session)
        # time.sleep(10)
        # nav_session.save_screenshot("hola.png")

        nav_session.quit()

    except Exception as e:

        print("error")
        nav_session.save_screenshot("hola.png")
        print(e)
        nav_session.quit()
