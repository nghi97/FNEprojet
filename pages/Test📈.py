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
    
def jauge(x):
    D1=go.Indicator(mode = "gauge+number",value = bdd_nonmoyglobal.loc[x]['Domaine 1'],domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Domaine 1", 'font': {'size': 10}},
               gauge={'bar':{'color':'red'},
                     'axis':{'range':[None,2.22]}})
    D5=go.Indicator(mode = "gauge+number",value = bdd_nonmoyglobal.loc[x]['Domaine 5'],domain = {'x': [0, 1], 'y': [0, 1]},
               title = {'text': "Domaine 5", 'font': {'size': 10}},
                gauge={'bar':{'color':'green'},
                       'axis':{'range':[None,2.22]}})
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{'type' : 'indicator'}, {'type' : 'indicator'}]],x_title=x
        )
    fig.append_trace(D1, row=1, col=1)
    fig.append_trace(D5, row=1, col=2)
    fig.update_layout(height=200, width=300)
    fig.show()
    
    
def jauge1(x,y):
    plot=go.Figure(go.Indicator(mode = "gauge+number",value = bdd_nonmoyglobal.loc[x][y],domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': x+": "+ y, 'font': {'size': 25}},
               gauge={'bar':{'color':'red'},
                     'axis':{'range':[None,2.22]}}))
    
    plot.show()
        
domain=["Domaine 1","Domaine 5"]       
st.sidebar.markdown("# Test :chart_with_upwards_trend:")       
st.title(" Test")


cole, col1, cole, col2, cole = st.columns([0.1, 1, 0.05, 1, 0.1])


    
    

    

    
MetricSlider02 = st.selectbox("Choisir l'individu", list_index)
MetricSlider03 = st.selectbox("Domaine", domain)
if st.button('Regarder le graphique'):
    fig=go.Figure(go.Indicator(mode = "gauge+number",value = bdd_nonmoyglobal.loc[MetricSlider02][MetricSlider03],domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text':MetricSlider02 +": "+ MetricSlider03, 'font': {'size': 25}},
               gauge={'bar':{'color':'red'},
                     'axis':{'range':[None,2.22]}}))
    st.pyplot(fig.show())
    st.set_option('deprecation.showPyplotGlobalUse', False)
