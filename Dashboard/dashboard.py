import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Layout dan Judul
st.set_page_config(page_title="Dashboard COVID-19 Indonesia", layout="wide")
st.title("🦠 Dashboard Analisis dan Prediksi COVID-19 Indonesia")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("Covid-19 Indonesia Dataset.csv")  # Sesuai dengan notebook kamu

data = load_data()

# Navigasi
menu = st.sidebar.radio("Menu", ["📊 EDA", "📈 Korelasi", "🤖 Prediksi", "📋 Evaluasi"])

# 📊 EDA
if menu == "📊 EDA":
    st.header("Exploratory Data Analysis")

    st.subheader("Tampilan Awal Dataset")
    st.dataframe(data.head())

    st.subheader("Trend Kasus Baru Harian")
    fig1 = px.line(data, x="Date", y="New Cases", title="Trend Kasus Baru Harian")
    st.plotly_chart(fig1)

    st.subheader("Distribusi Total Kasus")
    fig2, ax = plt.subplots()
    sns.histplot(data["Total Cases"], bins=30, kde=True, ax=ax)
    st.pyplot(fig2)

    st.subheader("Total Cases vs Total Deaths")
    fig3, ax = plt.subplots()
    sns.scatterplot(x="Total Cases", y="Total Deaths", data=data, ax=ax)
    st.pyplot(fig3)

# 📈 Korelasi
elif menu == "📈 Korelasi":
    st.header("Matriks Korelasi")
    cols = ["Total Cases", "Total Deaths", "New Cases", "Total Recovered"]
    corr = data[cols].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

# 🤖 Prediksi
elif menu == "🤖 Prediksi":
    st.header("Prediksi Total Deaths berdasarkan Total Cases")

    input_total_cases = st.number_input("Total Cases", 
                                        min_value=float(data["Total Cases"].min()), 
                                        max_value=float(data["Total Cases"].max()), 
                                        value=float(data["Total Cases"].mean()))

    X = data[["Total Cases"]]
    y = data["Total Deaths"]

    model = LinearRegression().fit(X, y)
    pred = model.predict([[input_total_cases]])[0]

    st.success(f"Prediksi Total Deaths: {pred:,.0f}")

# 📋 Evaluasi
elif menu == "📋 Evaluasi":
    st.header("Evaluasi Model Regresi: Total Cases → Total Deaths")

    X = data[["Total Cases"]]
    y = data["Total Deaths"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.subheader("Metode Evaluasi")
    st.write(f"MAE: {mean_absolute_error(y_test, y_pred):,.2f}")
    st.write(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

    st.subheader("Plot Prediksi vs Aktual")
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, alpha=0.6)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", lw=2)
    ax.set_xlabel("Actual Total Deaths")
    ax.set_ylabel("Predicted Total Deaths")
    st.pyplot(fig)