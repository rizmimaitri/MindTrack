import streamlit as st

st.set_page_config(page_title="MindTrack", page_icon="🧠")

st.title("🧠 MindTrack")
st.write("Selamat datang di platform latihan soal & catatan kuliah!")

# Sidebar menu
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Latihan Soal
elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")

# Halaman Catatan Kuliah
elif menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")
    st.write("Berisi kumpulan catatan kuliah dari berbagai mata kuliah.")

# Halaman Riwayat Jawaban
elif menu == "Riwayat Jawaban":
    st.title("🗂️ Riwayat Jawaban")
    st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")

# Halaman Tentang
elif menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
