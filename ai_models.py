
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_trend(df, target_col):
    """Memprediksi nilai linear (Linear Regression) untuk 1 periode ke depan."""
    if len(df) < 3 or target_col not in df.columns:
        return None
    
    X = np.arange(len(df)).reshape(-1, 1)
    y = df[target_col].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_period = np.array([[len(df)]])
    prediction = model.predict(next_period)[0]
    return prediction

def evaluasi_z_score(z_score):
    """Menentukan kategori Z-Score berdasarkan ambang batas risiko kebangkrutan."""
    if z_score > 2.60:
        return "Sehat", "✅" #[cite: 2]
    elif 1.10 < z_score <= 2.60:
        return "Tidak dapat dipastikan / grey area", "⚠️" #[cite: 2]
    else:
        return "Tidak sehat / berpotensi bangkrut", "❌" #[cite: 2]

def evaluasi_x_score(x_score):
    """Menentukan kategori X-Score berdasarkan ambang batas financial distress."""
    if x_score < 0:
        return "Sehat / tidak berpotensi financial distress", "✅" #[cite: 1]
    else:
        return "Tidak sehat / berpotensi mengalami financial distress", "❌" #[cite: 1]
