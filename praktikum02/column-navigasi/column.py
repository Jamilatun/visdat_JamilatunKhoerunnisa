import streamlit as st

st.title("Column")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")

col1, col2, = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/gambar4.jpeg" )
col1.write("Ini adalah kolom kedua")
col1.image("../../praktikum01/assets/gambar2.jpeg" )