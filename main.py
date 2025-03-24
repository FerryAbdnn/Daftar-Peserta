import streamlit as st
from daftarPeserta import Peserta, daftarPeserta

st.title("Daftar Peserta Lomba")

page = st.sidebar.selectbox("Pilih Halaman", ["Tambah Peserta", "Daftar Peserta"])

daftar = daftarPeserta("data.csv")

if page == "Tambah Peserta":
    st.subheader("Form Tambah Peserta")

    with st.form("form_peserta"):
        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        divisi = st.selectbox("Divisi", ["UX Design", "Software Development", "Game Development", "Competitive Programming", "Data Mining"])
        button = st.form_submit_button("Tambah Peserta")

        if button:
            if not nama or not nim:
                st.warning("Nama dan NIM harus diisi")
            else:
                pesertaBaru = Peserta(nama, nim, divisi)
                daftar.tambahPeserta(pesertaBaru)
                
                st.session_state["peserta_data"] = daftar.getDaftarPeserta()
                st.success(f"Peserta {nama} berhasil ditambahkan!")

elif page == "Daftar Peserta":
    st.subheader("Daftar Peserta")

    if "peserta_data" not in st.session_state:
        st.session_state["peserta_data"] = daftar.getDaftarPeserta()

    st.dataframe(st.session_state["peserta_data"])
