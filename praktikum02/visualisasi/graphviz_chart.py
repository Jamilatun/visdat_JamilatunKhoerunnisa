import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("graphviz chart")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")

st.graphviz_chart("""
    digraph{
     "Training Data" -> "ML Algorithm"
      "ML Algorithm" -> "Model"
      "Model" -> "Results Forecasting"
       "New Data" -> "Model"
    }                            
                     
""")

