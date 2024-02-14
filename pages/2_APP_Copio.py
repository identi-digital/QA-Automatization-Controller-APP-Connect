import streamlit as st
from apps.appcopio.script import (
    script_router_offline_appcopio,
    script_router_online_appcopio,
)

from apps.appcopio.script_with_session import script_router_with_session_appcopio

st.title("Tests online")

list_tests_online = ["REGISTRAR LOTE", "REGISTRAR LOTE NO ASOCIADO"]

list_tests_offline = ["REGISTRAR LOTE", "REGISTRAR LOTE NO ASOCIADO"]


online = st.toggle("Es online")

if online:

    test_selected = st.selectbox("Elige el test", options=list_tests_online)

else:

    test_selected = st.selectbox("Elige el test", options=list_tests_offline)


def execute_test():

    if online:

        script_router_online_appcopio(test_selected)

    else:

        script_router_offline_appcopio(test_selected)


st.button("Ejecutar", on_click=execute_test)

list_tests_with_session = [
    "REGISTRAR LOTE",
    "REGISTRAR LOTE NO ASOCIADO",
    "REGISTRAR TRANSACCION",
    "INICIAR SESION"
]

st.title("Tests con sesion")

test_selected_with_session = st.selectbox("Elige el test ", list_tests_with_session)

def execute_test_with_session():

    script_router_with_session_appcopio(test_selected_with_session)

st.button('Ejecutarr test con sesion', on_click=execute_test_with_session)
