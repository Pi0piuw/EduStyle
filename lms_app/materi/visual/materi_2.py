import streamlit as st

def materi_visual_2():
    st.title("🧠 Materi Visual: Fungsi Organ Pencernaan")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/fungsi_organ_pencernaan.jpeg", caption="Ilustrasi Sistem Pencernaan Manusia", width=600)
        st.markdown('<p style="text-align: center; font-size: 12px;">Sumber: [Brainly]</p>', unsafe_allow_html=True)


    st.markdown("---")
    st.markdown("### Penjelasan")

    st.markdown("""
    Sistem pencernaan manusia terdiri dari berbagai organ yang bekerja sama untuk mencerna makanan menjadi zat gizi yang dapat diserap oleh tubuh. Berikut ini urutan dan fungsi masing-masing organnya:

    1. **Mulut**  
    Tempat makanan pertama kali masuk. Gigi menghancurkan makanan secara mekanis, dan air liur mengandung enzim amilase untuk memulai pencernaan karbohidrat.

    2. **Kerongkongan (Esofagus)**  
    Menghubungkan mulut dengan lambung. Makanan didorong ke lambung melalui gerakan peristaltik.

    3. **Lambung**  
    Mencerna makanan dengan enzim pepsin dan asam lambung. Makanan diubah menjadi bentuk semi-cair (kimus).

    4. **Usus Halus**  
    Tempat utama penyerapan nutrisi. Pankreas dan hati mengeluarkan enzim dan empedu untuk membantu pencernaan lemak, protein, dan karbohidrat.

    5. **Usus Besar**  
    Menyerap air dan membentuk feses. Bakteri di sini juga membantu produksi vitamin tertentu.

    6. **Rektum dan Anus**  
    Sisa makanan disimpan di rektum dan dikeluarkan melalui anus dalam bentuk feses.

    ### Kesimpulan:
    Setiap organ pencernaan memiliki fungsi penting yang mendukung penyerapan nutrisi. Memahami proses ini membantu kita menjaga kesehatan sistem pencernaan.
    """)

    st.markdown("---")

    selesai_key = 'selesai_materi_visual_2'
    if st.button("✅ Selesai dan Lanjut ke Kuis"):
        st.session_state[selesai_key] = True
        st.session_state.step = 'kuis_visual_2'
        st.rerun()
