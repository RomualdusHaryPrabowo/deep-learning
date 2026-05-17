# Sentiment Analysis Komentar Aplikasi Gojek di Google Play Store

## Deskripsi Proyek
Proyek ini merupakan implementasi **Analisis Sentimen** terhadap komentar pengguna aplikasi Gojek yang diambil dari Google Play Store menggunakan teknik *scraping*. Dataset berisi sekitar **15.000 komentar** yang kemudian dilakukan pelabelan sentimen menjadi:

- Positif
- Negatif
- Netral

Proyek ini bertujuan untuk menganalisis opini pengguna terhadap layanan aplikasi Gojek menggunakan pendekatan Deep Learning dengan algoritma **LSTM** dan **Bi-LSTM**.

---

# Tahapan Proyek

## 1. Data Collection
Data diambil melalui proses scraping komentar aplikasi Gojek dari Google Play Store.

Jumlah data: ±15.000 komentar.

---

## 2. Data Labeling
Komentar diberi label sentimen menjadi tiga kelas:

- Positif
- Negatif
- Netral

---

## 3. Text Preprocessing
Tahapan preprocessing yang dilakukan meliputi:

- Case Folding
- Cleaning Text
- Menghapus URL, simbol, dan karakter khusus
- Normalisasi kata tidak baku
- Stopword Removal
- Stemming Bahasa Indonesia menggunakan **Sastrawi**

Contoh normalisasi kata:

| Kata Asli | Hasil Normalisasi |
|---|---|
| gk | tidak |
| lag | lambat |
| error | galat |
| keren | bagus |
| cancel | batal |

---

## 4. Feature Extraction & Label Encoding
Data teks yang telah dibersihkan kemudian dilakukan:

- Tokenizing
- Padding Sequence
- Label Encoding
- Konversi teks menjadi representasi numerik

---

## 5. Data Splitting
Dataset dibagi menjadi data training dan testing dengan beberapa skema:

| Skema | Algoritma | Split Data |
|---|---|---|
| Skema 1 | LSTM | 80:20 |
| Skema 2 | Bi-LSTM | 80:20 |
| Skema 3 | Bi-LSTM | 90:10 |

---

## 6. Model Training
Model Deep Learning yang digunakan:

- LSTM (Long Short-Term Memory)
- Bidirectional LSTM (Bi-LSTM)

Library utama:
- TensorFlow
- Keras
- Scikit-Learn

---

## 7. Inferensi
Model yang telah dilatih digunakan untuk melakukan prediksi sentimen terhadap komentar baru.

---

# Struktur Folder

```bash
proyek-analysis-sentimen/
├── dataset_com.gojek.app_15k.csv
├── analisis_sentimen.ipynb
├── requirements.txt
├── scraping.py
└── README.md