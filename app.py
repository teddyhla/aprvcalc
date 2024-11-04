#Streamlit app
# LC
# TH
####

import streamlit as st

st.markdown('# APRV Settings Calculator')

st.sidebar.title('Input variables')
st.sidebar.caption('In Development by Teddy Hla for Professor Luigi Camporota')

with st.sidebar:
    
    pplat = st.number_input(
        
        'Please insert **Plateau pressure** in cmH20:', value=25, placeholder = 'Type your plateau pressure',
        help='Perform inspiratory hold to measure plateau pressure'
    )
    
    rr = st.number_input(
        
        'Please insert **respiratory rate** per minute:', value=16, placeholder = 'Type your resp rate',
        help='This is the effective respiratory rate'
    )
    
    tv = st.number_input(
        
        'Please insert **tidal volumes** in mililitres:', value=500, placeholder = 'Type your tidal volume',
        help = 'This is the inspired tidal volume'
    )
    
    co2_actual = st.number_input(
        
        'Please insert **PaCO2 measured** in kPa:', value=8.0, placeholder = 'Type your PaCO2'
    )
    
    co2_desired = st.number_input(
        'Please insert **PaCO2 desired**',value=7.0, placeholder = 'Type your desired PaCO2'
    )
    
    pef = st.number_input(
        'Please input your peak expiratory flow ', value=80, placeholder = 'Type your Peak Expiratory Flow',
        help= 'How to measure peak expiratory flow'
    )
    
    actual_pef = st.number_input(
        'Please input your actual peak expiratory flow', value = 70, placeholder = 'Type your Actual PEF'
    )


# Calculations


ttot = 60/rr 
mv = (tv/1000) * rr 
mvc = (co2_actual/co2_desired)*mv
rrnew = mvc / (tv/1000)
plow = 0
tlowi = 0.5
thigh = (60/rrnew) - tlowi
target_tef = pef * 0.75 

def sf(x):
    x = float(f"{x:.3g}")
    return x

st.write('The current minute ventilation in litres is:',sf(mv))
st.write('The current time in each breath Ttot in seconds is', sf(ttot))
st.write('The new minute volume for desired CO2 in litres is', sf(mvc))
st.write('The new respiratory rate for desired CO2 per minute is', sf(rrnew))

st.title('APRV Recommended Settings')
st.write('Phigh in cmH20 is:',pplat)
st.write('Plow in cmH20:',plow)
st.write('Tlow(i) in seconds is',tlowi)
st.write('Thigh in seconds is',thigh)