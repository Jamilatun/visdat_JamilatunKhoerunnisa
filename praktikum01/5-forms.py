# membuat form
# text box
import streamlit as st
st.title("Text Box")
# creating text box
name = st.text_input("Enter your name")
st.write("you name is", name)

# Menampilkan Judul dan Deskripsi
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 2: Data Elements")

# text area
import streamlit as st
# creating text area
input_text = st.text_area("Enter your review")
# printing entered text
st.write(""" You entered \n""", input_text)

# number input
import streamlit as st
# create number input
st.number_input("Enter your number")

import streamlit as st
# create number input
num = st.number_input(" Enter your number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default value is 5, \n step size value is 2")
st.write("Total value after adding number enteres with step value is:", num)

# time
import streamlit as st
st.title("Time")
# definiting time function
st.time_input("Selet your time")

# date
# Input tanggal sederhana
import streamlit as st
st.title("Date")
# Defining Date Function
st.date_input("Select Date")

# Input tanggal dengan batas minimum, maksimum, dan nilai default
import streamlit as st
import datetime
st.title("Date")
# Defining Time Function
st.date_input(
    "Select Your Date",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)

# color
import streamlit as st

st.title("Select Color")

# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

# Dataset Upload
import streamlit as st
import pandas as pd

st.title("CSV Data")

# Upload CSV file
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file_size": data_file.size
        }
        st.write(file_details)

        # Membaca file CSV
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# Submit Button
import streamlit as st

my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)



