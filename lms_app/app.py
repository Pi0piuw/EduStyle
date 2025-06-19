import streamlit as st
import pandas as pd
import pickle

from materi.kinestetik import materi_list as kinestetik_materi
from materi.visual import materi_list as visual_materi
from materi.auditori import materi_list as auditori_materi

from kuis.kinestetik import kuis_list as kinestetik_kuis
from kuis.visual import kuis_list as visual_kuis
from kuis.auditori import kuis_list as auditori_kuis

all_kuis = {}
all_kuis.update(kinestetik_kuis)
all_kuis.update(visual_kuis)
all_kuis.update(auditori_kuis)

# Load model prediksi
with open('model_rf.pkl', 'rb') as f:
    model = pickle.load(f)

# Inisialisasi session state
if 'akses' not in st.session_state:
    st.session_state.akses = {'Kinestetik': 9, 'Visual': 10, 'Auditori': 12}
if 'skor' not in st.session_state:
    st.session_state.skor = {'Kinestetik': 720, 'Visual': 890, 'Auditori': 1080}
if 'step' not in st.session_state:
    st.session_state.step = 'home'

# Fungsi prediksi gaya belajar
def prediksi_gaya_belajar():
    def rata(jenis):
        a = st.session_state.akses[jenis]
        return st.session_state.skor[jenis] / a if a > 0 else 0
    df = pd.DataFrame({
        'Akses_Kinestetik': [st.session_state.akses['Kinestetik']],
        'Akses_Visual': [st.session_state.akses['Visual']],
        'Akses_Auditori': [st.session_state.akses['Auditori']],
        'Avg_Skor_Kinestetik': [rata('Kinestetik')],
        'Avg_Skor_Visual': [rata('Visual')],
        'Avg_Skor_Auditori': [rata('Auditori')],
    })
    return model.predict(df)[0]

# Halaman utama
def home_page():
    st.set_page_config(page_title="LMS Gaya Belajar", layout="wide")
    st.title("🎓 EduStyle")
    st.markdown("Belajar efektif sesuai **gaya belajar** kamu. Pilih materi di sidebar.")

    # Tombol home
    st.sidebar.markdown("## 🏠 Home")
    if st.sidebar.button("Beranda"):
        st.session_state.step = 'home'
        st.rerun()


    # Materi
    st.sidebar.markdown("## 📘 Materi")
    tampilkan_menu()

    st.sidebar.markdown("---")
    st.sidebar.markdown("🧠 Gaya belajar diprediksi dari interaksi kamu.")

    # Tampilan jumlah  akses
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Kinestetik", st.session_state.akses['Kinestetik'])
    col2.metric("Visual", st.session_state.akses['Visual'])
    col3.metric("Auditori", st.session_state.akses['Auditori'])

    # Fungsi untuk menghitung rata-rata
    def rata(jenis):
        a = st.session_state.akses[jenis]
        return st.session_state.skor[jenis] / a if a > 0 else 0

    col4, col5, col6 = st.columns(3)
    col4.metric("Rata-rata Skor Kinestetik", f"{rata('Kinestetik'):.2f}")
    col5.metric("Rata-rata Skor Visual", f"{rata('Visual'):.2f}")
    col6.metric("Rata-rata Skor Auditori", f"{rata('Auditori'):.2f}")

    if sum(st.session_state.akses.values()) > 0:
        gaya = prediksi_gaya_belajar()
        st.success(f"🎯 Prediksi gaya belajar kamu: **{gaya}**")
    else:
        st.warning("📌 Akses materi dulu untuk prediksi gaya belajar.")

# Fungsi sidebar
def tampilkan_menu():
    jenis_materi = {
        "Kinestetik": kinestetik_materi,
        "Visual": visual_materi,
        "Auditori": auditori_materi
    }

    for jenis, materi_dict in jenis_materi.items():
        st.sidebar.markdown(f"**{jenis}**")
        for nama, data in materi_dict.items():
            label = data["judul"]
            if st.sidebar.button(f"  ↪ {label}", key=nama):
                st.session_state.step = nama
                st.rerun()


def tampilkan_sidebar():
    # Tombol home
    st.sidebar.markdown("## 🏠 Home")
    if st.sidebar.button("Beranda"):
        st.session_state.step = 'home'
        st.rerun()

    # Materi
    st.sidebar.markdown("## 📘 Materi")
    tampilkan_menu()

    st.sidebar.markdown("---")
    st.sidebar.markdown("🧠 Gaya belajar diprediksi dari interaksi kamu.")

# Routing
all_materi = {}
for d in (kinestetik_materi, visual_materi, auditori_materi):
    for nama, data in d.items():
        all_materi[nama] = data["fungsi"]


# Cek dan reset variabel jika pindah halaman
if 'last_step' not in st.session_state:
    st.session_state.last_step = st.session_state.step

if st.session_state.step != st.session_state.last_step:
    # Reset variabel state lokal
    st.session_state.urutan_kinestetik = []
    st.session_state.jawaban_organ = {}
    st.session_state.skor_materi_2 = 0
    st.session_state.last_step = st.session_state.step  # Update

if st.session_state.step == 'home':
    home_page()
elif st.session_state.step in all_materi:
    tampilkan_sidebar() 
    all_materi[st.session_state.step]()
elif st.session_state.step in all_kuis:
    tampilkan_sidebar()
    all_kuis[st.session_state.step]()
else:
    st.error("Halaman tidak ditemukan.")