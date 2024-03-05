import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analisis Bike Sharing :sparkles:')
st.header('By Rafi Athallah Kurniawan')

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')


numeric_cols_day = day_df.select_dtypes(include=[np.number])
day_df[numeric_cols_day.columns] = numeric_cols_day.fillna(numeric_cols_day.mean())

numeric_cols_hour = hour_df.select_dtypes(include=[np.number])
hour_df[numeric_cols_hour.columns] = numeric_cols_hour.fillna(numeric_cols_hour.mean())

day_df = day_df.drop_duplicates()
hour_df = hour_df.drop_duplicates()

day_df = pd.read_csv('cleaned_day.csv')
hour_df = pd.read_csv('cleaned_hour.csv')


st.header('Visualisasi Data')

st.subheader('Histogram Jumlah Penyewaan Sepeda (cnt) di day.csv')
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(data=day_df, x='cnt', bins=30, kde=True)
plt.title('Distribution of Bike Rentals (cnt) in day.csv')
plt.xlabel('Count of Bike Rentals')
plt.ylabel('Frequency')
st.pyplot(fig)

st.subheader('Heatmap Korelasi untuk day.csv')
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(day_df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for day.csv')
st.pyplot(fig)

st.subheader('Histogram Jumlah Penyewaan Sepeda (cnt) di hour.csv')
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(data=hour_df, x='cnt', bins=30, kde=True)
plt.title('Distribution of Bike Rentals (cnt) in hour.csv')
plt.xlabel('Count of Bike Rentals')
plt.ylabel('Frequency')
st.pyplot(fig)

st.subheader('Heatmap Korelasi untuk hour.csv')
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(hour_df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for hour.csv')
st.pyplot(fig)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['month'] = day_df['dteday'].dt.month
rentals_per_month = day_df.groupby('month')['cnt'].sum().reset_index()

st.subheader('Jumlah Penyewaan Sepeda per Bulan')
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=rentals_per_month, x='month', y='cnt')
plt.title('Jumlah Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)

st.subheader('Perbandingan Jumlah Penyewaan Sepeda dengan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=day_df, x='weathersit', y='cnt')
plt.title('Perbandingan Jumlah Penyewaan Sepeda dengan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)

st.write("Jumlah baris setelah mengisi nilai yang hilang dan menghapus duplikat untuk dataset day.csv:", len(day_df))
st.write("Jumlah baris setelah mengisi nilai yang hilang dan menghapus duplikat untuk dataset hour.csv:", len(hour_df))
