#Render carrer metrics
import streamlit as st

def render_carrer_metrics(wr_data,selected_wr):
    st.subheader(f'Estadisticas de {selected_wr} en toda su carrera')

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    
    with c1:
        games = int(wr_data["GS"].sum())
        st.metric("Partidos Jugados",f"{games:,}",border=True)
    
    with c2:
        cmp_value = float(wr_data['Cmp%'].iloc[0])
        st.metric('Cmp%',f"{round(cmp_value, 2)}%",border=True)
    
    with c3:
        yards = int(wr_data["Yds"].sum())
        st.metric("Yardas Totales",f"{yards:,}",border=True)
    
    with c4:
        tds = int(wr_data["TD"].sum())
        st.metric("Touchdowns", tds,border=True)
    
    with c5:
        ints = int(wr_data["Int"].sum())
        st.metric("Intercepciones", ints,border=True)
    
    with c6:
        rating = float(wr_data['Rate'].iloc[0])
        st.metric('Rating', value=round(rating, 2),border=True)