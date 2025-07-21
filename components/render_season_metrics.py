# app/season_metrics.py
import streamlit as st
import pandas as pd

def rank_in_stat(week_data,player,stat):
    player_data = week_data[week_data['Player'] == player]
    metric = player_data[stat].sum()
    
    #print(player_data.head())

    titulos = {
        'Tgt':'Targets',
        'Rec':'Receptions',
        'Yds':'Air Yds',
        'Y/R':'Yds per rec',
        'Y/G':'Yds per game',
        'YAC':'Yds after catch',
        'TD':'Touchdowns'
    }   

    week_data = week_data.sort_values(by=stat, ascending=False).reset_index(drop=True)
    week_data[stat + "_rank"] = week_data[stat].rank(method="min", ascending=False)
    rank = week_data.loc[week_data["Player"] == player, stat + "_rank"].values[0]

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
    
    print(df_tm['Team'].values[0])

    if df_tm['Team'].values[0] == '2TM':
        columns = st.columns(7)
        for col, stat in zip(columns, stats):
            with col:
                rank_in_stat(df_tm,selected_wr,stat)
    else:        
        columns = st.columns(7)
        for col, stat in zip(columns, stats):
            with col:
                rank_in_stat(df,selected_wr,stat)