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

df=load_data('https://raw.githubusercontent.com/nghi97/FNEprojet/main/q1_q82%20(2).csv')

scoring = pd.DataFrame(columns = ['Nom.complet', "domaine_01", 
                                                 'domaine_02', 
                                                 'domaine_03', 
                                                 'domaine_04', 
                                                 'domaine_05'])

scoring['Nom.complet'] = df['r.Nom.complet']

#Domaine1
dom_01 = df.columns[np.r_[1:57]]
scoring["domaine_01"] = (df[dom_01].sum(axis=1) * 100 / 24.5).round(1)

# Domaine 2
dom_02 = df.columns[np.r_[57:104]]
scoring["domaine_02"] = (df[dom_02].sum(axis=1) * 100 / 18.5).round(1)

# Domaine 3
dom_03 = df.columns[np.r_[104:163]]
scoring['domaine_03'] = (df[dom_03].sum(axis=1) * 100 / 36).round(1)

# Domaine 4
dom_04 = df.columns[np.r_[163:181]]
scoring['domaine_04'] = (df[dom_04].sum(axis=1) * 100 / 18.75).round(1)

# Domaine 5
dom_05 = df.columns[np.r_[181:214]]
scoring['domaine_05'] = (df[dom_05].sum(axis=1) * 100 / 20.75).round(1)


#to list les repondants
repondants = scoring['Nom.complet'].tolist()



    
    
domaines = ["Littération de \nl'information et des données",
            'Communication \net collaboration', 
            'Création de contenu', 
            'Sécurité',
            'Environnement numérique \net résolution de problèmes']

# color for the slices and text
slice_colors = ["#1A78CF"] + ["#FF9300"] + ["#9A8C98"] + ["#78cf1a"] + ["#DA2C38"]
text_colors = ["#000000"] * 5


    
    
    

    
def plot(names):
    min_range = [0, 0, 0, 0, 0]
    max_range = [100, 100, 100, 100, 100]
    #for name in range(len(names)-1):
        #rep=scoring.loc[scoring['Nom.complet']==name,"domaine_01":"domaine_05"].values.tolist()[0]
    baker = PyPizza(
        params=domaines,           # list of parameters
        min_range=min_range,        # min range values
        max_range=max_range,        # max range values
        background_color="#EBEBE9",     # background color
        straight_line_color="#EBEBE9",  # color for straight lines
        straight_line_lw=1,             # linewidth for straight lines
        last_circle_lw=0,               # linewidth of last circle
        other_circle_lw=0,              # linewidth for other circles
        inner_circle_size=19.7          # size of inner circle
        
        )
    fig, ax = baker.make_pizza(
        scoring.loc[scoring['Nom.complet'].isin(names),"domaine_01":"domaine_05"].values.tolist()[0],
        figsize=(12, 13),                # adjust figsize according to your need
        color_blank_space="same",        # use same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=text_colors,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0.4,                 # alpha for blank-space colors
        kwargs_slices=dict(
        edgecolor="#F2F2F2", zorder=2, linewidth=1),    # values to be used when plotting slices
        kwargs_params=dict(color="#000000", fontsize=14, va="center"),   # values to be used when adding parameter
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
            0.515, 0.940, "Compétences numériques : {}".format(names), size=20,
            ha="center", color="#000000"
        )
    
    
    plt.show()
    
    
    
    
        
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
    Nomcomplet2=st.multiselect(label="Nom et Prénom",options=repondants, max_selections=1)
    #Nomcomplet= st.text_input(label="Nom et Prénom", placeholder="Par exemple: anonfirstname31 anonlastname31")
    st.write("") 
    
    

    
    
with col2:
    st.write("")
    st.write("")
    
    st.pyplot(plot(Nomcomplet2))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    
    st.write("")
    


    
    
