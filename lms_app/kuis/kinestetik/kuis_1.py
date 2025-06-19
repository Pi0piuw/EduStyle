import streamlit as st

def kuis_kinestetik_1():
    st.subheader("📋 Kuis Kinestetik: Urutan Jalur Peredaran Darah")
    skor = 0

    pertanyaan = [
        {
            "soal": "1. Jalur awal darah dari jantung ke paru-paru dimulai dari...",
            "opsi": ["Jantung (Bilik kanan)", "Jantung (Serambi kiri)", "Jantung (Bilik kiri)", "Aorta"],
            "jawaban": "Jantung (Bilik kanan)"
        },
        {
            "soal": "2. Setelah darah dipompa dari bilik kanan, organ berikutnya adalah...",
            "opsi": ["Jantung (Serambi kanan)", "Paru-paru", "Aorta", "Seluruh tubuh"],
            "jawaban": "Paru-paru"
        },
        {
            "soal": "3. Setelah dari paru-paru, darah masuk ke bagian jantung...",
            "opsi": ["Serambi kiri", "Bilik kiri", "Serambi kanan", "Bilik kanan"],
            "jawaban": "Serambi kiri"
        },
        {
            "soal": "4. Setelah serambi kiri, darah akan mengalir ke...",
            "opsi": ["Bilik kanan", "Bilik kiri", "Vena cava", "Aorta"],
            "jawaban": "Bilik kiri"
        },
        {
            "soal": "5. Darah dari bilik kiri kemudian mengalir ke...",
            "opsi": ["Paru-paru", "Aorta", "Vena cava", "Serambi kanan"],
            "jawaban": "Aorta"
        },
        {
            "soal": "6. Dari aorta, darah akan mengalir ke...",
            "opsi": ["Seluruh tubuh", "Paru-paru", "Jantung", "Serambi kiri"],
            "jawaban": "Seluruh tubuh"
        },
        {
            "soal": "7. Setelah dari seluruh tubuh, darah kembali ke jantung melalui...",
            "opsi": ["Aorta", "Paru-paru", "Vena cava", "Vena pulmonalis"],
            "jawaban": "Vena cava"
        },
        {
            "soal": "8. Vena cava membawa darah masuk ke bagian jantung...",
            "opsi": ["Bilik kanan", "Serambi kiri", "Serambi kanan", "Bilik kiri"],
            "jawaban": "Serambi kanan"
        },
        {
            "soal": "9. Urutan yang benar setelah serambi kanan adalah...",
            "opsi": ["Bilik kanan → Paru-paru", "Paru-paru → Serambi kiri", "Bilik kiri → Aorta", "Serambi kiri → Bilik kanan"],
            "jawaban": "Bilik kanan → Paru-paru"
        },
        {
            "soal": "10. Setelah paru-paru, darah mengalir ke...",
            "opsi": ["Jantung (Serambi kiri)", "Jantung (Serambi kanan)", "Jantung (Bilik kiri)", "Seluruh tubuh"],
            "jawaban": "Jantung (Serambi kiri)"
        }
    ]

    jawaban_user = []

    with st.form("kuis_kinestetik_form"):
        for i, q in enumerate(pertanyaan):
            pilihan = st.radio(q["soal"], q["opsi"], key=f"soal_{i}")
            jawaban_user.append(pilihan)
        submit = st.form_submit_button("Submit Jawaban")

    if submit:
        for i, q in enumerate(pertanyaan):
            if jawaban_user[i] == q["jawaban"]:
                skor += 10

        st.success(f"Skor kamu: {skor} dari 100")
        st.session_state.skor["Kinestetik"] += skor
        st.session_state.akses["Kinestetik"] += 1
        st.session_state.step = "home"
