from models.appium_class import NavigatorAppium
import time
import random


def register_productive_unit(sesion: NavigatorAppium, offline: bool):

    widgets = "//android.widget.EditText | //android.widget.Button"
    sesion.select_multiple_elements_by_XPATH(widgets)

    # Nombre
    sesion.type_from_multiple(1, "UNIDAD PRUEBA")

    # Area
    sesion.type_from_multiple(2, "500")

    # Tenencia
    sesion.click_from_multiple(3)
    sesion.click_element("Propietario", "id")

    # Cultivo principal
    sesion.click_from_multiple(4)
    sesion.click_element("Aji", "id")

    # Seleccionar cultivos
    sesion.click_element("Seleccionar cultivos", "id")
    sesion.click_element("Aji", "id")
    sesion.click_element("Aji Mirasol", "id")
    sesion.click_element("GUARDAR", "id")

    # Ubicacion de ingreso
    sesion.click_element("6. Capturar ubicación de ingreso (Opcional)", "id")

    # Permisos
    sesion.click_element("While using the app", "ui-text")
    time.sleep(5)

    sesion.movement_in_view(40)

    # Poligono
    sesion.click_element("7. Dibujar el Polígono (Opcional)", "id")
    time.sleep(10)

    points = [
        [
            float(f"-78.5{random.randint(20000,30000)}"),
            float(f"-5.4{random.randint(20000,30000)}"),
        ]
        for e in range(0, 5)
    ]

    for p in points:

        # Establecemos la ubicacion aleatoria
        sesion.set_location(p[1], p[0])

        # Click para ubicar en localizacion
        sesion.click_by_coordinates(1307, 447)
        time.sleep(2)
        # Guarda punto
        sesion.click_by_coordinates(740, 1754)

    sesion.click_element("Guardar", "id")

    # Cambio de seccion
    sesion.movement_in_view(30)
    sesion.select_multiple_elements_by_XPATH("//android.widget.EditText")

    # Direccion
    sesion.type_from_multiple(0, "Direccion")

    # Departamento
    sesion.click_from_multiple(1)
    sesion.click_element("Amazonas", "id")

    # Provincia
    sesion.click_from_multiple(2)
    sesion.click_element("Bongará", "id")

    # Distrito
    sesion.click_from_multiple(3)
    sesion.click_element("Churuja", "id")

    # Cambio de seccion
    sesion.movement_in_view(40)

    # # Patrones de la parcela
    # time.sleep(2)
    # sesion.click_by_coordinates(632, 1265)
    # sesion.click_element("Topatopa", "id")

    # Fecha
    sesion.click_element(
        "13. Selecciona la fecha de la última campaña (Obligatorio)", "id"
    )
    sesion.click_element("ACEPTAR", "id")

    # Altitud
    # sesion.click_element("14. Altitud (Opcional) *Altitud: 0 m.s.n.m.", "id")
    sesion.click_element(
        '//android.view.View[@content-desc="14. Altitud (Opcional)"]', "xpath"
    )

    time.sleep(5)

    # Cantidad producida
    sesion.type_element(
        "20",
        '//android.widget.EditText[@text="15. Indica la cantidad producida (Opcional)"]',
        "xpath",
    )

    if offline:

        sesion.toggle_wifi()

    # Registrar
    sesion.click_element("Siguiente", "id")
    sesion.click_element("ACEPTAR", "id")

    if offline:

        time.sleep(5)

        sesion.click_element("Siguiente", "id")
        sesion.click_element("ACEPTAR", "id")

        sesion.toggle_wifi()
        # time.sleep(4)

        # sesion.click_element("Abrir el menú de navegación", "id")
        # sesion.click_element("Módulo de sincronización", "id")

        # sesion.click_element("Allow all", "ui-text")
        # time.sleep(2)
        # sesion.click_by_coordinates(704, 1653)

        # # sesion.click_element("Registro de nuevos productores", "ui-desc")
        # time.sl
        # sesion.click_by_coordinates(716, 1110)
        # sesion.click_element("Sincronizar", "id")

    time.sleep(10)
