import streamlit as st
import random

def materi_kinestetik_1():
    st.title("🤸 Materi Kinestetik 1: Susun Urutan Peredaran Darah")
    st.markdown("""
    Susun urutan peredaran darah dengan **menyusun blok** di bawah ini sesuai alur yang benar.  
    Urutan harus **dimulai dari jantung**, lalu mengalir secara **berurutan**.  
    Klik blok untuk menambahkan ke daftar kamu, lalu **cek jawaban**.
    """)
    st.info("📌 *Catatan: Urutan blok akan diacak setiap ada blok yang dipilih*")

    jawaban_benar = [
        "Jantung (Bilik kanan)",
        "Paru-paru",
        "Jantung (Serambi kiri)",
        "Jantung (Bilik kiri)",
        "Aorta",
        "Seluruh tubuh",
        "Vena cava",
        "Jantung (Serambi kanan)"
    ]

    bagian_jantung = [
        "Jantung (Bilik kanan)",
        "Jantung (Serambi kiri)",
        "Jantung (Bilik kiri)",
        "Jantung (Serambi kanan)"
    ]

    def is_rotasi_benar_dari_jantung(user, kunci):
        if len(user) != len(kunci):
            return False
        if user[0] not in bagian_jantung:
            return False
        double_kunci = kunci + kunci
        for i in range(len(kunci)):
            if double_kunci[i:i+len(kunci)] == user:
                return True
        return False

    # Inisialisasi urutan & status
    if "urutan_kinestetik" not in st.session_state:
        st.session_state.urutan_kinestetik = []
    if "jawaban_benar_kinestetik" not in st.session_state:
        st.session_state.jawaban_benar_kinestetik = False

    opsi_acak = jawaban_benar.copy()
    random.shuffle(opsi_acak)

    st.markdown("### 🔽 Klik blok untuk menambahkan:")
    col1, col2 = st.columns(2)
    for i, bagian in enumerate(opsi_acak):
        already_picked = bagian in st.session_state.urutan_kinestetik
        if i % 2 == 0:
            with col1:
                st.button(bagian, key=f"kines_btn1_{bagian}", disabled=already_picked, on_click=lambda b=bagian: st.session_state.urutan_kinestetik.append(b))
        else:
            with col2:
                st.button(bagian, key=f"kines_btn2_{bagian}", disabled=already_picked, on_click=lambda b=bagian: st.session_state.urutan_kinestetik.append(b))

    st.markdown("### 📌 Urutan yang kamu susun:")
    if st.session_state.urutan_kinestetik:
        for i, bagian in enumerate(st.session_state.urutan_kinestetik, 1):
            st.write(f"{i}. {bagian}")
    else:
        st.info("Belum ada blok yang dipilih.")

    if len(st.session_state.urutan_kinestetik) == len(jawaban_benar):
        if st.button("✅ Cek Jawaban"):
            if is_rotasi_benar_dari_jantung(st.session_state.urutan_kinestetik, jawaban_benar):
                st.success("💯 Bagus! Urutan kamu benar.")
                st.session_state.jawaban_benar_kinestetik = True
                st.session_state.step = "kuis_kinestetik_1"
            else:
                st.warning("⚠️ Urutan salah. Pastikan mulai dari jantung dan urutannya benar.")
                st.session_state.jawaban_benar_kinestetik = False
    else:
        st.info("📌 Susun semua blok terlebih dahulu untuk memeriksa jawaban.")


    st.button(
        "🔄 Reset Urutan",
        on_click=lambda: st.session_state.urutan_kinestetik.clear(),
        disabled=len(st.session_state.urutan_kinestetik) == 0
    )

    selesai_key = 'selesai_materi_kinestetik_1'
    if st.session_state.jawaban_benar_kinestetik:
        if st.button("✅ Selesai dan Lanjut ke Kuis"):
            st.session_state[selesai_key] = True
            st.session_state.step = 'kuis_kinestetik_1'
    else:
        st.button("✅ Selesai dan Lanjut ke Kuis", disabled=True)
