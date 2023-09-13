import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('model.pkl','rb'))
df = pickle.load(open('data.pkl','rb'))

st.title("Rice Type Classification")

#Area
Area = st.number_input('Enter Area (value between 2500 to 10250) : ')

#MajorAxisLength
MajorAxisLength = st.number_input('Enter MajorAxisLength (value between 70 to 185) : ')

#MinorAxisLength
MinorAxisLength = st.number_input('Enter MinorAxisLength (value between 30 to 85) : ')

#Eccentricity
Eccentricity = st.number_input('Enter Eccentricity (value between 0 to 1) : ')

#ConvexArea
ConvexArea = st.number_input('Enter ConvexArea (value between 2500 to 1150) : ')

#EquivDiameter
EquivDiameter = st.number_input('Enter EquivDiameter (value between 50 to 120) : ')

#Extent
Extent = st.number_input('Enter Extent (value between 0 to 1) : ')

#Perimeter
Perimeter = st.number_input('Enter Extent (value between 190 to 510) : ')

#Roundness
Roundness = st.number_input('Enter Roundness (value between 0 to 1) : ')

#AspectRation
AspectRation = st.number_input('Enter AspectRation (value between 0 to 5) : ')

if st.button('Classify Rice'):
	query =np.array([Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation])
	query = query.reshape(1,10)
	pred = int(np.exp(model.predict(query)[0]))
	if pred == 1:
		st.title("The predicted class of this rice is JASMINE")
	else:
		st.title("The predicted class of this rice is GONEN")
    

