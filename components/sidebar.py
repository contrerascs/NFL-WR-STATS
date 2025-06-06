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
        
        # Obtener lista de QBs que jugaron en esa temporada
        wr_list = season_df["Player"].unique().tolist()
        
        # Verificar que haya al menos 2 QBs en la temporada seleccionada
        if len(wr_list) < 2:
            st.warning(f"¡Solo hay {len(wr_list)} WR(s) en la temporada {selected_season}!")
            if len(wr_list) == 1:
                return wr_list[0], None, selected_season
            else:
                return None, None, selected_season
        
        # Selección del primer QB
        selected_wr1 = st.selectbox("Select a wide receiber", wr_list, key='wr1')
        
        # Filtrar la lista para el segundo selectbox (excluyendo el primero)
        wr_list_filtered = [wr for wr in wr_list if wr != selected_wr1]
        
        # Selección del segundo QB (sin incluir el primero seleccionado)
        selected_wr2 = st.selectbox("Select a wide receiber", wr_list_filtered, key='wr2')

    return selected_wr1, selected_wr2, selected_season