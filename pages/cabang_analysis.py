import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("🏢 Analisis Cabang")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠️ Silakan upload dataset terlebih dahulu di halaman utama.")
else:
    selected_year = st.selectbox("Pilih Tahun", sorted(df["Tahun"].unique()))
    df_year = df[df["Tahun"] == selected_year]

    st.markdown(f"### 💰 Profit per Cabang – Tahun {selected_year}")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(data=df_year, x="Cabang", y="Profit", palette="coolwarm")
    plt.title(f"Profit per Cabang ({selected_year})")
    st.pyplot(fig)

    st.markdown("### 📦 Data Penjualan per Cabang")
    st.dataframe(df_year)
