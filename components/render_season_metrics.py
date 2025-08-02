# app/season_metrics.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def rank_in_stat(df,player,stat):
    player_data = df[df['Player'] == player]
    df_tm = player_data[player_data['Team'] == '2TM']
    if df_tm['Team'].values == '2TM':
        player_data = df_tm
        print(player_data)

    metric = player_data[stat].sum()

    titulos = {
        'Tgt':'Targets',
        'Rec':'Receptions',
        'Yds':'Air Yds',
        'Y/R':'Yds per rec',
        'Y/G':'Yds per game',
        'YAC':'Yds after catch',
        'TD':'Touchdowns'
    }   

    df = df.sort_values(by=stat, ascending=False).reset_index(drop=True)
    df[stat + "_rank"] = df[stat].rank(method="min", ascending=False)
    rank = df.loc[df["Player"] == player, stat + "_rank"].values[0]

    if stat == 'Int':
        if rank > 20:
            st.metric(titulos[stat], f"{metric}", f"{(int(rank))}º",border=True)
        elif rank > 10:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º", "off",border=True)
        else:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º","inverse",border=True)
    else:
        if rank > 20:
            st.metric(titulos[stat], f"{metric}", f"{(int(rank))}º","inverse",border=True)
        elif rank > 10:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º", "off",border=True)
        else:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º",border=True)

def render_season_metrics(wr_data,selected_season,selected_wr,df):
    df_season = wr_data[wr_data["Season"] == selected_season]
    st.title(f'{selected_wr} stats in {selected_season}')

    stats = ['Tgt','Rec','Yds','Y/R','Y/G','TD','YAC']

    df_tm = df_season[df_season['Team'] == '2TM']

    columns = st.columns(7)
    for col, stat in zip(columns, stats):
        with col:
            rank_in_stat(df,selected_wr,stat)

def render_season_plots(wr_stats,selected_wr,selected_season):
    # Gráfica de pastel: Pases Completos vs Incompletos
    completos = wr_stats["Cmp%"]
    incompletos = 100 - completos
    labels = ["Pases Completos", "Pases Incompletos"]
    values = [completos, incompletos]
    colors = ["#1CB698", "#0a4237"]
    
    fig_pie = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.5,
        marker=dict(colors=colors),
        textinfo="percent"
    ))
    fig_pie.update_layout(
        title=f"Porcentaje de Pases Completos de {selected_wr} en {selected_season}",
        template="plotly_dark"
    )