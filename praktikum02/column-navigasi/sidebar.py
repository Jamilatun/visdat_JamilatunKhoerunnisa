import streamlit as st

st.title("Praktikum 2 Visualisasi Data")
st.subheader("Sidebar")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")


# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)