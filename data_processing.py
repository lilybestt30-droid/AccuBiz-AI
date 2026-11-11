import pandas as pd

def clean_data(df):
    """Membersihkan data dan memastikan kolom numerik aman digunakan untuk perhitungan."""
    df = df.dropna(how='all')
    cols_to_fill = ['Total_Aset', 'Total_Hutang', 'Laba_Bersih', 'Pendapatan', 'Z_Score', 'X_Score']
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df

def get_latest_metrics(df):
    """Mengambil data periode (baris) terakhir untuk ditampilkan sebagai status terkini."""
    if df.empty:
        return None
    return df.iloc[-1]
