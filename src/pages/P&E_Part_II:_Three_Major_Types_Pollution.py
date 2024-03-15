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
st.write(':grey[Part II:] :orange[Three Major Types of Pollution]')
st.write(' ')
st.write(' ')

# Section for Air Pollution
st.header(':red[Air Pollution]')
st.header(' ',divider='red')
st.write('Air pollution is caused by the release of :red[pollutants] into the :green[atmosphere].')
st_lottie(load_lottie_file("animations/air.json"))
st.write('Sources of air pollution include :red[vehicle emissions], :red[industrial activities], :red[burning fossil fuels], and :red[large-scale agricultural practices].')
st.write('Pollutants can have :red[harmful effects] on :green[human health], including :red[respiratory issues], :red[cardiovascular diseases], and even :red[cancer].')
st.write('Air pollution also contributes to environmental problems like :red[acid rain], :red[ozone depletion], and :red[climate change].')
st.write(' ')
st.write(' ')

# Section for Water Pollution
st.header(':blue[Water Pollution]')
st.header(' ',divider='blue')
st.write('Water pollution occurs when :blue[contaminants] are discharged into bodies of water, such as :green[rivers], :green[lakes], :green[oceans], and :green[groundwater].')
st_lottie(load_lottie_file("animations/water.json"))
st.write('Sources of water pollution include :blue[industrial waste], :blue[agricultural runoff], :blue[sewage discharge], :blue[oil spills], and :blue[littering].')
st.write('Pollutants like :blue[heavy metals], :blue[pesticides], :blue[fertilizers], and :blue[plastics] can harm aquatic ecosystems, leading to the :blue[decline of fish populations], :blue[loss of biodiversity], and :blue[contamination of drinking water sources].')
st.write('Water pollution also poses :blue[health risks] to humans, causing diseases such as :blue[cholera], :blue[dysentery], and :blue[hepatitis], along with many others.')
st.write(' ')
st.write(' ')

# Section for Soil Pollution
st.header(':orange[Soil Pollution]')
st.header(' ',divider='orange')
st.write('Soil pollution refers to the presence of :orange[toxic chemicals], :orange[heavy metals], or other :orange[pollutants] in the :green[soil].')
st_lottie(load_lottie_file("animations/soil.json"))
st.write(':orange[Industrial activities], :orange[improper waste disposal], :orange[mining operations], and the use of :orange[pesticides and fertilizers] contribute to soil contamination.')
st.write('Contaminated soil can :orange[affect plant growth], :orange[reduce agricultural productivity], and :orange[pose risks to human health] through the consumption of :orange[contaminated food] or :orange[exposure to toxic substances].')
