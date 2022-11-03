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


V17 = st.sidebar.slider(label="V17", min_value=-35.00, max_value=15.00, step=0.01)
V14 = st.sidebar.slider(label="V14", min_value=-25.00, max_value=15.00, step=0.01)
V10 = st.sidebar.slider(label="V10", min_value=-30.00, max_value=30.00, step=0.01)
V12 = st.sidebar.slider(label="V12", min_value=-25.00, max_value=15.00, step=0.01)
V27 = st.sidebar.slider(label="V27", min_value=-25.00, max_value=35.00, step=0.01)
V7 = st.sidebar.slider(label="V7", min_value=-45.00, max_value=125.00, step=0.01)
V4 = st.sidebar.slider(label="V4", min_value=-7.00, max_value=20.00, step=0.01)
V2 = st.sidebar.slider(label="V2", min_value=-75.00, max_value=25.00, step=0.01)

capstone_3_model = pickle.load(open('xgb_model_final', 'rb'))

my_dict = {'V1': 1, 'V2': 1, 'V3': 1, 'V4': 1, 'V5': 1, 'V6': 1, 'V7': 1, 'V8': 1, 'V9': 1, 'V10': 1, 'V11': 1,
           'V12': 1, 'V13': 1, 'V14': 1, 'V15': 1, 'V16': 1, 'V17': 1, 'V18': 1, 'V19': 1, 'V20': 1, 'V21': 1,
           'V22': 1, 'V23': 1, 'V24': 1, 'V25': 1, 'V26': 1, 'V27': 1, 'V28': 1, 'Amount': 1
	   }

df = pd.DataFrame.from_dict([my_dict])

user_inputs = df



prediction = capstone_3_model.predict(user_inputs)




st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	if prediction[0]==0:
		st.success(prediction[0])
		st.success(f'This transaction is not fraudulent. :)')
	elif prediction[0]==1:
		st.warning(prediction[0])
		st.warning(f'This transaction is fraudulent. :(')
    
