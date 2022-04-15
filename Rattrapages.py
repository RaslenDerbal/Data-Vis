
#All the imports to do

import numpy as np
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
import os

#Opening and loading the data
@st.cache
def open_data():
    return pd.read_csv('C:\data_vis.csv')


#Settings of the visualisation
st.set_page_config(page_title="Data Visualisation Rattrapages", layout="centered", initial_sidebar_state="expanded")

#Open the data
agri = open_data()

st.write(agri)
