# app/season_metrics.py
import streamlit as st
import pandas as pd

def render_season_metrics(df,selected_season,selected_wr,wr_id):
    df_season = df[df["Season"] == selected_season]
    st.title(f'{selected_wr} stats in {selected_season}')

    # Mostrar estadísticas de la temporada
    stats = ['Pts*',"Att", "Cmp", "Yds", "TD", "Int"]
    columns = st.columns(len(stats))