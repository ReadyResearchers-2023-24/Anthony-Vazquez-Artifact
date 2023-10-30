import streamlit as st
import pandas as pd
import numpy as np
import random as rd


DATE_COLUMN = 'date/time'

@st.cache_data
def load_data(data):
    lowercase = lambda x: str(x).lower
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
total_data = pd.read_csv('data/total_emissions_global_2019.csv', nrows=222)
load_data(total_data)
capita_data = pd.read_csv('data/emissions_per_capita_2019.csv', nrows=223)
load_data(capita_data)
global_data = pd.read_csv('data/emissions_global_1751_2019.csv', nrows=270)
load_data(global_data)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data for total CO2 emissions from fossil fuels'):
    st.subheader('Raw data(thousand metric tons)')
    st.write(total_data)

if st.checkbox('Show raw data for total global C02 emissions per capita'):
    st.subheader('Raw data(metric tons)')
    st.write(capita_data)

if st.checkbox('Show raw data for total global C02 emissions from 1751-2019'):
    st.subheader('Raw data(million metric tons)')
    st.write(global_data)

st.subheader('Line Charts of global emissions from 1751 to 2019')

if st.checkbox('Global Carbon Emissions by fossil fuel'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})

    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel(million metric tons of C)", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])

    st.line_chart(chart_data, x="Year", y=["Emissions fossil fuel(million metric tons of C)", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])

    if st.checkbox('Click to see the raw data of this graph'):
        st.write(chart_data)

if st.checkbox('Show map of global carbon emissions(thousand metric tons of C)'):
    df = pd.read_csv('data/total_emissions_global_2019.csv')

    chart_data = pd.DataFrame(df, columns=['Emissions', 'LAT', 'LON'])
    st.map(chart_data, size='Emissions')