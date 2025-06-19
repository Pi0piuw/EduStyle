import streamlit as st

def materi_kinestetik_2():
    st.title("🤸 Materi Kinestetik 2: Cocokkan Fungsi Organ Pencernaan")
    st.info("""
    👉 **Petunjuk:**
    1. Akan muncul nama organ satu per satu.
    2. Pilih fungsi yang paling sesuai untuk setiap organ dari daftar pilihan.
    3. Setelah memilih, klik tombol **'Kunci Jawaban'** untuk menyimpan jawaban kamu.
    4. Kamu **tidak bisa mengganti jawaban** setelah dikunci.
    5. Nilai akan muncul setelah semua organ dijawab.
    """)

    # Data pasangan organ dan fungsi
    pasangan = {
        "Mulut": "Mengunyah dan mencerna makanan secara mekanik dan kimiawi",
        "Kerongkongan": "Menyalurkan makanan dari mulut ke lambung",
        "Lambung": "Mencerna makanan dengan enzim dan asam lambung",
        "Usus Halus": "Menyerap nutrisi dari makanan yang dicerna",
        "Usus Besar": "Menyerap air dan membentuk feses",
        "Hati": "Menghasilkan empedu untuk membantu pencernaan lemak",
        "Pankreas": "Menghasilkan enzim untuk mencerna karbohidrat, protein, dan lemak",
        "Rektum": "Menyimpan feses sebelum dikeluarkan"
    }

    # Inisialisasi session state
    if "soal_kinestetik_2" not in st.session_state:
        st.session_state.soal_kinestetik_2 = list(pasangan.items())  # TANPA random
        st.session_state.jawaban_kinestetik_2 = {}
        st.session_state.skor_materi_2 = 0
        st.session_state.selesai_materi_kinestetik_2 = False

    soal = st.session_state.soal_kinestetik_2
    jawaban = st.session_state.jawaban_kinestetik_2
    semua_fungsi = list(pasangan.values())  # Tetap urutan

    for organ, fungsi_benar in soal:
        if organ in jawaban:
            st.success(f"✅ {organ}: {jawaban[organ]}")
        else:
            st.write(f"### 🔹 Organ: {organ}")
            selected = st.radio(f"Pilih fungsi untuk organ **{organ}**", semua_fungsi, key=f"radio_{organ}")
            if st.button(f"Kunci Jawaban: {organ}", key=f"kunci_{organ}"):
                jawaban[organ] = selected
                if selected == fungsi_benar:
                    st.session_state.skor_materi_2 += 10
                st.rerun()

    # Tampilkan skor dan tombol lanjut jika selesai
    if len(jawaban) == len(soal):
        st.success(f"🎉 Skor kamu: {st.session_state.skor_materi_2} / 80")
        st.session_state.selesai_materi_kinestetik_2 = True

        if st.button("✅ Selesai dan Lanjut ke Kuis"):
            st.session_state.step = "kuis_kinestetik_2"
            st.session_state.skor_materi_2 = 0
            st.session_state.soal_kinestetik_2 = []
            st.session_state.jawaban_kinestetik_2 = {}
