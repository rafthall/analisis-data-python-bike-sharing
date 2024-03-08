import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analisis Bike Sharing :sparkles:')
st.header('By Rafi Athallah Kurniawan')

# Load datasets
df_day = pd.read_csv('day.csv')
pd_hour = pd.read_csv('hour.csv')

datetime_columns = ["dteday"]

for column in datetime_columns:
    df_day[column] = pd.to_datetime(df_day[column])

df_day['mnth'] = df_day['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
df_day['season'] = df_day['season'].map({
    1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
df_day['weekday'] = df_day['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
df_day['weathersit'] = df_day['weathersit'].map({
    1: 'Clear etc',
    2: 'Mist etc',
    3: 'Light Snow etc',
    4: 'Heavy Rain etc'
})

st.subheader('EDA for day.csv')
# Visualisasi distribusi variabel target (cnt)
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(data=df_day , x='cnt', bins=30, kde=True)
plt.title('Distribution of Bike Rentals (cnt) in day.csv')
plt.xlabel('Count of Bike Rentals')
plt.ylabel('Frequency')
st.pyplot(fig)

# Visualisasi korelasi antar variabel
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(df_day.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for day.csv')
st.pyplot(fig)

st.subheader('EDA for hour.csv')
# Visualisasi distribusi variabel target (cnt)
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(data=pd_hour, x='cnt', bins=30, kde=True)
plt.title('Distribution of Bike Rentals (cnt) in hour.csv')
plt.xlabel('Count of Bike Rentals')
plt.ylabel('Frequency')
st.pyplot(fig)

# Visualisasi korelasi antar variabel
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(pd_hour.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for hour.csv')
st.pyplot(fig)

# Menggunakan DataFrame df_day yang telah dibaca sebelumnya
# Ekstrak bulan dari kolom 'dteday'
df_day['month'] = df_day['dteday'].dt.month

# Hitung jumlah penyewaan sepeda per bulan
rentals_per_month = df_day.groupby('month')['cnt'].sum().reset_index()

# Plot grafik
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=rentals_per_month, x='month', y='cnt')
plt.title('Jumlah Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)

# Plot grafik perbandingan penyewaan sepeda dengan kondisi cuaca
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=df_day, x='weathersit', y='cnt')
plt.title('Perbandingan Jumlah Penyewaan Sepeda dengan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)
