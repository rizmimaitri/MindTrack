import streamlit as st

st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Sidebar menu
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
import pandas as pd

if menu == "Beranda":
    st.title("🧠 MindTrack")

    if "halaman" not in st.session_state:
        st.session_state.halaman = "login"
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False

    def load_users():
        try:
            df = pd.read_csv("users.csv")
            return df
        except:
            return pd.DataFrame(columns=["nama_lengkap", "nama_panggilan", "nim", "password"])

    users_df = load_users()

    if not st.session_state.is_logged_in:

        if st.session_state.halaman == "login":
            st.subheader("🔐 Masuk")
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
                else:
                    st.warning("Akun tidak ditemukan. Silakan daftar terlebih dahulu.")
                    st.session_state.halaman = "daftar"

        elif st.session_state.halaman == "daftar":
            st.subheader("📝 Daftar Akun Baru")
            nama_lengkap = st.text_input("Nama Lengkap")
            nama_panggilan = st.text_input("Nama Panggilan (opsional)")
            nim = st.text_input("NIM")
            password = st.text_input("Password", type="password")

            if st.button("Daftar"):
                if nama_lengkap.strip() == "" or nim.strip() == "" or password.strip() == "":
                    st.warning("Nama lengkap, NIM, dan password wajib diisi.")
                elif nama_lengkap in users_df["nama_lengkap"].values:
                    st.warning("Nama sudah terdaftar. Silakan login.")
                    st.session_state.halaman = "login"
                else:
                    new_data = pd.DataFrame([{
                        "nama_lengkap": nama_lengkap,
                        "nama_panggilan": nama_panggilan if nama_panggilan.strip() else nama_lengkap.split()[0],
                        "nim": nim,
                        "password": password
                    }])
                    new_df = pd.concat([users_df, new_data], ignore_index=True)
                    new_df.to_csv("users.csv", index=False)
                    st.success("Pendaftaran berhasil! Silakan login.")
                    st.session_state.halaman = "login"

            st.button("Sudah punya akun? Masuk", on_click=lambda: st.session_state.update({"halaman": "login"}))

    else:
        st.success(f"Halo, Selamat Datang Di MindTrack {st.session_state.nama_panggilan}! 👋")
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
