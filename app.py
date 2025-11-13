import streamlit as st

st.title("Meu primeiro app 🌹")

st.header ('Vamos fazer algo com interatividade')

n = st.number_imput('Entre com um número')

st.write(f'O numero que você escolheu ao quadrado é {n**2}')