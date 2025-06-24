# app/season_metrics.py
import streamlit as st
import pandas as pd

def render_season_metrics(df,selected_season,selected_wr,wr_id):
    df_season = df[df["Season"] == selected_season]
    st.title(f'{selected_wr} stats in {selected_season}')

    print(df.head())

    stats = ['Tgt','Rec','Yds','Y/R','Y/G','TD','YAC']
    
    columns = st.columns(7)
    
    for col, stat in zip(columns, stats):
        metric = df_season[stat].sum()
        with col:
            st.metric(stat, f"{metric}",border=True)