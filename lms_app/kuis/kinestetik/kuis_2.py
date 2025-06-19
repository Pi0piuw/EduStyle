import streamlit as st

def kuis_kinestetik_2():
    st.subheader("📋 Kuis Kinestetik: Fungsi Organ Sistem Pencernaan")
    skor = 0

    pertanyaan = [
        {
            "soal": "1. Apa fungsi utama mulut dalam sistem pencernaan?",
            "opsi": ["Mencerna protein", "Mencerna lemak", "Mengunyah dan memecah makanan secara mekanik", "Menyerap nutrisi"],
            "jawaban": "Mengunyah dan memecah makanan secara mekanik"
        },
        {
            "soal": "2. Organ apa yang menghubungkan mulut dengan lambung?",
            "opsi": ["Kerongkongan", "Usus halus", "Usus besar", "Trakea"],
            "jawaban": "Kerongkongan"
        },
        {
            "soal": "3. Fungsi utama lambung dalam pencernaan adalah...",
            "opsi": ["Menyerap nutrisi", "Mencerna karbohidrat", "Mencerna protein dengan enzim dan asam", "Mengedarkan darah"],
            "jawaban": "Mencerna protein dengan enzim dan asam"
        },
        {
            "soal": "4. Hati menghasilkan empedu yang berfungsi untuk...",
            "opsi": ["Mencerna protein", "Menetralisir asam", "Mengemulsi lemak", "Menyerap air"],
            "jawaban": "Mengemulsi lemak"
        },
        {
            "soal": "5. Dimanakah sebagian besar penyerapan nutrisi terjadi?",
            "opsi": ["Lambung", "Usus halus", "Usus besar", "Pankreas"],
            "jawaban": "Usus halus"
        },
        {
            "soal": "6. Fungsi utama usus besar adalah...",
            "opsi": ["Menghasilkan enzim", "Menyerap air dan membentuk feses", "Mencerna karbohidrat", "Menyaring racun"],
            "jawaban": "Menyerap air dan membentuk feses"
        },
        {
            "soal": "7. Organ apa yang menghasilkan insulin dan enzim pencernaan?",
            "opsi": ["Lambung", "Usus besar", "Hati", "Pankreas"],
            "jawaban": "Pankreas"
        },
        {
            "soal": "8. Dimana empedu disimpan sebelum digunakan?",
            "opsi": ["Hati", "Pankreas", "Kandung empedu", "Lambung"],
            "jawaban": "Kandung empedu"
        },
        {
            "soal": "9. Fungsi utama enzim amilase adalah...",
            "opsi": ["Memecah protein", "Memecah lemak", "Memecah karbohidrat", "Menghancurkan bakteri"],
            "jawaban": "Memecah karbohidrat"
        },
        {
            "soal": "10. Proses terakhir pencernaan berlangsung di organ...",
            "opsi": ["Lambung", "Usus besar", "Usus halus", "Mulut"],
            "jawaban": "Usus besar"
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
        st.rerun()
