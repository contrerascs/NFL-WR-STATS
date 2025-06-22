import streamlit as st

from helpers.data_loader import load_dataset
from components.sidebar import render_sidebar
from components.render_season_metrics import render_season_metrics

# Configuración inicial de Streamlit
st.set_page_config(
    page_title='The Best Wide Receiber',
    page_icon=':football:',
    layout='wide',
    initial_sidebar_state='expanded',
)

# Load dataset
df = load_dataset()

st.title('Analiza las estadísticas de tu WR favorito')

# Seleccionar QB
wr_list = df["Player"].unique()
selected_wr = st.selectbox("Selecciona un WR", wr_list)

# Filtrar datos del QB seleccionado y obtener el ID
wr_data = df[df["Player"] == selected_wr]
wr_id = wr_data["WR_ID"].iloc[0]

# Capturar selección del usuario
selected_season = render_sidebar(df,selected_wr,wr_id)

# Filtrar DataFrame por la temporada seleccionada
df_season = df[df['Season'] == selected_season]

# Si se seleccionó una temporada específica, renderizamos las gráficas
if selected_season != "Toda la carrera":
    render_season_metrics(df,selected_season,selected_wr,wr_id)
else:
    pass