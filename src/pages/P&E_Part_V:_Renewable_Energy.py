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
st.write(':grey[Part V:] :orange[Renewable Energy: The Future We Need]')
st.write(' ')
st.write(' ')