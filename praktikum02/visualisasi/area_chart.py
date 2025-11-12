import streamlit as st
import pandas as pd
import numpy as np

st.title("Area chart")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)

