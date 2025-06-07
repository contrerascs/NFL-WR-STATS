import streamlit as st

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