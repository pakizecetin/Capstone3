import streamlit as st
import pickle
import pandas as pd
import sklearn
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from PIL import Image
import base64
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.image("fraud.png", use_column_width=True)
html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Fraud Detection </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.sidebar.image("fraud.png", use_column_width=True)
st.markdown(html_temp,unsafe_allow_html=True)


V17 = st.sidebar.slider(label="V17", min_value=-35,
                        max_value=15, step=0.01)
V14 = st.sidebar.slider(label="V14", min_value=-25, max_value=15, step=1)
V10 = st.sidebar.slider(label="V10", min_value=-30, max_value=30, step=1)
V12 = st.sidebar.slider(label="V12", min_value=-25,
                        max_value=15, step=0.1)
V27 = st.sidebar.slider(label="V27", min_value=-25,
                        max_value=35, step=1)
V7 = st.sidebar.slider(label="V7", min_value=-45, max_value=125, step=1)
V4 = st.sidebar.slider(label="V4", min_value=-7, max_value=20, step=1)
V2 = st.sidebar.slider(label="V2",
                       min_value=-75, max_value=25, step=1)

capstone_3_model = pickle.load(open('xgb_model_final', 'rb'))

scalerfile = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))

my_dict = {'V17':V17, 
	   'V14':V14, 
	   'V10':V10, 
	   'V12':V12,
	   'V27':V27,
	   'V7':V7,
	   'V4':V4,
	   'V2':V2
	   }

df = pd.DataFrame.from_dict([my_dict])

user_inputs = df



prediction = capstone_3_model.predict(user_inputs)


st.header("The inputs are below")
st.table(df)

st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	if prediction[0]==0:
		st.success(prediction[0])
		st.success(f'This transaction is not fraudulent. :)')
	elif prediction[0]==1:
		st.warning(prediction[0])
		st.warning(f'This transaction is fraudulent. :(')
    
