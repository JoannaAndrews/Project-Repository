# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:45:16 2024

@author: Owner
"""

import numpy as np
import pickle
import streamlit as st
import cv2

# #Your Code Here
# #File Input
# import streamlit as st

# loading the saved model


loaded_model = pickle.load(open('C:/Users/Owner/Pictures/face_model.sav', 'rb'))

uploaded_file = st.file_uploader("Upload File")
if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #image = cv2.imdecode(file_bytes, 1)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    st.image(image, channels="BGR", caption='Your Image')

    small = cv2.resize(image, (50,50) ) #YOUR CODE HERE: specify image, dimensions
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

    flattened_image = np.reshape(gray, (1,2500))
    #result = (loaded_model[8]) #loaded_model[1](flattened_image)
    



    #loaded_model[0].predict(flattened_image)
    

     # if result == 0:
     #   st.write("No malaria")
     # elif result == 1:
    #st.write(result)
else:
    pass