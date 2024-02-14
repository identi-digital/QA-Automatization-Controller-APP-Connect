import streamlit as st
from apps.agros_connect.script import script_router_offline, script_router_online
from apps.agros_connect.script_with_session import script_router_online_with_session
import uuid

st.title('Tests online')

list_tests_online = [
    "REGISTRAR PRODUCTOR",
    "FORMULARIO FOTOS",
    "FORMULARIO TEXTO",
    "FORMULARIO OPCION MULTIPLE"
]

list_tests_offline = [
    "REGISTRAR PRODUCTOR",
    "FORMULARIO FOTOS",
    "FORMULARIO TEXTO"
]

list_tests_with_session = [
    "REGISTRAR PRODUCTOR",
    "FORMULARIO FOTOS",
    "FORMULARIO TEXTO",
    "FORMULARIO OPCION MULTIPLE"
]

online = st.toggle('Es online')

if online:

    test_selected = st.selectbox('Elige el test', options=list_tests_online)

else:

    test_selected = st.selectbox('Elige el test', options=list_tests_offline)

def execute_test():

    if online:

        script_router_online(test_selected)

    else:

        script_router_offline(test_selected)

st.button('Ejecutar', on_click=execute_test)

st.title('Tests con sesion')

test_selected_with_session = st.selectbox('Elige el test ', list_tests_with_session)

def execute_test_with_session():

    script_router_online_with_session(test_selected_with_session)

st.button('Ejecutarr test con sesion', on_click=execute_test_with_session)