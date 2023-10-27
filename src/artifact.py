import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'date/time'

@st.cache_data
def load_data(data):
    lowercase = lambda x: str(x).lower
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
total_data = pd.read_csv('data/total_emissions_global_2019.csv', nrows=223)
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
    df = pd.read_csv('data/emissions_global_1751_2019.csv', usecols=['Year'])
    dt = pd.read_csv('data/emissions_global_1751_2019.csv', usecols=[' Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)'])
    
    chart_data = pd.DataFrame(
        {
            "Year": df,
            "Emissions": dt
        }
    )

    st.line_chart(chart_data, x="Year", y="Emissions")


#array_years = np.array(my_list)
#df = pd.DataFrame({'Years': array_years})

# chart_data = pd.DataFrame(
    # {
        # "Years": np.arange(1751, 2019, 1),
        # "Emissions": np.
    # }
# )
#st.line_chart(df)

"""
st.subheader('Number of CO2 emissions by fuel')
hist_values = np.histogram(total_data[0].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Map of CO2 Emissions Global/National')
if st.checkbox('Show map for total global CO2 emissions in 2019'):
    st.map(total_data)
elif st.checkbox('Show map for total global CO2 emissions per capita in 2019'):
    st.map(capita_data)
elif st.checkbox('Show chart for total global CO2 emissions from 1751-2019'):
    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Year', 'Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)', 'Carbon emissions from solid fuel consumption', 'Carbon emissions from liquid fuel consumption', 'Carbon emissions from gas fuel consumption', 'Carbon emissions from cement production', 'Carbon emissions from gas flaring', 'Per capita carbon emissions (metric tons of carbon; after 1949 only)'])
    st.line_chart(data='data/emissions_global_1751_2019.csv', x='Year', y='CO2 Emissions', color=None, width=None, height=None, use_container_width=False)
"""