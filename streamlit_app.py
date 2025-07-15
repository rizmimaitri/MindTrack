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
    
elif menu == "Latihan Soal":
    st.title("✏ Latihan Soal")
    st.write("Silakan jawab soal-soal berikut dan kirim jawabanmu:")

    if "show_notes" not in st.session_state:
        st.session_state.show_notes = False

    tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"], horizontal=True)
    blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
    matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

    import streamlit as st
# Title for the application
st.title("Latihan Soal")
# Select Level
tingkat = st.radio("Pilih Tingkat:", ["Tingkat 1", "Tingkat 2"])
# Select Block
blok = st.selectbox("Pilih Blok:", ["Blok 1", "Blok 2", "Blok 3"])
# Select Subject
mata_kuliah = st.selectbox("Pilih Mata Kuliah:", ["Biokimia", "Fisika", "Matematika"])
# Store answer
st.header("1. Unsur manakah yang termasuk logam alkali?")
jawaban = st.radio("Pilih jawaban:", ["A. Lithium", "B. Helium", "C. Neon", "D. Karbon"])
# Simpan button
if st.button("Simpan"):
    st.success("Jawaban Anda telah disimpan!")
    
    if st.button("✅ simpan"):
        st.session_state.show_notes = True
        st.session_state.selected_tingkat = tingkat
        st.session_state.selected_blok = blok
        st.session_state.selected_matkul = matkul

    # SOAL 1
    st.subheader("1. Unsur manakah yang termasuk logam alkali?")
    jawaban1 = st.radio("Pilih jawaban:", ["Oksigen", "Natrium", "Kalsium", "Klorin"], key="soal1")

    # SOAL 2
    st.subheader("2. Rumus kimia dari air adalah...")
    jawaban2 = st.radio("Pilih jawaban:", ["CO2", "NaCl", "H2O", "CH4"], key="soal2")

    # SOAL 3
    st.subheader("3. Manakah yang merupakan senyawa organik?")
    jawaban3 = st.multiselect("Pilih semua yang benar:", ["NaCl", "CH4", "C2H6", "H2SO4"], key="soal3")

    # TOMBOL KIRIM
    if st.button("✅ Kirim Jawaban"):
        st.success("Jawaban kamu berhasil dikirim!")

        # Koreksi otomatis
        skor = 0
        if jawaban1 == "Natrium":
            skor += 1
        if jawaban2 == "H2O":
            skor += 1
        if set(jawaban3) == {"CH4", "C2H6"}:
            skor += 1

        # Tampilkan hasil
        st.markdown("### 📊 Rekap Jawaban Kamu:")
        st.write(f"**1.** {jawaban1}")
        st.write(f"**2.** {jawaban2}")
        st.write(f"**3.** {', '.join(jawaban3)}" if jawaban3 else "**3.** Belum menjawab")

        st.markdown(f"### 🏆 Skor Akhir: **{skor}/3**")



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
