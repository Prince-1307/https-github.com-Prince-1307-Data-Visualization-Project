import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

final_df = pd.read_csv('India.csv')

list_of_state = list(final_df['State'].unique())
list_of_state.insert(0,'Overall India')
cols = final_df.columns[4:]


st.sidebar.title("Data Visualization App for India")

state = st.sidebar.selectbox('Select a State',list_of_state)
primary = st.sidebar.selectbox('Primary Parameter',cols)
Secondary = st.sidebar.selectbox('Secondary Parameter',cols)

plot = st.sidebar.button('Plot Graph')

if plot:
    if state == 'Overall India' :
        # st.title(f'India {primary} vs {Secondary} ')
        # plot for India
        df = final_df
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', size=primary, color=Secondary,
                             hover_name='District', hover_data=[primary, Secondary],
                             title=f'India {primary} vs {Secondary} ',
                            size_max=15, zoom=3, width=1200, height=700, map_style="carto-positron",
                            color_continuous_scale="plasma" )
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        df = final_df[final_df['State'] == state]
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', size=primary, color=Secondary,
                             hover_name='District', hover_data=[primary, Secondary],
                             title=f'India {primary} vs {Secondary} ',
                            size_max=25, zoom=5, width=1200, height=700, map_style="carto-positron",
                            color_continuous_scale="plasma" )
        st.plotly_chart(fig, use_container_width=True)
