# 🎓 Proyek Akhir Praktikum Artificial Intelligence 
<h2 align="center">LMS Gaya Belajar Berbasis Streamlit</h2>

Aplikasi pembelajaran berbasis web yang menggunakan pendekatan kecerdasan buatan untuk memprediksi gaya belajar dominan siswa (Visual, Auditori, atau Kinestetik) berdasarkan interaksi mereka dengan materi. Sistem ini dikembangkan menggunakan algoritma *Random Forest* dan antarmuka interaktif dengan Streamlit.

---

## 📑 Daftar Isi
<details open="open">
<summary>Klik untuk melihat</summary>

1. [Anggota Tim](#👥-anggota-tim)  
2. [Latar Belakang](#📌-latar-belakang)  
3. [Tujuan dan Manfaat](#🎯-tujuan-dan-manfaat)  
4. [Penjelasan Aplikasi](#🧾-penjelasan-aplikasi)  
5. [Fitur Utama](#🛠️-fitur-utama)  
6. [Prediksi Gaya Belajar](#🧠-prediksi-gaya-belajar)  
7. [Tools dan Teknologi](#🧰-tools-dan-teknologi)  
8. [Rencana Pengerjaan Proyek](#📆-rencana-pengerjaan-proyek)  
9. [Lisensi](#🪪-lisensi)  
</details>

---

## 👥 Anggota Tim

| NPM           | Nama Lengkap             |
| ------------- | ------------------------ |
| 140810230025  | Kresna Bayu Wicaksono    |
| 140810230039  | Naqiyyah Zhahirah        |
| 140810230063  | Shofy Aliya              |

---

## 📌 Latar Belakang

Setiap siswa memiliki gaya belajar yang berbeda. Sayangnya, sistem pembelajaran konvensional sering kali bersifat seragam dan tidak memperhatikan perbedaan tersebut. Hal ini menyebabkan rendahnya efektivitas belajar bagi sebagian siswa.

Aplikasi ini dikembangkan sebagai solusi, dengan memanfaatkan AI untuk memprediksi gaya belajar dominan dari data interaksi siswa terhadap materi pembelajaran digital. Pendekatan ini mendukung pembelajaran yang adaptif dan personal.

---

## 🎯 Tujuan dan Manfaat

Tujuan:
- Mengembangkan sistem prediktif berbasis AI untuk mengklasifikasikan gaya belajar siswa.
- Memberikan rekomendasi materi belajar yang sesuai.
- Mendorong pembelajaran yang personal, bukan seragam.

Manfaat:
- Penerapan nyata algoritma *supervised learning* (Random Forest).
- Simulasi LMS yang responsif dan interaktif berbasis Streamlit.
- Memberikan insight kepada pengajar dalam menyesuaikan metode mengajar.

---

## 🧾 Penjelasan Aplikasi

Siswa akan mengakses tiga jenis materi (visual, auditori, kinestetik). Setelah itu, siswa mengerjakan kuis. Sistem mencatat frekuensi akses dan skor kuis, lalu memproses data tersebut untuk memprediksi gaya belajar dominan siswa. Hasil prediksi akan direkomendasikan dalam bentuk format materi yang sesuai.

---

## 🛠️ Fitur Utama

- Navigasi multi-halaman dengan sidebar
- Materi belajar berdasarkan gaya (visual, auditori, kinestetik)
- Kuis hanya terbuka setelah materi dipelajari
- Tracking skor dan frekuensi akses
- Prediksi gaya belajar dengan Random Forest
- Visualisasi hasil secara real-time
- Penyimpanan progres menggunakan `st.session_state`

---

## 🧠 Prediksi Gaya Belajar

Fitur input:
- `Akses_Visual`, `Akses_Auditori`, `Akses_Kinestetik`
- `Avg_Skor_Visual`, `Avg_Skor_Auditori`, `Avg_Skor_Kinestetik`

Model:
- Random Forest Classifier
  - Akurasi tinggi dan tahan terhadap overfitting
  - Dapat menangani data numerik dan kategorikal
  - Mendukung klasifikasi multi-kelas (Visual, Auditori, Kinestetik)

---

## 🧰 Tools dan Teknologi

| Tools              | Keterangan                                    |
|--------------------|-----------------------------------------------|
| Python             | Bahasa utama untuk pengolahan data dan model  |
| Pandas             | Untuk analisis dan manipulasi dataset         |
| Scikit-learn       | Pembangunan model Random Forest               |
| Pickle             | Menyimpan dan memuat ulang model `.pkl`       |
| Streamlit          | Antarmuka web interaktif dan ringan           |
| Visual Studio Code | Editor utama untuk pengembangan proyek        |

---

## 📆 Rencana Pengerjaan Proyek
 
Koordinasi Tim:
- WhatsApp → Komunikasi dan diskusi harian  

---

## 🪪 Lisensi

MIT License © 2025 – IF UNPAD  
Proyek ini bersifat open-source untuk kebutuhan edukasi dan pengembangan lebih lanjut.

---