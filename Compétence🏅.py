# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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



def load_data(database):
    df=pd.read_csv(database,encoding='cp1252')
    return df

df=load_data('C:\\Users\\ndgng\\Downloads\\q1_q82.csv')

scoring = pd.DataFrame(columns = ['Nom.complet', 'dom_01_CO', 'dom_01_CU', 'dom_02_CO', 'dom_02_CU', 'dom_03_CO', 'dom_03_CU',
                                         'dom_04_CO', 'dom_04_CU', 'dom_05_CO', 'dom_05_CU'])

scoring['Nom.complet'] = df['r.Nom.complet']

#Domaine1
dom_01_co = df.columns[np.r_[15:23,24,27:35,39:47]]
scoring['dom_01_CO'] = df[dom_01_co].sum(axis=1).round(1)

dom_01_cu = df.columns[np.r_[1:15,23,25:27,35:39]]
scoring['dom_01_CU'] = df[dom_01_cu].sum(axis=1).round(1)
# Domaine 2
dom_02_co = df.columns[np.r_[47:52,58:63]]
scoring['dom_02_CO'] = df[dom_02_co].sum(axis=1).round(1)

dom_02_cu = df.columns[np.r_[52:58,63:81]]
scoring['dom_02_CU'] = df[dom_02_cu].sum(axis=1).round(1)

# Domaine 3
dom_03_co = df.columns[np.r_[86:125,129:132]]
scoring['dom_03_CO'] = df[dom_03_co].sum(axis=1).round(1)

dom_03_cu = df.columns[np.r_[81:86,125:129]]
scoring['dom_03_CU'] = df[dom_03_cu].sum(axis=1).round(1)

# Domaine 4
dom_04_co = df.columns[np.r_[132:137,140,143:146,149:153]]
scoring['dom_04_CO'] = df[dom_04_co].sum(axis=1).round(1)

dom_04_cu = df.columns[np.r_[137:140,141:143,146:149]] 
scoring['dom_04_CU'] = df[dom_04_cu].sum(axis=1).round(1)

# Domaine 5
dom_05_co = df.columns[np.r_[153:170,180:183]]
scoring['dom_05_CO'] = df[dom_05_co].sum(axis=1).round(1)

dom_05_cu = df.columns[np.r_[170:180]]
scoring['dom_05_CU'] = df[dom_05_cu].sum(axis=1).round(1)


#to list les étudiants
etudiants = scoring['Nom.complet'].tolist()



    
    
sous_domaines = ["Culture numérique", "Compétences numérique",
                 "Culture numérique", "Compétences numérique",
                 "Culture numérique", "Compétences numérique",
                 "Culture numérique", "Compétences numérique",
                 "Culture numérique", "Compétences numérique"]

# color for the slices and text
slice_colors = ["#1A78CF"] * 2 + ["#FF9300"] * 2  + ["#9A8C98"] * 2 + ["#78cf1a"] * 2 + ["#DA2C38"] * 2
text_colors = ["#000000"] * 10


    
    
    

    
def plot(name):
    
    baker = PyPizza(
        params=sous_domaines,           # list of parameters
        background_color="#EBEBE9",     # background color
        straight_line_color="#EBEBE9",  # color for straight lines
        straight_line_lw=1,             # linewidth for straight lines
        last_circle_lw=0,               # linewidth of last circle
        other_circle_lw=0,              # linewidth for other circles
        inner_circle_size=19.7          # size of inner circle
    )
    fig, ax = baker.make_pizza(
        scoring.loc[scoring['Nom.complet'] == name, 'dom_01_CO':'dom_05_CU'].values.tolist()[0],
        figsize=(12, 13),                # adjust figsize according to your need
        color_blank_space="same",        # use same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=text_colors,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0.4,                 # alpha for blank-space colors
        kwargs_slices=dict(
        edgecolor="#F2F2F2", zorder=2, linewidth=1),    # values to be used when plotting slices
        kwargs_params=dict(color="#000000", fontsize=12, va="center"),   # values to be used when adding parameter
        kwargs_values=dict(
            color="#000000", fontsize=11,
            zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        )                                # values to be used when adding parameter-values
    )
    # add title
    fig.text(
        0.515, 0.975, "Compétences numériques : {}".format(name), size=20,
        ha="center", color="#000000"
    )
    
    # add text
    fig.text(
    0.515, 0.940, "Littération de l'information et des données          Communication et collaboration", size=14,
    ha="center", color="#000000"
    )
    fig.text(
    0.515, 0.905, "Création de contenu         Sécurité         Environnement numérique et résolution de problèmes", size=14,
    ha="center", color="#000000"
    )

    # add rectangles
    fig.patches.extend([
    plt.Rectangle(
        (0.154, 0.935), 0.025, 0.021, fill=True, color="#1A78CF",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.550, 0.935), 0.025, 0.021, fill=True, color="#FF9300",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.101, 0.900), 0.025, 0.021, fill=True, color="#9A8C98",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.310, 0.900), 0.025, 0.021, fill=True, color="#78cf1a",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.425, 0.900), 0.025, 0.021, fill=True, color="#D70232",
        transform=fig.transFigure, figure=fig
    ),
    ])
    
  
    
    plt.show()
    
    
    
bdd=pd.read_excel("C://Users//ndgng//Downloads//RADAR-1.xlsm","Notes Traitées",index_col=False)
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
    plot=go.Figure(go.Indicator(mode = "gauge+number",value = bdd_nonmoyglobal.loc[x][y],domain = {'x': [0, 0.5], 'y': [0, 0.5]},
                title = {'text': x+": "+ y, 'font': {'size': 10}},
               gauge={'bar':{'color':'red'},
                     'axis':{'range':[None,2.22]}}))
    
    plot.show()
        
domain=["Domaine 1","Domaine 5"]       
        
st.title("Approfondissement des visualisations des Digitales Compétence")
st.sidebar.markdown("# Compétence :sports_medal:")

st.write("Pour cet approfondissement de la visualisation, nous vous proposons premièrement un graphique permettant une vue d’ensemble des notes des professeurs dans les cinq domaines du questionnaire. En suivant les recommandations du commanditaire nous avons divisé les questions en deux types : celles relevant de la culture, et les autres relevant de la compétence. Nous rappelons ici l’ordre des domaines du référentiel DigComp, dont un récapitulatif se trouve dans les annexes :")
st.write("1. Littératie de l'information et des données")
st.write("2. Communication et collaboration")
st.write("3. Création de contenus")
st.write("4. Sécurité")
st.write("5. Environnement numérique et résolution de problèmes")
st.write("")
st.write("")
cole, col1, cole, col2, cole = st.columns([0.1, 1, 0.05, 1, 0.1])

with col1:
    MetricSlider01 = st.selectbox("Choisir l'individu", etudiants)
    


    st.write("") 
    
    

    
    
with col2:
    st.pyplot(plot(MetricSlider01))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    
    st.write("")
    


    
    
