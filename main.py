import streamlit as st

from helpers.data_loader import load_dataset

# Configuración inicial de Streamlit
st.set_page_config(
    page_title='Fantasy Football',
    page_icon=':football:',
    layout='wide',
    initial_sidebar_state='expanded',
)

# Load dataset
df = load_dataset()