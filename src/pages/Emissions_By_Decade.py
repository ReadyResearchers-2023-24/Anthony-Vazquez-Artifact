import streamlit as st
import pandas as pd

st.header(' ',divider='grey')
st.title(':blue[Global Emissions by Decade from 1750-2020]')

st.write('This is a running system of maps including information on :blue[global emissions] using each decade from :blue[1750 to 2020] as marking points.')
st.write('The measurements for these maps are recorded in :blue[billions of tons of Carbon pollution], and for each respective map, the smallest circle represents :blue[0 billion tons] of pollution.')
st.write('It is important to note that the :blue[pollution] used for these maps consists solely of :blue[Carbon-Based pollution], some of which are the leading :blue[pollutants] that scientists know of today, emitting a staggering :blue[35 billion tons annually in CO2] alone.')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1750')
if st.checkbox(':grey[Click to view map for 1750!]'):
    temp_data = pd.read_csv('data/emissions_1750.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[This map for global emissions from 1750 shows how little industrialization and large-scale production there was during this time, mony of the early maps in this segment will look similar as there was not much pollution being emitted when compared to the numbers of todays world.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[However, once you go through later maps, you will see this is most definitely not the case, and that the emitions that are being produced increase exponentially as the years go by.]')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1760')
if st.checkbox(':grey[Click to view map for 1760!]'):
    temp_data = pd.read_csv('data/emissions_1760.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.write(':blue[Being the fact that there are not as many countries from this time as there are today, along with the fact that this sort of data was much harder to collect back then, there are not many points of data to reference.]')
    st.map(map_data, size='Emissions')
    st.write(':blue[Maps such as these truly help to visualize and understand the difference of the world today versus the world from centuries ago when technology was not nearly as prevalent as it is today.]')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1770')
if st.checkbox(':grey[Click to view map for 1770!]'):
    temp_data = pd.read_csv('data/emissions_1770.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1780')
if st.checkbox(':grey[Click to view map for 1780!]'):
    temp_data = pd.read_csv('data/emissions_1780.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1790')
if st.checkbox(':grey[Click to view map for 1790!]'):
    temp_data = pd.read_csv('data/emissions_1790.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1800')
if st.checkbox(':grey[Click to view map for 1800!]'):
    temp_data = pd.read_csv('data/emissions_1800.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1810')
if st.checkbox(':grey[Click to view map for 1810!]'):
    temp_data = pd.read_csv('data/emissions_1810.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1820')
if st.checkbox(':grey[Click to view map for 1820!]'):
    temp_data = pd.read_csv('data/emissions_1820.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1830')
if st.checkbox(':grey[Click to view map for 1830!]'):
    temp_data = pd.read_csv('data/emissions_1830.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1840')
if st.checkbox(':grey[Click to view map for 1840!]'):
    temp_data = pd.read_csv('data/emissions_1840.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1850')
if st.checkbox(':grey[Click to view map for 1850!]'):
    temp_data = pd.read_csv('data/emissions_1850.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1860')
if st.checkbox(':grey[Click to view map for 1860!]'):
    temp_data = pd.read_csv('data/emissions_1860.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1870')
if st.checkbox(':grey[Click to view map for 1870!]'):
    temp_data = pd.read_csv('data/emissions_1870.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1880')
if st.checkbox(':grey[Click to view map for 1880!]'):
    temp_data = pd.read_csv('data/emissions_1880.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1890')
if st.checkbox(':grey[Click to view map for 1890!]'):
    temp_data = pd.read_csv('data/emissions_1890.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1900')
if st.checkbox(':grey[Click to view map for 1900!]'):
    temp_data = pd.read_csv('data/emissions_1900.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1910')
if st.checkbox(':grey[Click to view map for 1910!]'):
    temp_data = pd.read_csv('data/emissions_1910.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1920')
if st.checkbox(':grey[Click to view map for 1920!]'):
    temp_data = pd.read_csv('data/emissions_1920.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1930')
if st.checkbox(':grey[Click to view map for 1930!]'):
    temp_data = pd.read_csv('data/emissions_1930.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1940')
if st.checkbox(':grey[Click to view map for 1940!]'):
    temp_data = pd.read_csv('data/emissions_1940.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1950')
if st.checkbox(':grey[Click to view map for 1950!]'):
    temp_data = pd.read_csv('data/emissions_1950.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1960')
if st.checkbox(':grey[Click to view map for 1960!]'):
    temp_data = pd.read_csv('data/emissions_1960.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1970')
if st.checkbox(':grey[Click to view map for 1970!]'):
    temp_data = pd.read_csv('data/emissions_1970.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1980')
if st.checkbox(':grey[Click to view map for 1980!]'):
    temp_data = pd.read_csv('data/emissions_1980.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 1990')
if st.checkbox(':grey[Click to view map for 1990!]'):
    temp_data = pd.read_csv('data/emissions_1990.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 2000')
if st.checkbox(':grey[Click to view map for 2000!]'):
    temp_data = pd.read_csv('data/emissions_2000.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 2010')
if st.checkbox(':grey[Click to view map for 2010!]'):
    temp_data = pd.read_csv('data/emissions_2010.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')

st.header(' ',divider='grey')
st.header('Map of emissions in the year 2020')
if st.checkbox(':grey[Click to view map for 2020!]'):
    temp_data = pd.read_csv('data/emissions_2020.csv')
    map_data = pd.DataFrame({
        "Emissions": temp_data['Emissions'] / 1000,
        "LAT": temp_data['LAT'],
        "LON": temp_data['LON']
    })
    st.map(map_data, size='Emissions')
