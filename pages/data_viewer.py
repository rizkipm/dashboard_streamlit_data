import streamlit as st
import pandas as pd

st.title("📋 Data Viewer")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠️ Silakan upload dataset terlebih dahulu di halaman utama.")
else:
    st.dataframe(df)

    with st.expander("📥 Unduh Data"):
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="💾 Download CSV",
            data=csv,
            file_name="data_penjualan.csv",
            mime="text/csv"
        )
