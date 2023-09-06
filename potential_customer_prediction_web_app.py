# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:16:59 2023

@author: dell1
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('Model/trained_model.sav','rb'))
scaled = pickle.load(open('Model/trained_model_scaled.sav','rb'))


def potential_cus(input_data):
    input_data_array = np.asarray(input_data)
    input_data_scaled = scaled.transform(input_data_array)
    input_data_reshape = input_data_scaled.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
    if (prediction[0] == 1.):
        return 'The person has Loan on Card'
    else:
        return 'the person does not have loan on card'

def main():
    
    st.title('Potential Customer Prediction')
    st.header("Enter the value of the following parameters:")
    
    HighestSpend = st.number_input('Enter the value of Highest spend')
    MonthlyAverageSpend = st.number_input('Enter the value of monthly average spend')
    Mortgage = st.number_input('Enter the value of Mortgage')
    FixedDepositAccount= st.selectbox('Is the person have fixed deposit account with the bank', ('yes','No'))
    if FixedDepositAccount == 'yes':
        FixedDepositAccount = 1
    else:
        FixedDepositAccount=0
    HiddenScore_1= st.selectbox('Hidden score associated with the person is 1', ('yes','No'))
    if HiddenScore_1 == 'yes':
        HiddenScore_1 = 1
    else:
        HiddenScore_1=0
    HiddenScore_2= st.selectbox('Hidden score associated wit the person is 2', ('yes','No'))
    if HiddenScore_2 == 'yes':
        HiddenScore_2 = 1
    else:
        HiddenScore_2=0
    HiddenScore_3= st.selectbox('Hidden score associaegory ted wit the person is 3', ('yes','No'))
    if HiddenScore_3 == 'yes':
        HiddenScore_3 = 1
    else:
        HiddenScore_3=0
    HiddenScore_4= st.selectbox('Hidden score associated with the person is 4', ('yes','No'))
    if HiddenScore_4 == 'yes':
        HiddenScore_4 = 1
    else:
        HiddenScore_4=0
    Level_1= st.selectbox('Level associated with the person is 1', ('yes','No'))
    if Level_1 == 'yes':
        Level_1 = 1
    else:
        Level_1=0
    Level_2= st.selectbox('Level associated with the person is 2', ('yes','No'))
    if Level_2 == 'yes':
        Level_2 = 1
    else:
        Level_2=0
    Level_3= st.selectbox('Level associated with the person is 3', ('yes','No'))
    if Level_3 == 'yes':
        Level_3 = 1
    else:
        Level_3=0
    
    
    
    potential_customer = ' '
    
    if st.button('Predict Potential Customer'):
        potential_customer = potential_cus([[HighestSpend,MonthlyAverageSpend,Mortgage,FixedDepositAccount,HiddenScore_1,HiddenScore_2,HiddenScore_3,HiddenScore_4,Level_1,Level_2,Level_3]])
    st.success(potential_customer)
    
if __name__ == '__main__':
    main()

    