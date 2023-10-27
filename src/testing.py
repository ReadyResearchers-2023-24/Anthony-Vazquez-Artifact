import streamlit as st
import pandas as pd
import numpy as np

data = 'data/emissions_global_1751_2019.csv'
headers = ['Year', 'Total carbon emissions from fossil fuel consumption and cement production (million metric tons of C)', 'Carbon emissions from solid fuel consumption', 'Carbon emissions from liquid fuel consumption', 'Carbon emissions from gas fuel consumption', 'Carbon emissions from cement production', 'Carbon emissions from gas flaring', 'Per capita carbon emissions (metric tons of carbon; after 1949 only)']

def csv_to_dict(file):
    new_dict = {}
    with open(file, 'r') as f:
        count = 0
        for line in f:
            counter = 0
            items = line.split(',')
            if count == 0:
                for thing in items:
                    new_dict = thing
                count += 1
                print(new_dict)
            else:
                for item in items:
                    new_dict[headers[counter]] = item
                counter += 1
    
    return new_dict

print(csv_to_dict(data))