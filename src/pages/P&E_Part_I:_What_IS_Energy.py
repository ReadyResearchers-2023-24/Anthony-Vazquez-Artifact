import json
import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

st.sidebar.success("Choose a page from directory above.")

def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

st.header(' ',divider='grey')
st.title(":blue[Pollution and Energy Overview]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part I:] :orange[What IS Pollution?]')
st.write(' ')
st.write(' ')

st.write(":red[Pollution] occurs when harmful substances are introduced into the :green[environment], causing adverse effects on :green[living organisms] and :green[ecosystems].")

st_lottie(load_lottie_file("animations/killing_nature.json"))

st.write("These :red[pollutants] can be in the form of :green[solid], :green[liquid], or :green[gas], and they often result from human activities such as :red[industrial processes], :red[transportation], :red[agriculture], and :red[waste disposal].")

st_lottie(load_lottie_file("animations/emissions.json"))

st.write("Some common pollutants include :red[carbon dioxide (]:grey[CO2]:red[)], :red[sulfur dioxide (]:grey[SO2]:red[)], :red[nitrogen dioxide (]:grey[NO2]:red[)], :red[particulate matter (]:grey[PM]:red[)], :red[ozone (]:grey[O3]:red[)], :red[heavy metals], and various :red[chemical compounds].")

st_lottie(load_lottie_file("animations/climate_change.json"))

st.write(":red[Pollution] is extremely harmful to the :green[environment], and everything that lives in it. From the :red[disease] that comes with breathing in the :red[polluted air] to the broader term of :red[climate change], pollution has extreme adverse effects on the :green[ecosystem], and ramififcations must be made before the changes become :red[irreversible].")
