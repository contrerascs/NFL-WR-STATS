import streamlit as st

from helpers.data_utils import get_image_path

def render_player_info(col, selected_wr, wr_id):
    # Renderiza la información del jugador en la barra lateral.
    with col:
        st.header('Wide Receiver')
        image_path = get_image_path(wr_id)
        st.image(image_path, width=150)
        st.subheader(selected_wr)

def render_seasons_info(col, wr_data):
    # Renderiza la información de las temporadas en la barra lateral.
    with col:
        st.subheader(':gray[Temporadas]', divider="gray")
        start_qb = wr_data['Season'].min()
        end_qb = wr_data['Season'].max()
        st.text(f'{start_qb} - {end_qb}')
        st.subheader(':gray[Equipos]', divider="gray")
        start_qb = wr_data['Season'].min()
        end_qb = wr_data['Season'].max()
        st.text(f'{start_qb} - {end_qb}')

def render_sidebar(df,selected_wr,wr_id):
    # Renderiza la barra lateral completa.
    with st.sidebar:
        st.image('assets/logo.jpg', use_container_width=True)

        col1, col2 = st.columns(2)

        # Información del jugador
        render_player_info(col1, selected_wr, wr_id)
        wr_data = df[df["Player"] == selected_wr]
        render_seasons_info(col2,wr_data)

        # Filtrar el dataframe por el jugador seleccionado
        season_df = df[df["Player"] == selected_wr]

        # Obtener lista de temporadas ordenadas (más recientes primero)
        season_list = ["Toda la carrera"] + sorted(season_df["Season"].unique().tolist(), reverse=True)
        
        # Selección de temporada
        selected_season = st.selectbox('Select a season', season_list, key='season')

    return selected_season