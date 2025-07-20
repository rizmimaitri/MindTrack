import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda 🏠", "Latihan Soal ✏", "Catatan Kuliah 📒", "Tentang ℹ"])

# Data Soal
soal_data = {
    "Spektrofotometri 🧪": [
        {"question": "Perbedaan metode analisis secara konvensional dan analisis intrumen adalah sebagai berikut, kecuali ?", "options": ["Metode analisis instrumen digunakan untuk analit dengan konsentrasi rendah, sedangkan metode analisis konvensional digunakan untuk analit konsentrasi tinggi", "Metode analisis instrumen membutuhkan standar sedangkan metode analis konvensional tidak ", "Metode analisis instrumen membutuhkan pemisahan analit secara fisik sedangkan metode analis konvensional tidak ","Metode analisis instrumen memiliki sensitivitas lebih tinggi dengan metode analis konvensional"], "answer": "Metode analisis instrumen membutuhkan pemisahan analit secara fisik sedangkan metode analis konvensional tidak "},
        {"question": "Jika transmita suatu larutan adalah 19.4% maka absorbansi larutan tersebut adalah?", "options": [" 1.288 ", "1,404 ", "0,806 ","0,712"], "answer": "0,712"},
        {"question": "Apa itu panjang gelombang?", "options": ["Jarak antara dua puncak gelombang", "Jumlah gelombang per detik", "Energi cahaya"], "answer": "Jarak antara dua puncak gelombang"},
        {"question": "Apa yang dimaksud dengan absorbansi?", "options": ["Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Jumlah cahaya yang diserap"},
        {"question": "Apa itu hukum Beer-Lambert?", "options": ["Hubungan antara konsentrasi dan absorbansi", "Hubungan antara suhu dan tekanan", "Hubungan antara volume dan massa"], "answer": "Hubungan antara konsentrasi dan absorbansi"},
        {"question": "Apa yang dimaksud dengan spektrometer?", "options": ["Alat untuk mengukur suhu", "Alat untuk mengukur cahaya", "Alat untuk mengukur tekanan"], "answer": "Alat untuk mengukur cahaya"},
        {"question": "Apa itu fotodetektor?", "options": ["Alat untuk menghasilkan cahaya", "Alat untuk mendeteksi cahaya", "Alat untuk menyimpan cahaya"], "answer": "Alat untuk mendeteksi cahaya"},
        {"question": "Apa yang dimaksud dengan transmittance?", "options": ["Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Jumlah cahaya yang diteruskan"},
        {"question": "Apa itu larutan standar?", "options": ["Larutan dengan konsentrasi yang diketahui", "Larutan dengan pH yang diketahui", "Larutan dengan suhu yang diketahui"], "answer": "Larutan dengan konsentrasi yang diketahui"},
        {"question": "Apa yang dimaksud dengan kalibrasi?", "options": ["Proses mengukur suhu", "Proses mengukur konsentrasi", "Proses menyesuaikan alat ukur"], "answer": "Proses menyesuaikan alat ukur"},
        {"question": "Apa itu spektrum?", "options": ["Rentang panjang gelombang", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Rentang panjang gelombang"},
        {"question": "Apa yang dimaksud dengan fotometri?", "options": ["Ilmu tentang cahaya", "Ilmu tentang suara", "Ilmu tentang suhu"], "answer": "Ilmu tentang cahaya"},
        {"question": "Apa itu sumber cahaya?", "options": ["Alat untuk mengukur cahaya", "Alat untuk menghasilkan cahaya", "Alat untuk menyimpan cahaya"], "answer": "Alat untuk menghasilkan cahaya"},
        {"question": "Apa yang dimaksud dengan panjang gelombang maksimum?", "options": ["Panjang gelombang dengan absorbansi tertinggi", "Panjang gelombang dengan suhu tertinggi", "Panjang gelombang dengan tekanan tertinggi"], "answer": "Panjang gelombang dengan absorbansi tertinggi"},
        {"question": "Apa itu larutan sampel?", "options": ["Larutan yang akan diuji", "Larutan yang digunakan untuk kalibrasi", "Larutan yang digunakan untuk mencuci alat"], "answer": "Larutan yang akan diuji"},
        {"question": "Apa yang dimaksud dengan noise dalam spektrofotometri?", "options": ["Gangguan pada sinyal", "Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap"], "answer": "Gangguan pada sinyal"},
        {"question": "Apa itu resolusi dalam spektrofotometri?", "options": ["Kemampuan alat untuk membedakan panjang gelombang", "Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap"], "answer": "Kemampuan alat untuk membedakan panjang gelombang"},
        {"question": "Apa yang dimaksud dengan fotometri UV-Vis?", "options": ["Pengukuran cahaya ultraviolet dan tampak", "Pengukuran cahaya inframerah", "Pengukuran cahaya mikro"], "answer": "Pengukuran cahaya ultraviolet dan tampak"},
        {"question": "Apa itu cuvette?", "options": ["Wadah untuk larutan", "Alat untuk mengukur suhu", "Alat untuk mengukur tekanan"], "answer": "Wadah untuk larutan"},
        {"question": "Apa yang dimaksud dengan efek sel?", "options": ["Perubahan absorbansi akibat konsentrasi", "Perubahan suhu akibat cahaya", "Perubahan tekanan akibat cahaya"], "answer": "Perubahan absorbansi akibat konsentrasi"},
        {"question": "Apa itu spektrofotometer UV-Vis?", "options": ["Alat untuk mengukur cahaya ultraviolet dan tampak", "Alat untuk mengukur suhu", "Alat untuk mengukur tekanan"], "answer": "Alat untuk mengukur cahaya ultraviolet dan tampak"},
        {"question": "Metode analisis instrumen yang menggunakan prinsip hamburan cahaya (scattering of radiation) adalah?", "options": ["Flamefotometri", "Polarimeteri", "Turbidimetri"], "answer": "Turbidimetri"},
        {"question": "Jika suatu materi dikenai radiasi sinar gamma maka yang terjadi adalah?", "options": ["Vibrasi molekul", "Eksitasi elektron pada kulit yang paling dalam", "Eksitasi inti"], "answer": "Eksitasi inti"},
        {"question": "Diantara senyawa berikut yang memiliki seapan pada panjang gelombang yang tertinggi adalah...", "options": ["Metanol", "Heksana", "Aseton"], "answer": "Heksana"},
        {"question": "Detektor dibawah ini manakah yang merupakan detektor yang digunakan pada spektrofotometer?", "options": ["Detektor PMT(Photo Multiplier Tube)", "Detektor FID(Flame Ionization Detector)", "Detektor TCD(Thermal Conductivity Detector"], "answer": "Detektor PMT (Photo Multiplier Tube)"},
        {"question": "Jika absorbans sampel 0,007 maka berapa nilai % T?", "options": ["2,00", "20,00", "11,22"], "answer": "20,00"},
        {"question": "Pernyataan yang benar tentang persamaan Lambert Beer adalah...", "options": ["Absorptivitas molar tidak dipengaruhi oleh konsentrasi", "Menunjukkan hubungan linier antara absorptivitas dengan konsentrasi", "Menunjukkan hubungan linier antara tebal media dengan konsentrasi"], "answer": "Menunjukkan hubungan linier antara absorptivitas dengan konsentrasi"},
        {"question": "kuvet yang digunakan untuk analisis spektrofotometri harus memiliki syarat syarat sebagaimana berikut,kecuali...", "options": ["Harus tahan api/panas yang tinggi", "Permukaannya secara optis benar benar sejajar", "Tidak menyerap daerah pengukuran"], "answer": "Harus tahan api/panas yang tinggi"},
        {"question": "Penyimpangan Hukum Lambert Beer dapat disebabkan oleh hal berikut,kecuali...", "options": ["Adanya sesatan cahaya", "Konsentrasi contoh terlalu tinggi", "Terdapat reaksi kesetimbangan namun tidak menjadi pergeseran arah reaksi"], "answer": "Terdapat reaksi kesetimbangan namun tidak menjadi pergeseran arah reaksi"},
    ],
    "Kimia Fisika 🔬": [
        {"question": "Apa hukum pertama termodinamika?", "options": ["Energi dapat diciptakan","Energi tidak dapat diciptakan atau dimusnahkan", "Energi tidak dapat diciptakan atau dimusnahkan", "Energi selalu meningkat"], "answer": "Energi tidak dapat diciptakan atau dimusnahkan"},
        {"question": "Apa itu entropi?", "options": ["Ukuran ketidakteraturan", "Ukuran energi", "Ukuran massa"], "answer": "Ukuran ketidakteraturan"},
        {"question": "Apa yang dimaksud dengan energi potensial?", "options": ["Energi yang dimiliki benda karena posisinya", "Energi yang dimiliki benda karena gerakannya", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang dimiliki benda karena posisinya"},
        {"question": "Apa itu energi kinetik?", "options": ["Energi yang dimiliki benda karena gerakannya", "Energi yang dimiliki benda karena posisinya", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang dimiliki benda karena gerakannya"},
        {"question": "Apa yang dimaksud dengan hukum kedua termodinamika?", "options": ["Energi tidak dapat diciptakan atau dimusnahkan","Energi selalu mengalir dari yang panas ke yang dingin", "Energi selalu meningkat"], "answer": "Energi selalu mengalir dari yang panas ke yang dingin"},
        {"question": "Apa itu kalor?", "options": ["Energi yang berpindah karena perbedaan suhu", "Energi yang dihasilkan oleh reaksi kimia", "Energi yang dimiliki benda karena posisinya"], "answer": "Energi yang berpindah karena perbedaan suhu"},
        {"question": "Apa yang dimaksud dengan sistem tertutup?", "options": ["Sistem yang tidak dapat bertukar energi dengan lingkungan", "Sistem yang dapat bertukar energi dengan lingkungan", "Sistem yang tidak dapat bertukar materi dengan lingkungan"], "answer": "Sistem yang tidak dapat bertukar energi dengan lingkungan"},
        {"question": "Apa itu reaksi eksotermik?", "options": ["Reaksi yang menyerap energi","Reaksi yang melepaskan energi", "Reaksi yang tidak melibatkan energi"], "answer": "Reaksi yang melepaskan energi"},
        {"question": "Apa yang dimaksud dengan reaksi endotermik?", "options": ["Reaksi yang melepaskan energi", "Reaksi yang menyerap energi", "Reaksi yang tidak melibatkan energi"], "answer": "Reaksi yang menyerap energi"},
        {"question": "Apa itu hukum kekekalan energi?", "options": ["Energi tidak dapat diciptakan atau dimusnahkan", "Energi dapat diciptakan", "Energi selalu meningkat"], "answer": "Energi tidak dapat diciptakan atau dimusnahkan"},
        {"question": "Apa yang dimaksud dengan tekanan?", "options": ["Energi per satuan volume", "Massa per satuan volume","Gaya per satuan luas"], "answer": "Gaya per satuan luas"},
        {"question": "Apa itu volume?", "options": ["Ruang yang ditempati oleh suatu benda", "Massa per satuan luas", "Energi per satuan volume"], "answer": "Ruang yang ditempati oleh suatu benda"},
        {"question": "Apa yang dimaksud dengan suhu?", "options": ["Ukuran massa", "Ukuran energi kinetik rata-rata partikel", "Ukuran volume"], "answer": "Ukuran energi kinetik rata-rata partikel"},
        {"question": "Apa itu gas ideal?", "options": ["Gas yang tidak memiliki volume", "Gas yang tidak dapat ditekan","Gas yang mengikuti hukum gas ideal"], "answer": "Gas yang mengikuti hukum gas ideal"},
        {"question": "Apa yang dimaksud dengan hukum Boyle?", "options": ["Tekanan berbanding terbalik dengan volume pada suhu tetap", "Tekanan berbanding lurus dengan volume pada suhu tetap", "Volume berbanding lurus dengan suhu pada tekanan tetap"], "answer": "Tekanan berbanding terbalik dengan volume pada suhu tetap"},
        {"question": "Apa itu hukum Charles?", "options": ["Volume berbanding lurus dengan suhu pada tekanan tetap", "Tekanan berbanding terbalik dengan volume pada suhu tetap", "Volume berbanding terbalik dengan tekanan pada suhu tetap"], "answer": "Volume berbanding lurus dengan suhu pada tekanan tetap"},
        {"question": "Apa yang dimaksud dengan hukum Avogadro?", "options": ["Volume gas berbanding lurus dengan jumlah mol pada suhu dan tekanan tetap", "Tekanan berbanding terbalik dengan volume pada suhu tetap", "Volume berbanding lurus dengan suhu pada tekanan tetap"], "answer": "Volume gas berbanding lurus dengan jumlah mol pada suhu dan tekanan tetap"},
        {"question": "Apa itu energi bebas Gibbs?", "options": ["Energi yang tersedia untuk melakukan kerja", "Energi yang tidak dapat digunakan", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang tersedia untuk melakukan kerja"},
        {"question": "Apa yang dimaksud dengan reaksi redoks?", "options": ["Reaksi yang melibatkan transfer elektron", "Reaksi yang tidak melibatkan transfer elektron", "Reaksi yang melibatkan perubahan suhu"], "answer": "Reaksi yang melibatkan transfer elektron"},
        {"question": "Apa itu katalis?", "options": [ "Zat yang memperlambat reaksi","Zat yang mempercepat reaksi tanpa ikut bereaksi", "Zat yang tidak berpengaruh pada reaksi"], "answer": "Zat yang mempercepat reaksi tanpa ikut bereaksi"},
        {"question": "Apa yang dimaksud dengan pH?", "options": ["Ukuran konsentrasi", "Ukuran energi", "Ukuran keasaman atau kebasaan suatu larutan"], "answer": "Ukuran keasaman atau kebasaan suatu larutan"},
    ],
    "Biokimia 🧬": [
        {"question": "Apa itu enzim?", "options": ["Katalisator biologis","Zat pewarna", "Zat pengawet"], "answer": "Katalisator biologis"},
        {"question": "Apa yang dimaksud dengan metabolisme?", "options": ["Proses pembentukan energi", "Proses pengolahan limbah", "Proses penguraian makanan",], "answer": "Proses penguraian makanan"},
        {"question": "Apa itu asam amino?", "options": ["Penyusun karbohidrat", "Penyusun protein",  "Penyusun lemak"], "answer": "Penyusun protein"},
        {"question": "Apa yang dimaksud dengan DNA?", "options": ["Zat pewarna", "Zat pengawet", "Materi genetik"], "answer": "Materi genetik"},
        {"question": "Apa itu RNA?", "options": ["Asam deoksiribonukleat", "Asam ribonukleat", "Asam amino"], "answer": "Asam ribonukleat"},
        {"question": "Apa yang dimaksud dengan glukosa?", "options": ["Lemak", "Protein", "Karbohidrat sederhana"], "answer": "Karbohidrat sederhana"},
        {"question": "Apa itu lipid?", "options": ["Zat yang larut dalam air", "Zat yang tidak larut dalam air", "Zat yang tidak berfungsi dalam tubuh"], "answer": "Zat yang tidak larut dalam air"},
        {"question": "Apa yang dimaksud dengan karbohidrat?", "options": ["Sumber energi utama", "Sumber protein", "Sumber lemak"], "answer": "Sumber energi utama"},
        {"question": "Apa itu protein?", "options": ["Sumber energi","Penyusun sel", "Zat pewarna"], "answer": "Penyusun sel"},
        {"question": "Apa yang dimaksud dengan metabolisme anaerob?", "options": ["Proses metabolisme tanpa oksigen", "Proses metabolisme dengan oksigen", "Proses metabolisme dengan suhu tinggi"], "answer": "Proses metabolisme tanpa oksigen"},
        {"question": "Apa itu fotosintesis?", "options": ["Proses pembentukan glukosa dari cahaya", "Proses penguraian glukosa", "Proses pembentukan energi dari lemak"], "answer": "Proses pembentukan glukosa dari cahaya"},
        {"question": "Apa yang dimaksud dengan respirasi seluler?", "options": ["Proses penguraian glukosa untuk menghasilkan energi", "Proses pembentukan glukosa", "Proses penguraian lemak"], "answer": "Proses penguraian glukosa untuk menghasilkan energi"},
        {"question": "Apa itu ATP?", "options": ["Molekul penyimpan lemak", "Molekul penyimpan protein", "Molekul penyimpan energi"], "answer": "Molekul penyimpan energi"},
        {"question": "Apa yang dimaksud dengan enzim katalase?", "options": ["Enzim yang menguraikan hidrogen peroksida", "Enzim yang menguraikan glukosa", "Enzim yang menguraikan lemak"], "answer": "Enzim yang menguraikan hidrogen peroksida"},
        {"question": "Apa itu hormon?", "options": ["Zat penyusun sel", "Zat pengatur dalam tubuh", "Zat penyimpan energi"], "answer": "Zat pengatur dalam tubuh"},
        {"question": "Apa yang dimaksud dengan asam lemak?", "options": [ "Penyusun protein", "Penyusun lipid", "Penyusun karbohidrat"], "answer": "Penyusun lipid"},
        {"question": "Apa itu glikogen?", "options": ["Cadangan energi pada tumbuhan", "Cadangan energi pada bakteri", "Cadangan energi pada hewan"], "answer": "Cadangan energi pada hewan"},
        {"question": "Apa yang dimaksud dengan sel?", "options": ["Unit dasar kehidupan", "Unit dasar energi", "Unit dasar protein"], "answer": "Unit dasar kehidupan"},
        {"question": "Apa itu biokimia?", "options": ["Ilmu tentang reaksi kimia dalam makhluk hidup", "Ilmu tentang reaksi fisika", "Ilmu tentang reaksi kimia dalam benda mati"], "answer": "Ilmu tentang reaksi kimia dalam makhluk hidup"},
        {"question": "Apa yang dimaksud dengan metabolisme aerob?", "options": ["Proses metabolisme dengan oksigen", "Proses metabolisme tanpa oksigen", "Proses metabolisme dengan suhu tinggi"], "answer": "Proses metabolisme dengan oksigen"},
        {"question": "Apa itu enzim amilase?", "options": ["Enzim yang menguraikan protein", "Enzim yang menguraikan karbohidrat", "Enzim yang menguraikan lemak"], "answer": "Enzim yang menguraikan karbohidrat"},
    ],
    "Fisika ⚛": [
        {"question": "Perpindahan, kecepatan, percepatan, dan gaya termasuk besaran?", "options": ["Skalar", "Vektor", "Turunan","Satuan","Utama"], "answer": "Vektor"},
        {"question": "Daya adalah ?", "options": ["Joule/sekon", "Joule.sekon", "Newton/sekon","Newton.sekon","Joule"], "answer": "Joule/sekon"},
        {"question": "Dua lembah dan dua bukit gelombang sama dengan?", "options": ["1/2 lambda", "1 lambda", "1,5 lambda","2 lambda","2,5 lambda"], "answer": "2 lambda"}, 
        {"question": "Diantara besaran dibawah ini, manakah yang termasuk besaran pokok ?", "options": ["Kecepatan", "Percepatan", "Jumlah zat","Kadar","Energi"], "answer": "Jumlah zat"},
        {"question": "Pada kasus benda jatuh, energi yang besarnya semakin berkurang adalah?", "options": ["Energi potensial", "Energi kinetik", "Energi gerak","Energi  gesekan","Energi mekanik"], "answer": "Energi potensial"},
        {"question": "Usaha yang dilakukan oleh gaya gesek selalu bernilai?", "options": ["Positif", "Negatif", "Tergantung kemiringan","Tergantung sudut","Nol"], "answer": "Negatif"},
        {"question": "Penulisan simbol yang benar untuk satuan mililiter yaitu?", "options": ["ml", "mL", "Ml","ML","mLiter"], "answer": "mL"},
        {"question": "Perbandingan massa benda terhadap volume benda disebut?", "options": ["Berat jenis", "Bobot jenis", "Massa jenis","Massa jenis relative","Specific gravity"], "answer": "Massa jenis"},
        {"question": "Gerak harmonis sederhana memiliki amplitudo yang besarnya?", "options": ["Selalu sama", "Selalu bertambah besar", "Selalu berkurang","Tergantung massa beban","Selalu berubah ubah"], "answer": "Selalu sama"},
        {"question": "Jika gaya berat benda lebih besar dari gaya apung maka benda akan?", "options": ["Terapung seluruhnya", "Terapung sebagian", "Melayang diatas","Melayang ditengah","Tenggelam di dasar"], "answer": "Tenggelam di dasar"},
        {"question": "Pernyataan di bawah ini yang bukan syarat pasangan gaya bisa disebut aksi reaksi yaitu?", "options": ["Berlawanan arah", "Sama besar", "Bekerja pada benda yang sama","Bekerja pada benda yang berbeda","Semua jawaban benar"], "answer": "Sama besar"},
        {"question": "Diantara besarab besaran berikut, manakah yang tidak terkait dengan kinematika?", "options": ["Perpindahan", "Waktu", "Percepatan","Gaya","Kecepatan"], "answer": "Gaya"},
        {"question": "Prinsip.... menyatakan bahwa tekanan yang diberikan pada fluida tertutup akan diteruskan sama besar ke segala arah", "options": ["Pascal", "Bernoulli", "Archimedes","Tegangan permukaan","Viskositas"], "answer": "Pascal"},
        {"question": "Penyebab perubahan gerak benda adalah?", "options": ["Usaha", "Gaya", "Energi","Percepatan","Kecepatan"], "answer": "Gaya"},
        {"question": "Suatu thermometer menunjukan suhu 30 Celcius, berapakah dinyatakan dalam skala fahrenheit?", "options": ["78", "54", "86","77","90"], "answer": "86"},
    ]
}

#Judul Matkul dan Materi Catatan
materi_titles = {
    "Kimia Fisika 🔬": {
        1: "Gas Ideal dan Gas Nyata",
        2: "Hukum Thermodinamika"
    },
    "Spektrofotometri 🧪": {
        1: "Spektrofotometri Infrared",
        2: "Flame Photometry",
        3: "ICP AES"
    },
    "Biokimia 🧬": {
        1: "Karbohidrat",
        2: "Protein",
        3: "Enzim"
    }
}


# Halaman Beranda
if menu == "Beranda 🏠":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di MindTrack, 👋")
    st.write("Sudah Siap Untuk Mulai Belajar?")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

elif menu == "Latihan Soal ✏":
    st.title("✏ Latihan Soal")

    # Pilih Mata Kuliah
    matkul = st.selectbox("Pilih Mata Kuliah", ["Spektrofotometri 🧪", "Kimia Fisika 🔬", "Biokimia 🧬", "Fisika ⚛"])

    # Tampilkan Soal Berdasarkan Mata Kuliah
    st.subheader(f"Soal {matkul}")
    jawaban = []
    for index, soal in enumerate(soal_data[matkul]):
        st.subheader(f"{index + 1}. {soal['question']}")
        jawaban.append(st.radio("Pilih jawaban:", soal["options"], key=f"soal_{matkul}_{index}"))

    # TOMBOL KIRIM
    if st.button("✅ Kirim Jawaban"):
        st.success("Jawaban kamu berhasil dikirim!")
        # Koreksi otomatis
        skor = 0
        for index, soal in enumerate(soal_data[matkul]):
            if jawaban[index] == soal["answer"]:
                skor += 1
            else:
                # Tampilkan jawaban yang benar jika salah
                st.error(f"Jawaban kamu untuk soal {index + 1} salah. Jawaban yang benar adalah: {soal['answer']}")

        # Tampilkan hasil
        st.markdown(f"### 🏆 Skor Akhir: {skor}/{len(soal_data[matkul])}")

# Catatan Kuliah
elif menu == "Catatan Kuliah 📒":
    st.title("📒 Catatan Kuliah")

    # Inisialisasi session_state jika belum ada
    if "selected_matkul_simple" not in st.session_state:
        st.session_state.selected_matkul_simple = None
    if "selected_pertemuan_simple" not in st.session_state:
        st.session_state.selected_pertemuan_simple = None
        
    # Dropdown Mata Kuliah
    matkul_options = list(materi_titles.keys())
    selected_matkul = st.selectbox("Pilih Mata Kuliah", matkul_options, key="matkul_dropdown_simple")
    
    # Jika mata kuliah dipilih (saat selectbox berubah)
    if selected_matkul != st.session_state.selected_matkul_simple:
        st.session_state.selected_matkul_simple = selected_matkul
        st.session_state.selected_pertemuan_simple = None # Reset pertemuan jika matkul berubah
    
    # Tampilkan tombol pertemuan hanya jika mata kuliah sudah dipilih
    if st.session_state.selected_matkul_simple:
        st.subheader(f"Catatan untuk {st.session_state.selected_matkul_simple}")
        st.markdown("---")
        st.write("Pilih Materi Pertemuan:")
        
        # Mendapatkan judul materi untuk mata kuliah yang sedang dipilih
        current_matkul_titles = materi_titles.get(st.session_state.selected_matkul_simple, {})
        
        # Menentukan berapa banyak kolom yang dibutuhkan berdasarkan jumlah pertemuan
        num_pertemuan = len(current_matkul_titles)
        cols = st.columns(num_pertemuan if num_pertemuan > 0 else 1) # Buat kolom sebanyak jumlah pertemuan
    
        # Loop melalui nomor pertemuan yang ada untuk mata kuliah ini
        sorted_pertemuan_nums = sorted(current_matkul_titles.keys()) 
        
        for idx, pertemuan_num in enumerate(sorted_pertemuan_nums):
            with cols[idx]: # Menggunakan indeks untuk menempatkan tombol di kolom yang berbeda
                button_label = current_matkul_titles.get(pertemuan_num, f"Pertemuan {pertemuan_num}")
                
                def set_pertemuan_simple_callback(p_num): # Ganti nama fungsi callback agar tidak bentrok
                    st.session_state.selected_pertemuan_simple = p_num
                
                st.button(button_label, key=f"materi_btn_simple_{pertemuan_num}", on_click=set_pertemuan_simple_callback, args=(pertemuan_num,))
    
        # Menampilkan Konten Pertemuan
        if st.session_state.selected_pertemuan_simple:
            st.markdown("---")
            konten_subheader_title = current_matkul_titles.get(st.session_state.selected_pertemuan_simple, f"Konten Pertemuan {st.session_state.selected_pertemuan_simple}")
            st.subheader(f"Konten: {konten_subheader_title}")
            st.write(f"Ini adalah detail untuk {st.session_state.selected_matkul_simple} - {konten_subheader_title}.")
            
            # --- BAGIAN KONTEN DAN GAMBAR ---
            if st.session_state.selected_matkul_simple == "Kimia Fisika 🔬":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Gas Ideal dan Gas Nyata")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_3.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_4.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_5.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250708_103057_6.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250718_152601_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Notes_250718_152601_2.jpg")
                    
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Hukum Thermodinamika")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_3.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_4.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_5.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Hukum%20Termodinamika_6.jpg")    
                    
            elif st.session_state.selected_matkul_simple == "Spektrofotometri 🧪":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Spektrofotometri Infrared")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_3.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_4.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_5.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/FTIR_6.jpg")
                    
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Flame Photometry")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Flame_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Flame_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Flame_3.jpg")
                    
                elif st.session_state.selected_pertemuan_simple == 3:
                    st.write("ICP AES")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/ICP_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/ICP_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/ICP_3.jpg")
            
            elif st.session_state.selected_matkul_simple == "Biokimia 🧬":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Karbohidrat")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Karbo_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Karbo_2.jpg")
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Protein")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Protein_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Protein_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Protein_3.jpg")
                elif st.session_state.selected_pertemuan_simple == 3:
                    st.write("Enzim")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Enzim_1.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Enzim_2.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Enzim_3.jpg")
                    st.image("https://raw.githubusercontent.com/fiikar/copy-projek/main/Enzim_4.jpg")
        else:
            st.info("Silakan pilih materi pertemuan di atas untuk melihat detail.")
    else:
        st.info("Silakan pilih mata kuliah di atas.")

# Halaman Tentang
elif menu == "Tentang ℹ":
    st.title("ℹTentang MindTrack")
    st.write("MindTrack adalah sebuah web yang dirancang untuk membantu mahasiswa khusunya di lingkungan Politeiknik AKA Bogor dalam memahami konsep-konsep penting di mata kuliah teori.")
    
    st.header("Tujuan Aplikasi")
    st.write("""
        Aplikasi ini bertujuan untuk:
        - Menyediakan latihan soal yang bervariasi untuk meningkatkan pemahaman.
        - Menyediakan catatan kuliah yang mudah diakses untuk membantu dalam belajar.
        - Membantu mempersiapkan diri untuk menghadapi UTS maupun UAS 
        """)
    
    st.header("Fitur Utama")
    st.write("""
        - *Latihan Soal*: Pengguna dapat memilih mata kuliah dan menjawab soal-soal yang telah disediakan.
        - *Catatan Kuliah*: Pengguna dapat mengakses catatan kuliah yang relevan dengan mata kuliah yang dipilih.
    """)
    
    st.header("Tim Pengembang")
    st.write("""
        Aplikasi ini dikembangkan oleh:
        - *Zulfikar Syahid.*
        - *Rizmi Maitri Nurgianti.*
        - *Nafisah Nailalhusna Isbandi.*
        - *Jane Lazarina Bora Isu.*
    """)
    
    st.header("Kontak")
    st.write("""
        Jika Anda memiliki pertanyaan atau masukan, silakan hubungi kami di:
        - Email: zulfikarsyahid20@gmail.com
    """)
    
    st.write("Terima kasih telah menggunakan MindTrack! Selamat belajar! 🎉")
