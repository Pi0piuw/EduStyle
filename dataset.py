import csv
import random
import os
from collections import Counter

# Fungsi untuk menentukan label gaya belajar
def tentukan_label(freq_a, freq_v, freq_k, score_a, score_v, score_k):
    nilai_a = freq_a * score_a
    nilai_v = freq_v * score_v
    nilai_k = freq_k * score_k

    nilai_dict = {
        "Auditori": nilai_a,
        "Visual": nilai_v,
        "Kinestetik": nilai_k,
    }
    return max(nilai_dict, key=nilai_dict.get)

# Fungsi untuk hitung skor acak (kelipatan 10) dalam rentang rendah/tinggi
def hitung_rata_skor(jumlah_akses, tinggi=True):
    if jumlah_akses == 0:
        return 0
    if tinggi:
        skor_range = range(60, 101, 10)  # Skor tinggi (>50)
    else:
        skor_range = range(0, 51, 10)    # Skor rendah (<=50)
    total = sum([random.choice(skor_range) for _ in range(jumlah_akses)])
    return round(total / jumlah_akses, 2)

# Fungsi utama untuk generate data
def generate_data(jumlah_data=600, nama_file='aktivitas_lms.csv', persentase_skor_tinggi=0.5):
    header = [
        'Kode',
        'Akses_Kinestetik',
        'Akses_Visual',
        'Akses_Auditori',
        'Avg_Skor_Kinestetik',
        'Avg_Skor_Visual',
        'Avg_Skor_Auditori',
        'Gaya_Belajar'
    ]

    data = []
    max_akses = 20
    batas_tinggi = int(jumlah_data * persentase_skor_tinggi)

    for kode in range(jumlah_data//2):
        skor_tinggi = kode < batas_tinggi

        akses_k = random.randint(0, 5)
        akses_v = random.randint(0, 5)
        akses_a = random.randint(0, 5)

        skor_k = hitung_rata_skor(akses_k, tinggi=skor_tinggi)
        skor_v = hitung_rata_skor(akses_v, tinggi=skor_tinggi)
        skor_a = hitung_rata_skor(akses_a, tinggi=skor_tinggi)

        gaya_belajar = tentukan_label(
            freq_a=akses_a, freq_v=akses_v, freq_k=akses_k,
            score_a=skor_a, score_v=skor_v, score_k=skor_k
        )

        data.append([
            kode,
            akses_k, akses_v, akses_a,
            skor_k, skor_v, skor_a,
            gaya_belajar
        ])

    for kode in range(jumlah_data//2, jumlah_data):
        skor_tinggi = kode < batas_tinggi

        akses_k = random.randint(6, max_akses)
        akses_v = random.randint(6, max_akses)
        akses_a = random.randint(6, max_akses)

        skor_k = hitung_rata_skor(akses_k, tinggi=skor_tinggi)
        skor_v = hitung_rata_skor(akses_v, tinggi=skor_tinggi)
        skor_a = hitung_rata_skor(akses_a, tinggi=skor_tinggi)

        gaya_belajar = tentukan_label(
            freq_a=akses_a, freq_v=akses_v, freq_k=akses_k,
            score_a=skor_a, score_v=skor_v, score_k=skor_k
        )

        data.append([
            kode,
            akses_k, akses_v, akses_a,
            skor_k, skor_v, skor_a,
            gaya_belajar
        ])

    with open(nama_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print("Lokasi folder sekarang:", os.getcwd())
    print(f'Dataset berhasil disimpan di: {nama_file}')

# Fungsi untuk menghitung distribusi label
def hitung_label(nama_file='aktivitas_lms.csv'):
    with open(nama_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        labels = [row['Gaya_Belajar'] for row in reader]

    jumlah_per_label = Counter(labels)
    print("Jumlah masing-masing gaya belajar:")
    for label, jumlah in jumlah_per_label.items():
        print(f"{label}: {jumlah}")

# Jalankan fungsi
generate_data(jumlah_data=600, persentase_skor_tinggi=0.5)
hitung_label()
