'''Leer correos no leidos y sacar su asunto, origen y cuerpo'''

import streamlit as st



# Pedir el usuario y la contraseña
USERNAME = st.text_input("Correo: ")
PASSWORD = st.text_input("Enter a password", type="password")

