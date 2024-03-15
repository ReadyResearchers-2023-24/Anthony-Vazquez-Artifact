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
st.write(':grey[Part III:] :orange[What IS Energy?]')
st.write(' ')
st.write(' ')

st.header(':orange[Energy] is a fundamental concept in physics and refers to the ability to work :green[work] or produce :green[change].')
st.header(' ',divider='grey')
st.write(' ')

# Section for Renewable and Non-Renewable energy
st.write('There are two major sources for energy that we know of: :green[renewable energy] and :red[non-renewable energy].')
st.write(':green[Renewable energy] is derived from natural resources that are :green[replenished] over time, such as :green[sunlight(]:grey[solar energy]:green[)], :green[wind(]:grey[wind turbines]:green[)], :green[water(]:grey[hydropower]:green[)], :green[biomass(]:grey[carbon-based organisms]:green[)], and :green[geothermal heat(]:grey[volcanoes & geothermal vents]:green[)].')
st.write(':red[Non-renewable energy] is derived from finite resources that are :red[not replenished] on a human timescale, including :red[fossil fuels(]:grey[coal, oil, natural gas]:red[)] and :red[nuclear energy(]:grey[from radioactive materials]:red[)].')
st.header(' ',divider='grey')

# Section for Kinetic Energy
st.write('It exists in various forms, including :orange[kinetic energy(]:grey[energy of motion]:orange[)];')
st_lottie(load_lottie_file("animations/kinetic.json"))
st.write(":orange[Kinetic energy] is the energy possessed by an object due to its :orange[motion]. It is one of the fundamental forms of :orange[energy] and is directly related to the object's :orange[mass] and :orange[velocity].")
st.header(' ',divider='orange')
st.write(' ')
st.write(' ')

# Section for Potential Energy
st.write(':orange[potential energy(]:grey[stored energy]:orange[)];')
st_lottie(load_lottie_file("animations/potential.json"))
st.write(":orange[Potential energy] is the energy stored in an object due to its :orange[position] or :orange[configuration]. Unlike kinetic energy, which is associated with motion, :orange[potential energy] is associated with the :orange[potential] to do :orange[work] or cause a :orange[change].")
st.write("There are several types of potential energy, including :orange[gravitational] potential energy, :orange[elastic] potential energy, :orange[chemical] potential energy, and :orange[electrical] potential energy.")
st.header(' ',divider='orange')
st.write(' ')
st.write(' ')

# Section for Thermal Energy
st.write(':red[thermal energy(]:grey[heat]:red[)];')
st_lottie(load_lottie_file("animations/thermal.json"))
st.write(":red[Thermal energy], also known as heat energy, is the :red[energy] that comes from the vibrations and movements of :red[atoms] and :red[molecules] within a substance.")
st.write("It is a form of :red[kinetic energy] associated with the random :red[motion] of :red[particles] at the microscopic level, most commonly associated with :red[fire] as the most recognizeable form of this :red[energy]. Thermal energy determines the temperature of a substance and is transferred between objects through mechanisms such as :red[conduction], :red[convection], and :red[radiation].")
st.header(' ',divider='red')
st.write(' ')
st.write(' ')

# Section for Chemical Energy
st.write(':green[chemical energy(]:grey[energy stored in chemical bonds]:green[)];')
st_lottie(load_lottie_file("animations/chemical.json"))
st.write(":green[Chemical energy] is a form of :green[potential energy] stored within the :green[chemical bonds] of molecules. It is :green[released] or :green[absorbed] during :green[chemical reactions] when bonds are :green[broken] or :green[formed].")
st.write(":green[Chemical energy] is one of the most prevalent forms of :green[energy] and is essential for sustaining life and powering various :green[natural] and :green[technological] processes.")
st.header(' ',divider='green')
st.write(' ')
st.write(' ')

# Section for Electrical Energy
st.write('and :orange[electrical energy(]:grey[energy associated with electric charges]:orange[)].')
st_lottie(load_lottie_file("animations/electrical.json"))
st.write(":orange[Electrical energy] is a form of :orange[energy] associated with the :orange[movement] of :orange[electric charges]. It is a type of :orange[kinetic energy] transferred through :orange[electrical circuits] and used to power various :orange[devices] and :orange[systems].")
st.write(":orange[Electrical energy] is generated from various sources and plays a crucial role in modern society for :orange[lighting], :orange[heating], :orange[transportation], :orange[communication], and :orange[industrial processes].")
st.header(' ',divider='orange')
