import streamlit as st
from PIL import Image

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Spaced Out")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")

img = Image.open("../assets/gambar-contoh.jpg")
# Defining two Rows
for _ in range(2):
# Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)