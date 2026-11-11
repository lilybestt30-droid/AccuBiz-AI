# 📊 AccuBiz AI

**Pengembangan Sistem Informasi Akuntansi Berbasis Artificial Intelligence untuk Penilaian Kesehatan Keuangan dan Pendukung Pengambilan Keputusan UMKM**

AccuBiz AI adalah aplikasi *web* interaktif berbasis Streamlit yang dirancang untuk membantu Usaha Mikro, Kecil, dan Menengah (UMKM) dalam menganalisis kesehatan keuangan, memprediksi potensi kebangkrutan, dan memberikan rekomendasi keputusan bisnis secara otomatis menggunakan pendekatan *Machine Learning*.

## ✨ Fitur Utama

1. **Upload Data Mudah:** Mendukung file CSV dan Excel (Data transaksi/rekapitulasi UMKM).
2. **Penilaian Kesehatan Keuangan (Financial Health Score):**
   * **Altman Z-Score:** Analisis risiko kebangkrutan (*Bankruptcy Prediction*).
   * **Zmijewski X-Score:** Analisis potensi kesulitan keuangan (*Financial Distress*).
3. **Prediksi AI & Analisis Tren:** Memprediksi kinerja laba bersih periode berikutnya menggunakan model *Linear Regression*.
4. **Sistem Pendukung Keputusan (DSS):** Rekomendasi tindakan secara otomatis (*rule-based*) berdasarkan metrik kesehatan dan prediksi AI.
5. **Mode Uji Coba:** Disediakan *dataset* sampel bawaan agar pengguna dapat mencoba sistem secara instan.

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Framework Web:** Streamlit
* **Data Science & AI:** Pandas, NumPy, Scikit-Learn
* **Visualisasi Data:** Plotly Express

## 📂 Struktur Repositori

```text
AccuBiz-AI/
├── app.py                     # File utama aplikasi Streamlit (UI & Routing)
├── data_processing.py         # Modul pembersihan dan pengolahan data numerik
├── ai_models.py               # Algoritma prediksi Linear Regression, kategori Z-Score & X-Score
├── requirements.txt           # Daftar dependensi library Python
└── data_uji_coba_accubiz_zx.csv # Dataset sampel untuk pengujian
