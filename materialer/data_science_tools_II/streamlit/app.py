import streamlit as st
import pandas as pd

df = pd.read_csv('../assets/worldcities.csv')


"---"

country = st.selectbox('Pick', df['city'].unique())
df[df['city'] == country]

"---"
filtered = df[df['city'] == country]


st.bar_chart(filtered.set_index('city')['population'])
st.line_chart(filtered.set_index('city')['population'])

