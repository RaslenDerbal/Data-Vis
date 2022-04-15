
#All the imports to do

import numpy as np
import streamlit as st 
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import time
import seaborn as sns
import os

#Opening and loading the data
@st.cache
def open_data(nrows):
    return pd.read_csv('data_vis.csv',nrows=nrows)


#Settings of the visualisation
st.set_page_config(page_title="Data Visualisation Rattrapages", layout="wide", initial_sidebar_state="expanded")

#Open the data
agri = open_data(50)
st.title('French agriculture vizualisation tool')
st.markdown("""Here is a simple visualization the data obtained on datagouv.fr """)


st.write(agri)
