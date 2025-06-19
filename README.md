# 📚 LMS Gaya Belajar Berbasis Streamlit

Sebuah aplikasi pembelajaran interaktif berbasis **gaya belajar** untuk membantu siswa memahami materi lebih efektif melalui pendekatan:
- **Kinestetik** (aktivitas fisik dan interaktif)
- **Visual** (gambar dan penjelasan teks)
- **Auditori** (penjelasan melalui audio)

Aplikasi ini juga dilengkapi **model machine learning Random Forest** untuk memprediksi gaya belajar dominan berdasarkan interaksi pengguna.

---

## 🛠 Fitur Utama

- ✅ Navigasi multi-halaman via sidebar
- ✅ Materi interaktif per gaya belajar
- ✅ Kuis hanya terbuka setelah menyelesaikan materi
- ✅ Tracking skor dan frekuensi akses per gaya belajar
- ✅ Prediksi gaya belajar siswa dengan Random Forest
- ✅ Visualisasi skor dan akses pengguna secara real-time
- ✅ Penyimpanan status pengguna menggunakan `st.session_state`

---

## 🧠 Prediksi Gaya Belajar

Prediksi dilakukan berdasarkan:
- **Akses** ke materi: `Akses_Kinestetik`, `Akses_Visual`, `Akses_Auditori`
- **Rata-rata skor** kuis: `Avg_Skor_Kinestetik`, `Avg_Skor_Visual`, `Avg_Skor_Auditori`

Model:  
```python
RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
