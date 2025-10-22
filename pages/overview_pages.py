import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("📈 Overview Dashboard")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠️ Silakan upload dataset terlebih dahulu di halaman utama.")
else:
    total_penjualan = int(df["Penjualan"].sum())
    total_profit = int(df["Profit"].sum())
    avg_growth = round(df["Penjualan"].pct_change().mean() * 100, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Penjualan", f"{total_penjualan:,}")
    col2.metric("Total Profit", f"{total_profit:,}")
    col3.metric("Rata-rata Pertumbuhan", f"{avg_growth}%")

    st.markdown("### 📊 Grafik Tren Penjualan & Profit")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df, x="Tahun", y="Penjualan", marker="o", label="Penjualan")
    sns.lineplot(data=df, x="Tahun", y="Profit", marker="o", label="Profit")
    plt.title("Tren Penjualan dan Profit per Tahun")
    plt.legend()
    st.pyplot(fig)
