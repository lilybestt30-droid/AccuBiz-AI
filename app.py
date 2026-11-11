import streamlit as st
import pandas as pd
import plotly.express as px
from data_processing import clean_data, get_latest_metrics
from ai_models import predict_trend, evaluasi_z_score, evaluasi_x_score

# Konfigurasi Halaman (Tanpa Sidebar)
st.set_page_config(page_title="AccuBiz AI", layout="wide")

st.title("📊 AccuBiz AI")
st.subheader("Sistem Informasi Akuntansi Berbasis AI untuk UMKM")
st.markdown("Penilaian Kesehatan Keuangan & Pendukung Pengambilan Keputusan")

# --- FITUR UJI COBA (Langsung di Halaman Utama) ---
st.markdown("---")
st.write("**Mode Uji Coba: Gunakan data sampel ini jika Anda belum memiliki file data sendiri.**")
with open("data_uji_coba_accubiz_zx.csv", "rb") as f:
    st.download_button(
        label="📥 Unduh Data Uji Coba (CSV)", 
        data=f, 
        file_name="data_uji_coba_accubiz_zx.csv", 
        mime="text/csv"
    )
st.markdown("---")

# --- UPLOAD DATA ---
st.write("**Mulai Analisis: Unggah file akuntansi Anda di bawah ini.**")
uploaded_file = st.file_uploader("Unggah File Data (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        df = clean_data(df)
        
        with st.expander("Lihat Detail Data Tabel"):
            st.dataframe(df, use_container_width=True)

        latest_data = get_latest_metrics(df)

        # --- SKOR KESEHATAN (Z-SCORE & X-SCORE) ---
        st.header("1. Penilaian Kesehatan Keuangan")
        
        if 'Z_Score' in df.columns and 'X_Score' in df.columns:
            z_val = latest_data['Z_Score']
            x_val = latest_data['X_Score']
            
            z_status, z_icon = evaluasi_z_score(z_val)
            x_status, x_icon = evaluasi_x_score(x_val)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Altman Z-Score (Periode Terakhir)", f"{z_val:.2f}")
                st.info(f"{z_icon} **Status:** {z_status}")
                
                fig_z = px.line(df, x='Bulan', y='Z_Score', title='Grafik Tren Z-Score')
                fig_z.add_hline(y=2.60, line_dash="dash", line_color="green", annotation_text="Batas Sehat (> 2.60)")
                fig_z.add_hline(y=1.10, line_dash="dash", line_color="red", annotation_text="Batas Bangkrut (<= 1.10)")
                st.plotly_chart(fig_z, use_container_width=True)
                
            with col2:
                st.metric("Zmijewski X-Score (Periode Terakhir)", f"{x_val:.2f}")
                st.info(f"{x_icon} **Status:** {x_status}")
                
                fig_x = px.line(df, x='Bulan', y='X_Score', title='Grafik Tren X-Score')
                fig_x.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Batas Distress (0)")
                st.plotly_chart(fig_x, use_container_width=True)
        else:
            st.warning("File yang diunggah tidak memiliki kolom 'Z_Score' dan 'X_Score'. Pastikan format data Anda sesuai dengan data uji coba.")

        # --- AI PREDIKSI TREN KEUANGAN ---
        st.header("2. AI Prediksi Kinerja & Rekomendasi Keputusan")
        if 'Laba_Bersih' in df.columns:
            pred_laba = predict_trend(df, 'Laba_Bersih')
            
            if pred_laba is not None:
                st.metric("🔮 Prediksi Laba Bersih Periode Depan", f"Rp {pred_laba:,.0f}")
                
                # Rule-based Recommendation
                if pred_laba < 0:
                    st.error("⚠️ **Rekomendasi AI:** Prediksi laba periode depan bernilai negatif (Rugi). Segera lakukan efisiensi pengeluaran, tunda pembelian aset, dan fokus pada penagihan piutang!")
                elif pred_laba >= 0 and z_val <= 1.10:
                    st.warning("⚠️ **Rekomendasi AI:** Prediksi laba positif, namun risiko kebangkrutan sangat tinggi. Hindari penambahan hutang baru dan pertahankan likuiditas kas.")
                else:
                    st.success("✅ **Rekomendasi AI:** Prediksi laba positif dan metrik risiko terkendali. Pertahankan strategi saat ini.")
            else:
                st.warning("Data terlalu sedikit untuk melakukan prediksi AI (membutuhkan minimal 3 baris data).")
        else:
            st.info("Sistem membutuhkan kolom 'Laba_Bersih' untuk mengaktifkan fitur prediksi.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses data: {e}. Pastikan format file sesuai.")
