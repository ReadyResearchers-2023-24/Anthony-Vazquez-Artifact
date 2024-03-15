import streamlit as st
import pandas as pd

st.header(' ',divider='grey')
st.title(':blue[Charting Global Emissions]')
st.header(' ',divider='grey')

st.subheader('Line chart of global emissions from 1751 to 2019(millions of tons of C)')

if st.checkbox(':grey[Global Carbon Emissions by fossil fuel(Line Chart)]'):
    df = pd.read_csv('data/emissions_global_1751_2019.csv', dtype={"Year": str})
    chart_data = pd.DataFrame(df, columns=["Year", "Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.line_chart(chart_data, x="Year", y=["Emissions fossil fuel", "Emissions solid fuel", "Emissions liquid fuel", "Emissions gas fuel", "Emissions cement production", "Emissions gas flaring", "Emissions per capita(metric tons of carbon)"])
    st.write(':green[In this Line Chart, we see the relation that advancing years along the time scale correlates to increasing amount of emissions.]')
    st.write(':green[We can see the same data from the running list of maps displayed here in a different way, and it gives a much better idea of the volume that these emissions have increased by.]')
    st.write(':green[Charts like these make it increasingly obvious that there is an issue with the amount of pollution that is being emitted by human activity, and becomes increasingly evident when compared with other charts.]')