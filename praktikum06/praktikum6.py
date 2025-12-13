# import 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# header
st.title("Praktikum 06 visualisasi data")
st.write("Kelompok: 2")
st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim Rifai - 0110122068
""")

# dataset
stores = ['stores A'], ['stores B', 'stores c']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [120, 230, 170]

# data quarter 
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1 grafik stacked vertical bar chart

st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, bottom=male, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 2 grafik stacked vertical bar chart

st.subheader("2. Stacked Vertical Bar Chart dengan matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='product B', color='green')

ax.set_title('Sales Transaction by store')
ax.set_xlabel('Stores')
ax.set_ylabel('sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3 grafik kustomisasi stacked vertical bar chart
st.subheader ("3. Kustomisasi Stacked Vertical Bar chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

# 4 grafik multiple stacked vertical bar chart
st.subheader("4. multiple stacked vertical bar chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# quarter 1
ax.bar(x-width/2, q1_male, label='Q1 male', color='lightblue', width=width)
ax.bar(x-width/2, q1_female, bottom=q1_male, label='Q1 female', color='pink', width=width)

# quarter 2
ax.bar(x+width/2, q2_male, label='Q2 male', color='blue', width=width)
ax.bar(x+width/2, q2_female, bottom=q2_male, label='Q2 female', color='red', width=width)


ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)
