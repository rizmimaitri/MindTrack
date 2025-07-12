import streamlit as st
import pandas as pd

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")

    # Inisialisasi session state jika belum ada
    if "halaman" not in st.session_state:
        st.session_state.halaman = "awal"
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
    # Flag untuk menunjukkan pendaftaran berhasil di sesi ini, agar pesan sukses muncul sekali
    if "registration_successful_this_session" not in st.session_state:
        st.session_state.registration_successful_this_session = False

    # Fungsi untuk memuat data pengguna dari CSV
    def load_users():
        try:
            df = pd.read_csv("users.csv")
            return df
        except FileNotFoundError: # Tangani jika file belum ada
            return pd.DataFrame(columns=["nama_lengkap", "nama_panggilan", "nim", "password"])

    users_df = load_users()

    # Logika tampilan berdasarkan status login
    if not st.session_state.is_logged_in: # Jika pengguna BELUM login
        # Halaman awal dengan pilihan Masuk / Daftar
        if st.session_state.halaman == "awal":
            st.write("Halo! Selamat datang di **MindTrack**, platform latihan soal dan catatan kuliah 👋")
            st.write("Silakan pilih salah satu opsi di bawah:")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔐 Masuk"):
                    st.session_state.halaman = "login"
            with col2:
                if st.button("📝 Daftar"):
                    st.session_state.halaman = "daftar"

        # Halaman Login
        elif st.session_state.halaman == "login":
            st.subheader("🔐 Masuk ke Akun")
            nama_login = st.text_input("Nama Lengkap")
            password_login = st.text_input("Password", type="password")

            if st.button("Masuk"):
                user_match = users_df[
                    (users_df["nama_lengkap"] == nama_login) &
                    (users_df["password"] == password_login)
                ]
                if not user_match.empty:
                    st.session_state.is_logged_in = True
                    st.session_state.nama_lengkap = user_match.iloc[0]["nama_lengkap"]
                    st.session_state.nama_panggilan = user_match.iloc[0]["nama_panggilan"]
                    st.session_state.nim = user_match.iloc[0]["nim"]
                    st.success(f"Halo, {st.session_state.nama_panggilan}! Kamu berhasil login.")
                    # Setelah login, langsung tampilkan halaman utama yang sudah login
                    st.session_state.halaman = "beranda_logged_in" # State baru untuk tampilan setelah login
                else:
                    st.warning("Akun tidak ditemukan. Ayo daftar dulu yuk!")
                    st.session_state.halaman = "daftar" # Arahkan ke halaman daftar jika tidak ditemukan

            st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"halaman": "awal"}))

        # Halaman Pendaftaran
        elif st.session_state.halaman == "daftar":
            st.subheader("📝 Daftar Akun Baru")
            nama_lengkap = st.text_input("Nama Lengkap")
            nama_panggilan = st.text_input("Nama Panggilan (opsional)")
            nim = st.text_input("NIM")
            password = st.text_input("Password", type="password")

            # Tombol "Daftar" dan logikanya harus berada di dalam blok halaman "daftar"
            if st.button("Daftar"):
                if nama_lengkap.strip() == "" or nim.strip() == "" or password.strip() == "":
                    st.warning("Nama lengkap, NIM, dan password wajib diisi.")
                elif nama_lengkap in users_df["nama_lengkap"].values:
                    st.warning("Nama sudah terdaftar. Silakan masuk.")
                    st.session_state.halaman = "login"
                else:
                    # Simpan data user baru
                    new_data = pd.DataFrame([{
                        "nama_lengkap": nama_lengkap,
                        "nama_panggilan": nama_panggilan if nama_panggilan.strip() else nama_lengkap.split()[0],
                        "nim": nim,
                        "password": password
                    }])
                    new_df = pd.concat([users_df, new_data], ignore_index=True)
                    new_df.to_csv("users.csv", index=False)

                    # Langsung login otomatis setelah pendaftaran
                    st.session_state.is_logged_in = True
                    st.session_state.nama_lengkap = nama_lengkap
                    st.session_state.nama_panggilan = nama_panggilan if nama_panggilan.strip() else nama_lengkap.split()[0]
                    st.session_state.nim = nim
                    st.session_state.registration_successful_this_session = True # Set flag ini
                    st.session_state.halaman = "beranda_logged_in" # Arahkan ke tampilan setelah login

            # Tombol "Kembali" untuk halaman daftar
            st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"halaman": "awal"}))

    else: # Jika pengguna SUDAH login (ini adalah 'else' yang benar untuk 'if not st.session_state.is_logged_in:')
        if st.session_state.registration_successful_this_session:
            st.success(f"Pendaftaran berhasil! Selamat datang, {st.session_state.nama_panggilan} 🎉")
            st.session_state.registration_successful_this_session = False # Reset flag
        else:
            st.success(f"Halo, {st.session_state.nama_panggilan}! 👋")
        st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

        # Tambahkan tombol logout jika sudah login
        if st.button("Keluar"):
            st.session_state.is_logged_in = False
            st.session_state.halaman = "awal"
            st.success("Anda telah berhasil keluar.")

# Halaman Latihan Soal
elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")
    if not st.session_state.is_logged_in:
        st.warning("Anda harus login untuk mengakses halaman ini.")

# Halaman Catatan Kuliah
elif menu == "Catatan Kuliah":
    if not st.session_state.get("is_logged_in", False):
        st.warning("Silakan login terlebih dahulu untuk mengakses catatan kuliah.")
    else:
        st.title("📒 Catatan Kuliah")
        # Pilihan tingkat langsung muncul (pakai radio horizontal)
        tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"], horizontal=True)

        # Dropdown blok
        blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
        
        # Dropdown mata kuliah
        matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])
        
        # Menampilkan catatan sesuai pilihan
        st.subheader(f"📘 Catatan untuk {matkul} - {tingkat} {blok}")
        st.info("Belum ada catatan yang ditambahkan.")
        
        # Halaman Riwayat Jawaban
        if menu == "Riwayat Jawaban":
            st.title("🗂️ Riwayat Jawaban")
            st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")
            if not st.session_state.is_logged_in:
                 st.warning("Anda harus login untuk mengakses halaman ini.")

# Halaman Tentang
if menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
    st.header("Tentang Pendiri")
    st.write("Zulfikar Syahid")
    st.write("Rizmi Maitri Nurgianti")
    st.write("Nafisah Nailalhusna I.")
    st.write("Jane Lazarina Bora Isu")
