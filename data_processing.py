import pandas as pd
import numpy as np

def clean_data(df):
    """Pembersihan data otomatis"""
    df = df.dropna(how='all') # Hapus baris kosong
    # Pastikan kolom tanggal berformat datetime
    if 'Tanggal' in df.columns:
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    
    # Isi nilai kosong (NaN) dengan 0 pada kolom numerik
    cols_to_fill = ['Pemasukan', 'Pengeluaran', 'Saldo Kas']
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    return df

def calculate_financial_health(df):
    """Menghitung metrik sederhana dan Skor Kesehatan (0-100)"""
    total_pemasukan = df['Pemasukan'].sum()
    total_pengeluaran = df['Pengeluaran'].sum()
    
    if total_pemasukan == 0:
        return 0, 0, 0
    
    # Asumsi Sederhana:
    # Profit Margin = (Pemasukan - Pengeluaran) / Pemasukan
    net_profit = total_pemasukan - total_pengeluaran
    profit_margin = (net_profit / total_pemasukan) * 100
    
    # Skor Kesehatan (Logika Sederhana)
    # Jika margin >= 20% (Sangat Sehat = 90-100)
    # Jika margin 10-19% (Sehat = 70-89)
    # Jika margin 0-9% (Waspada = 50-69)
    # Jika margin < 0 (Kritis < 50)
    
    if profit_margin >= 20:
        skor = 95
    elif profit_margin >= 10:
        skor = 80
    elif profit_margin >= 0:
        skor = 60
    else:
        skor = 30
        
    return profit_margin, net_profit, skor

def generate_recommendation(skor, net_profit):
    """Rule-based decision support"""
    if skor >= 80:
        return "✅ Keuangan Sangat Sehat. Pertahankan margin keuntungan dan pertimbangkan ekspansi bisnis."
    elif skor >= 60:
        return "⚠️ Keuangan Waspada. Margin tipis. Coba tekan pengeluaran operasional atau evaluasi harga jual."
    else:
        return "❌ Keuangan Kritis (Rugi). Segera hentikan pengeluaran tidak penting dan fokus genjot penjualan bulan ini!"
