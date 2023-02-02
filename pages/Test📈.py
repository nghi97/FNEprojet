# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:53:38 2023

@author: ndgng
"""
import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns
from mplsoccer import PyPizza, add_image
import plotly.graph_objects as go
from plotly.subplots import make_subplots


bdd=pd.read_csv("https://raw.githubusercontent.com/nghi97/FNEprojet/main/RADAR-1.csv",index_col=False)
bdd_nonmoyglobal=bdd.drop(bdd.index[-1],axis=0)
bdd_nonmoyglobal=bdd_nonmoyglobal.drop(['Nom'],axis=1)
list_index=bdd_nonmoyglobal['Prénom'].tolist()
bdd_nonmoyglobal=bdd_nonmoyglobal.drop(['Prénom'],axis=1)
c=pd.Series(list_index)
bdd_nonmoyglobal=bdd_nonmoyglobal.set_index(c)
    
domain=["Domaine 1","Domaine 5"]



    

    
MetricSlider02 = st.selectbox("Choisir l'individu", list_index)
MetricSlider03 = st.selectbox("Domaine", domain)
if st.button('Regarder le graphique'):
    fig=go.Figure(go.Indicator(mode = "gauge+number+delta",value = bdd_nonmoyglobal.loc[MetricSlider02][MetricSlider03],domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text':MetricSlider02 +": "+ MetricSlider03, 'font': {'size': 25}},
                delta = {'reference': bdd.loc[3][MetricSlider03]},
               gauge={'bar':{'color':'red'},
                     'axis':{'range':[None,2.22]}}))
    st.plotly_chart(fig, use_container_width=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
