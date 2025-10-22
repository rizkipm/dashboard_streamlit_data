import streamlit as st
import pandas as pd

# === Konfigurasi Halaman Utama ===
st.set_page_config(
    page_title="📊 Dashboard Penjualan Interaktif",
    page_icon="📈",
    layout="wide"
)

st.title("📊 Dashboard Penjualan & Profit – Multi Page")
st.markdown("""
Selamat datang di dashboard interaktif berbasis **Streamlit** 💻  
Gunakan sidebar untuk berpindah antar halaman (Overview, Cabang, Data Viewer).  
Kamu juga bisa **upload file CSV** untuk mengganti dataset default.
""")

# === Upload Dataset ===
uploaded_file = st.file_uploader("📤 Upload file CSV data penjualan", type=["csv"])

if uploaded_file is not None:
    # df = pd.read_csv(uploaded_file)
    df = pd.read_csv("data/sales_data_large.csv")

    st.session_state["df"] = df
    st.success("✅ Dataset berhasil diupload dan disimpan di session.")
else:
    # Default dataset jika belum upload
    df = pd.DataFrame({
        "Tahun": [2020, 2021, 2022, 2023, 2024],
        "Penjualan": [120, 150, 180, 210, 300],
        "Profit": [15, 25, 30, 45, 60],
        "Cabang": ["Jakarta", "Bandung", "Surabaya", "Medan", "Denpasar"]
    })
    st.session_state["df"] = df

# === Preview Data ===
st.markdown("### 🧾 Preview Data")
st.dataframe(st.session_state["df"].head())

st.info("📍 Pilih halaman di sidebar kiri untuk melihat analisis lainnya.")
