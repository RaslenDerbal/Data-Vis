
#All the imports to do

import numpy as np
import streamlit as st 
import pandas as pd
import plotly.figure_factory as ff
import matplotlib
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



#Plot the data in multiple forms

#Adding the filters on thhe dataset
st.sidebar.header('Choose what to show')
categories = agri['GRP CULTU'].unique().tolist
categories_choosed = st.sidebar.multiselect('Culture Categories', categories, categories)
