import streamlit as st

def materi_visual_1():
    st.title("📖 Materi Visual: Sistem Peredaran Darah Manusia")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/peredaran-darah-kecil-1.gif", caption="Ilustrasi Jalur Peredaran Darah", width=600)
        st.markdown('<p style="text-align: center; font-size: 12px;">Sumber: [RuangGuru]</p>', unsafe_allow_html=True)
    st.markdown("""
Sistem peredaran darah manusia merupakan sistem tertutup dan ganda, artinya darah selalu mengalir dalam pembuluh dan melewati jantung dua kali dalam satu siklus lengkap.

Berikut ini adalah urutan alur peredaran darah:

---

### 1. Dari Bilik Kanan ke Paru-paru  
Darah kotor (kaya karbon dioksida) dipompa keluar dari **bilik kanan** jantung menuju **paru-paru** melalui arteri pulmonalis.

---

### 2. Di Paru-paru  
Di paru-paru, darah akan melepaskan karbon dioksida dan menyerap oksigen. Darah bersih (kaya oksigen) kemudian dialirkan kembali ke jantung.

---

### 3. Masuk ke Serambi Kiri  
Darah bersih dari paru-paru masuk ke **serambi kiri** jantung melalui vena pulmonalis.

---

### 4. Mengalir ke Bilik Kiri  
Dari serambi kiri, darah dialirkan ke **bilik kiri** jantung yang memiliki dinding paling tebal karena bertugas memompa darah ke seluruh tubuh.

---

### 5. Didorong ke Aorta  
Bilik kiri memompa darah ke seluruh tubuh melalui pembuluh darah terbesar bernama **aorta**.

---

### 6. Menuju Seluruh Tubuh  
Darah yang keluar dari aorta akan menyebar ke seluruh jaringan tubuh untuk menyuplai oksigen dan nutrisi.

---

### 7. Kembali ke Jantung Melalui Vena Cava  
Setelah digunakan oleh sel-sel tubuh, darah kotor kembali ke jantung melalui pembuluh balik besar bernama **vena cava**.

---

### 8. Masuk ke Serambi Kanan  
Darah yang datang melalui vena cava masuk ke **serambi kanan** jantung.

---

### 9. Mengalir ke Bilik Kanan  
Dari serambi kanan, darah dialirkan ke **bilik kanan** untuk mengulang kembali siklus ke paru-paru.

---

### 10. Siklus Berulang  
Siklus ini akan terus berulang sepanjang hidup manusia, memastikan suplai oksigen dan pembuangan karbon dioksida berjalan lancar.

---

""")

    st.success("✅ Materi visual selesai. Setelah ini, kamu bisa lanjut ke kuis!")

    if st.button("Selesai"):
        st.session_state.step = "kuis_visual_1"
        st.rerun()
