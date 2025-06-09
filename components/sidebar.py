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

def render_sidebar(df):
    # Renderiza la barra lateral completa.
    with st.sidebar:
        st.image('assets/logo.jpg', use_container_width=True)

        # Obtener lista de temporadas ordenadas (más recientes primero)
        season_list = sorted(df["Season"].unique().tolist(), reverse=True)
        
        # Selección de temporada primero
        selected_season = st.selectbox('Select a season', season_list, key='season')
        
        # Filtrar el dataframe por la temporada seleccionada
        season_df = df[df["Season"] == selected_season]
        
        # Obtener lista de WRs que jugaron en esa temporada
        wr_list = season_df["Player"].unique().tolist()
        
        # Selección del WR
        selected_wr1 = st.selectbox("Select a wide receiber", wr_list, key='wr1')

    return selected_wr1, selected_season