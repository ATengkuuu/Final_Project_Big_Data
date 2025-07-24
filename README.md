# 🦠 Final Project Big Data - Analisis & Prediksi COVID-19 Indonesia

# 🧠 Dibuat oleh
- [Isi Nama Anggota Tim di sini]
- [Contoh: Agi Tengku 23.11.xxxx]
- [Kosongkan baris ini jika belum ada nama lengkap]
- [Kosongkan baris ini jika belum ada nama lengkap]

Mata Kuliah: Big Data & Predictive Analytics  
Universitas Amikom Yogyakarta

Proyek ini bertujuan untuk menganalisis dan memprediksi perkembangan COVID-19 di Indonesia menggunakan teknik eksplorasi data dan algoritma regresi linier.

---

## 📂 Struktur Folder
- `data/` : Dataset mentah dan hasil pembersihan (CSV)
- `notebook/` : Notebook Jupyter utama (`Covid_19_Indonesia_Dataset.ipynb`)
- `dashboard/` : File dashboard interaktif (`dashboard.py`)
- `laporan/` : Laporan akhir (PDF atau DOCX)
- `poster/` : Poster singkat berbentuk JPG
- `requirements.txt` : Daftar pustaka Python yang digunakan

---

## 📊 Dataset
- Jumlah baris: ±31.822 baris dan 38 kolom 
- Kolom penting: `Date`, `Total Cases`, `New Cases`, `Total Deaths`, `Total Recovered`
- File: `Covid_19_Indonesia_Dataset.csv` (bersih dan siap pakai)

---

## 🔍 Analisis
- **EDA**: 
  - Tren kasus harian (`New Cases`)
  - Distribusi total kasus dan kematian
  - Scatter plot `Total Cases` vs `Total Deaths`
- **Korelasi**: 
  - Heatmap antar fitur numerik
  - Visualisasi interaktif (Plotly)
- **Model Regresi Linier**:
  - Fitur: `Total Cases`
  - Target: `Total Deaths`
- **Evaluasi**:
  - MAE (Mean Absolute Error)
  - R² Score
  - Visualisasi Prediksi vs Aktual

---

## 🚀 Cara Menjalankan

### ▶️ Via Notebook
Buka notebook berikut di Google Colab atau Jupyter: Final_Project_Big_Data\Notebook\Covid_19_Indonesia_Dataset.ipynb