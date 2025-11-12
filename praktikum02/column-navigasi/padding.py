import streamlit as st
from PIL import Image

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Padding")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")


img = Image.open("../../praktikum01/assets/gambar2.jpeg")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)