import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='prediction of disease outbreaks',
                   layout = 'wide',
                   page_icon='doctor')
diabetes_model  = pickle.load(open(r"C:\Users\aiden\OneDrive\Desktop\DOP\training models\diabetes_model.sav",'rb'))                   
heart_model = pickle.load(open(r"C:\Users\aiden\OneDrive\Desktop\DOP\training models\heart_model.sav",'rb'))
parkisons_model = pickle.load(open(r"C:\Users\aiden\OneDrive\Desktop\DOP\training models\parkinons_model.sav",'rb'))

with st.sidebar:
    selected = option_menu("Prediction of disease outbreak system",['diabetes prediction' , 'heart disease prediction' , 'parkinsons prediction'],
                           menu_icon='hospital-fill' , icons = ['activity', 'heart','person'],default_index=0)

if selected == 'diabetes prediction' :
    st.title('diabetes prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies= st.text_input("number of pregnancies")
    with col2:
        Glucose = st.text_input("glucose level")        
    with col3:
        bloodpressure = st.text_input("blood pressure value")    
    with col1:
        skinthickness = st.text_input("skin thickness value")    
    with col2:
        insulin = st.text_input('insulin level')    
    with col3:
        BMI = st.text_input("BMI measured")    
    with col1:
        diabetespedigreefunction = st.text_input("Diabetes pedigree function")    
    with col2:
        age = st.text_input ("Age of the person")    

    diab_diagnosis = ''
    if st.button('diabetes test result'):
     user_input= [pregnancies , Glucose,bloodpressure,  skinthickness, insulin,BMI,diabetespedigreefunction,age]
     user_input = [float(x) for x in user_input]
     diab_prediction = diabetes_model.predict([user_input])
     if diab_prediction[0]== 1:
        diab_diagnosis='the person is diabetic'
     else:
        diab_diagnosis='the person is non diabetic'    
    st.success(diab_diagnosis)    

if selected == 'heart disease prediction' :
    st.title('heart disease prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        cholestrol= st.text_input("cholestrol")
    with col2:
        ca = st.text_input("ca")        
    with col3:
        thal = st.text_input("thal")    
    with col1:
        oldpeak = st.text_input("oldpeak")    
    with col2:
        trestbps = st.text_input('trestbpl')    
    with col3:
        restecg = st.text_input("restecg")    
    with col1:
        thalach = st.text_input("thalach")    
    with col2:
        age = st.text_input ("Age of the person")    

    heart_diagnosis = ''
    if st.button('heart disease test result'):
     user_input= [cholestrol , ca, thal,oldpeak, trestbps,restecg,thalach,age]
     user_input = [float(x) for x in user_input]
     heart_prediction = heart_model.predict([user_input])
     if heart_prediction[0]== 1:
        heart_diagnosis='the person is patient'
     else:
        heart_diagnosis='the person is non heart patient'    
    st.success(heart_diagnosis)    

if selected == 'parkinsons prediction' :
    st.title('parkinsons disease prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        MDVPFo= st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVPFhi = st.text_input("MDVP:Fhi(Hz)")        
    with col3:
        MDVPFlo = st.text_input("MDVP:Flo(Hz)")    
    with col1:
        MDVPJitter = st.text_input("MDVP:Jitter(%)")    
    with col2:
        MDVPAbs = st.text_input('Abs')    
    with col3:
        MDVPRAP = st.text_input("MDVP:RAP")    
    with col1:
        MDVPPPQ = st.text_input("MDVP:PPQ")    
    with col2:
        HNR = st.text_input ("AHNR")    

    parkinsons_diagnosis = ''
    if st.button('parkinsons disease test result'):
     user_input= [MDVPFo ,MDVPFhi,MDVPFlo,MDVPJitter,MDVPAbs,MDVPRAP,MDVPPPQ,HNR]
     user_input = [float(x) for x in user_input]
     parkinsons_prediction = parkisons_model.predict([user_input])
     if parkinsons_prediction[0]== 1:
        parkinsons_diagnosis='the person is parkninson patient'
     else:
        parkinsons_diagnosis='the person is non parkinson patient'    
    st.success(parkinsons_diagnosis)    