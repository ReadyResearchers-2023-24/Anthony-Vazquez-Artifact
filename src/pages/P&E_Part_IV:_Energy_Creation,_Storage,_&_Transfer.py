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
st.write(':grey[Part IV:] :orange[How is Energy Created, Stored, and Transferred?]')
st.write(' ')
st.write(' ')

st.write(":orange[Energy] can neither be :blue[created] nor :blue[destroyed], only :blue[converted] between different forms, so we really cant 'make' :orange[energy]. However, being able to :blue[convert] :orange[energy] into different forms proves to be very useful to our technology today, and there are many ways that it can be :blue[converted].")
st.write("The different ways that we can convert :orange[energy] from one form to another are: :blue[chemical reactions], :blue[nuclear reactions], :blue[mechanical processes], :blue[thermal processes], :blue[geothermal energy], and :blue[renewable resources]")
