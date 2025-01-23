import streamlit as st


from jamb import data_pel, grouped_data 


st.title('Welcome to Ode Remo')

st.bar_chart(data_pel)

st.bar_chart(grouped_data)