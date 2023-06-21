import numpy as np
import pandas as pd
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import catboost

agri_pro_model = pickle.load(open('pipe.pkl','rb'))

with st.sidebar:
    
    selected = option_menu('Andhra Pradesh Crop Yield Prediction',
                          
                          ['Andhra Pradesh Crop Yield Prediction'],
                          icons=['Ear of Corn'],
                          default_index=0)
    

if(selected =='Andhra Pradesh Crop Yield Prediction' ):
    st.title('Andhra Pradesh Crop Yield Prediction')
    
    districts = {
    "ANANTAPUR": 0,
    "EAST GODAVARI": 1,
    "KRISHNA": 2,
    "VIZIANAGARAM": 3,
    "WEST GODAVARI": 4,
    "CHITTOOR": 5,
    "GUNTUR": 6,
    "KADAPA": 7,
    "KURNOOL": 8,
    "PRAKASAM": 9,
    "SPSR NELLORE": 10,
    "SRIKAKULAM": 11,
    "VISAKHAPATANAM": 12
    }

    season = {
        "Kharif (June to November)": 1,
        "Rabi (November-May)": 2,
        "Whole Year" : 3
    }


    crop = {
        'Arhar/Tur' : 0,
        'Bajra':1,
        'Castor seed':2,
        'Cotton(lint)':3,
        'Dry chillies':4,
        'Groundnut':5,
        'Horse-gram':6,
        'Jowar':7,
        'Korra':8,
        'Maize':9,
        'Moong(Green Gram)':10,
        'Other Kharif pulses':11,
        'Ragi':12,
        'Rice':13,
        'Sugarcane':14,
        'Sunflower':15,
        'Tobacco':16,
        'Gram':17, 'Wheat':18,
        'Masoor':19, 'Sesamum':20, 'Urad':21, 'Linseed':22, 'Safflower':23, 'Onion':24,
        'other misc. pulses':25, 'Samai':26, 'Small millets':27, 'Arecanut':28,
        'Banana':29, 'Coconut ':30, 'Coriander':31, 'Potato':32, 'Sweet potato':33,
        'Turmeric':34, 'Other  Rabi pulses':35, 'Soyabean':36,
        'Beans & Mutter(Vegetable)':37, 'Bhindi':38, 'Brinjal':39, 'Citrus Fruit':40,
        'Cucumber':41, 'Grapes':42, 'Mango':43, 'Orange':44, 'other fibres':45,
        'Other Fresh Fruits':46, 'Other Vegetables':47, 'Papaya':48, 'Pome Fruit':49,
        'Tomato':50, 'Mesta':51, 'Cowpea(Lobia)':52, 'other oilseeds':53, 'Lemon':54,
        'Pome Granet':55, 'Sapota':56, 'Cabbage':57, 'Cashewnut':58,
        'Rapeseed &Mustard':59, 'Tapioca':60, 'Peas  (vegetable)':61, 'Niger seed':62,
        'Bottle Gourd':63, 'Dry ginger':64, 'Varagu':65, 'Garlic':66, 'Ginger':67
    }
    

    selected_district = st.selectbox("Select District", list(districts.keys()))
    selected_district_value = districts[selected_district]
    st.write("Selected District Value:", selected_district_value)

    selected_season = st.selectbox("Select Crop Season", list(season.keys()))
    selected_season_value = season[selected_season]
    st.write("Selected Crop Season Value:", selected_season_value)

    selected_crop = st.selectbox("Select Crop", list(crop.keys()))
    selected_crop_value = crop[selected_crop]
    st.write("Selected Crop Value:", selected_crop_value)

    year= {
        1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026
    }


    year = st.selectbox('Enter Year of Crop Growth',list(year))

    area = st.number_input('Enter Area of Crop Growth in Hectacres',0,100000)


    Prediction=''

    if st.button('Test Yield in Tons'):
        Prediction = agri_pro_model.predict([[selected_district_value,year,selected_season_value,selected_crop_value,area]])


    st.success(Prediction)
