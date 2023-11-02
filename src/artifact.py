import streamlit as st
import pandas as pd
import numpy as np
import random as rd

DATE_COLUMN = 'date/time'

data_load_state = st.text('Loading data...')
total_data = pd.read_csv('data/total_emissions_global_2019.csv', dtype={"Year": str}, nrows=36)
capita_data = pd.read_csv('data/emissions_per_capita_2019.csv', dtype={"Year": str}, nrows=223)
global_data = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str}, nrows=270)
data_load_state.text("Done loading data! (using st.cache_data)")

if st.checkbox('Show raw data for total CO2 emissions from fossil fuels'):
    st.subheader('Raw data(thousand metric tons of C)')
    st.write(total_data)

if st.button('Show raw data for total global C02 emissions per capita'):
    st.subheader('Raw data(metric tons of C)')
    st.write(capita_data)

if st.toggle('Show raw data for total global C02 emissions from 1751-2019'):
    st.subheader('Raw data(million metric tons of C)')
    st.write(global_data)

st.subheader('Line chart of global emissions from 1751 to 2019.')
if st.checkbox('Global Carbon Emissions by fossil fuel(Line Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.line_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    if st.checkbox('Click to see the raw data of this graph'):
        st.write(chart_data)

st.subheader('Bar chart of global emissions from 1751 to 2019.')
if st.checkbox('Global Carbon Emissions by fossil fuel(Bar Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.bar_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    if st.checkbox('Click to see the raw data of this graph'):
        st.write(chart_data)

st.subheader('Area chart of global emissions from 1751 to 2019.')
if st.checkbox('Global Carbon Emissions by fossil fuel(Area Chart)'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.area_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    if st.checkbox('Click to see the raw data of this graph'):
        st.write(chart_data)

st.subheader('Map of total global emissions in 2019.')
if st.checkbox('Show map of global carbon emissions(thousand metric tons of C)'):
    df = pd.read_csv('data/total_emissions_global_2019.csv')
    chart_data = pd.DataFrame(df, columns=['Emissions', 'LAT', 'LON'])
    st.map(chart_data, size='Emissions')
