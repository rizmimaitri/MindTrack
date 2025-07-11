import streamlit as st

st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Sidebar menu
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")

    # Cek apakah user sudah login
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        st.subheader("🔐 Silakan Login")
        username = st.text_input("Nama kamu")
        if st.button("Login"):
            if username.strip() != "":
                st.session_state.is_logged_in = True
                st.session_state.username = username
                st.success(f"Halo, {username}! Kamu berhasil login.")
            else:
                st.warning("Nama tidak boleh kosong.")
    else:
        st.success(f"Halo, {st.session_state.username}! 👋")
        st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

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
