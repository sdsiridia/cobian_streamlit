'''pagina principal'''
import streamlit as st


pg = st.navigation([st.Page("page_1.py"), st.Page(
    "page_2.py"), st.Page("page_3.py")])
pg.run()