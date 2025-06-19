import streamlit as st

def materi_auditori_1():
    st.title("🎧 Materi Auditori: Fungsi Organ Pencernaan")

    st.markdown("Silakan dengarkan penjelasan berikut untuk memahami fungsi organ-organ dalam sistem pencernaan:")

    audio_file_path = "assets/peredaran_darah.mp3"

    try:
        audio_file = open(audio_file_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    except FileNotFoundError:
        st.error("🎵 File audio tidak ditemukan. Pastikan file berada di folder `assets/` dan namanya benar.")

    st.markdown("---")

    selesai_key = 'selesai_materi_auditori_1'
    if st.button("✅ Selesai dan Lanjut ke Kuis"):
        st.session_state[selesai_key] = True
        st.session_state.step = 'kuis_auditori_1'
        st.rerun()
