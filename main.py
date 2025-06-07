import streamlit as st

from helpers.data_loader import load_dataset
from components.sidebar import render_sidebar

# Configuración inicial de Streamlit
st.set_page_config(
    page_title='Fantasy Football',
    page_icon=':football:',
    layout='wide',
    initial_sidebar_state='expanded',
)

# Load dataset
df = load_dataset()

# Capturar selección del usuario
selected_wr1, selected_season = render_sidebar(df)

# Filtrar DataFrame por la temporada seleccionada
df_season = df[df['Season'] == selected_season]

# Verificar si los jugadores están en la temporada seleccionada
wr1_exists = selected_wr1 in df_season['Player'].values

if not wr1_exists:
    # Mostrar advertencias si un jugador no jugó en la temporada seleccionada
    if not wr1_exists:
        st.warning(f"⚠️ {selected_wr1} not played in season {selected_season}.")
else:
    pass
    # Mostrar comparación solo si ambos jugadores jugaron en la temporada seleccionada
    #display_wr_comparison(df_season, selected_wr1, selected_wr2)