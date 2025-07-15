import streamlit as st
import pandas as pd

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di **MindTrack**, platform latihan soal dan catatan kuliah 👋")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

# Halaman Latihan Soal
elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")
elif menu == "Latihan Soal":
    st.title("📝 Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")

# Form upload file
    uploaded_file = st.file_uploader("Unggah file soal (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    
if uploaded_file is not None:
    st.success(f"Berhasil mengunggah: {uploaded_file.name}")
    file_details = {
            "Nama File": uploaded_file.name,
            "Jenis File": uploaded_file.type,
            "Ukuran": f"{uploaded_file.size / 1024:.2f} KB"
        }
    File "/mount/src/mindtrack/streamlit_app.py", line 34
          st.json(file_details)
         ^

# Tambahan jika ingin menampilkan isi file .txt (opsional)
if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
            st.text_area("Isi File:", content, height=300)

elif menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

if "show_notes" not in st.session_state:
        st.session_state.show_notes = False

    tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"], horizontal=True)
    blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
    matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

    if st.button("✅ simpan"):
        st.session_state.show_notes = True
        st.session_state.selected_tingkat = tingkat
        st.session_state.selected_blok = blok
        st.session_state.selected_matkul = matkul

    if st.session_state.show_notes:
        st.subheader(f"📘 Catatan untuk {st.session_state.selected_matkul} - {st.session_state.selected_tingkat} {st.session_state.selected_blok}")
        st.info("Belum ada catatan yang ditambahkan.")

# Halaman Riwayat Jawaban
elif menu == "Riwayat Jawaban":
    st.title("🗂️ Riwayat Jawaban")
    st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")

# Halaman Tentang
elif menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
    st.header("Tentang Pendiri")
    st.write("Zulfikar Syahid")
    st.write("Rizmi Maitri Nurgianti")
    st.write("Nafisah Nailalhusna I.")
    st.write("Jane Lazarina Bora Isu")
