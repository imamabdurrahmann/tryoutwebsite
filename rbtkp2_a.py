import json

questions = [
    # === PELAYANAN PUBLIK (8) ===
    {
        "id": "tkp2_001", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda seorang kepala dinas di sebuah Pemerintah Daerah yang sedang menghadapi situasi kritis: seorang pengusaha besar yang merupakan investor utama di daerah Anda menuntut percepatan perizinan untuk proyek infrastruktur besar yang akan menyerap ribuan tenaga kerja. Namun proses AMDAL proyek tersebut baru mencapai 60% dan temuan awal menunjukkan potensi dampak lingkungan yang signifikan di daerah resapan air. Di saat yang sama, Anda mendapat informasi bahwa pengusaha tersebut memiliki hubungan dekat dengan seorang pejabat tinggi di pemerintah pusat yang secara implisit sudah memberikan dukungan terhadap proyek ini. Masyarakat sekitar lokasi proyek mulai mempertanyakan komitmen pemerintah terhadap lingkungan. Investigation internal terhadap prosedur perizinan yang berjalan selama ini juga menunjukkan beberapa irregularities yang berpotensi melanggar aturan. Waktu Anda terbatas dan tekanan dari berbagai arah sangat kuat. Sebagai kepala dinas yang bertanggung jawab atas perizinan dan lingkungan, langkah Anda adalah...",
        "options": [
            "Proses perizinan dipercepat dan izin dikeluarkan segera karena proyek akan menciptakan ribuan lapangan kerja dan dukungan dari pejabat tinggi pusat merupakan legitimasi yang cukup",
            "Izin ditunda sampai AMDAL selesai 100%, sampaikan kepada pengusaha bahwa regulasi lingkungan tidak bisa dikompromikan dan proses harus berjalan sesuai prosedur, namun jaga komunikasi tetap diplomatis",
            "Buat izin bersyarat yang mewajibkan pengusaha melakukan pemulihan lingkungan menyeluruh sebagai bagian dari persyaratan izin, dengan timeline yang tegas dan mekanisme monitoring independent",
            "Serahkan keputusan final kepada pengusaha: apakah mereka mau menunggu AMDAL selesai atau memilih membatalkan proyek, karena Anda tidak ingin menanggung risiko dari kedua pilihan",
            "Buat keputusan berdasarkan hasil voting internal tim Anda karena keputusan kolektif lebih aman jika kemudian terjadi masalah"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan keseimbangan antara tanggung jawab lingkungan dan kebutuhan ekonomi. Izin bersyarat bukan penundaan yang merugikan investasi, bukan penolakan tanpa dasar, bukan pelepasan tanggung jawab, bukan keputusan yang menghindari risiko. Instrumen izin bersyarat dengan kewajiban pemulihan lingkungan adalah praktik terbaik dalam perizinan berkelanjutan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_002", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola unit pelayanan publik di sebuah kabupaten yang sedang melakukan digitalisasi layanan. Setelah 6 bulan implementasi, data menunjukkan bahwa layanan digital memang meningkat efisiensinya untuk kelompok usia produktif, namun terjadi peningkatan signifikan的人数 pengaduan dari lansia, penyandang disabilitas, dan warga di daerah terpencil yang tidak memiliki akses internet yang memadai. Beberapa warga lansia bahkan sampai tidak bisa mengakses layanan dasar karena tidak mampu menggunakan aplikasi digital. Di saat yang sama, anggaran untuk维持 layanan 非digital sudah dipangkas untuk mendanai digitalisasi. Pejabat yang membidangi transformation digital meminta agar semua layanan sepenuhnya migrated ke digital dalam 3 bulan ke depan. Kondisi Anda sangat rumit: efisiensi digital versus aksesibilitas universal, tekanan politik versus kebutuhan riil warga. Posisi Anda adalah...",
        "options": [
            "Dukung migrasi penuh ke digital sesuai permintaan pejabat karena transformasi digital adalah arah kebijakan pemerintah dan aksesibilitas adalah urusan masing-masing warga untuk beradaptasi",
            "Berikan perpanjangan deadline migrasi digital selama 6 bulan lagi sambil secara agresif meningkatkan program pelatihan digital literacy untuk warga yang kesulitan, dengan resources yang dialokasikan secara proporsional dari efisiensi digital",
            "Kembalikan semua layanan ke 非digital karena digitalisasi jelas merugikan kelompok rentan dan efisiensi tidak boleh mengorbankan keadilan akses",
            "Biarkan warga memilih sendiri channel layanan yang mereka mau, digital atau 非digital, dan lihat numbers saja tanpa intervensi apapun",
            "Serahkan keputusan kepada pejabat transformation digital karena Anda tidak memiliki expertise untuk menilai apakah digitalisasi sudah waktunya atau belum"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan yang pragmatis dan inklusif: mendukung transformasi digital tapi dengan timeline yang realistic dan investasi konkret pada literasi digital warga. Pendekatan ini tidak menolak perubahan tapi memastikan perubahan tidak meninggalkan siapa pun. Bukan A yang tidak peka terhadap aksesibilitas, bukan C yang regressive, bukan D yang pasif, bukan E yang menghindari tanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_003", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda kepala bagian pelayanan masyarakat di sebuah pemerintah kota yang sedang menghadapi krisis kepercayaan publik. Selama 3 bulan terakhir, media memberitakan serangkaian kasus di mana warga mengalami difficulties mengakses layanan dasar: perbaikan KTP yang memakan waktu berbulan-bulan, layanan kesehatan yang menolak pasien karena masalah administrasi, dan pengurusan izin usaha yang korup. Setiap kasus adalah nyata dan terdokumentasi dengan baik. Kondisi ini diperumit oleh fakta bahwa beberapa kasus melibatkan staf Anda personally, dan Anda tahu bahwa setidaknya satu kasus melibatkan staf yang memiliki hubungan keluarga dengan pejabat daerah yang powerful. Anda tidak memiliki bukti tertulis tentang KKN tapi ada enough circumstantial evidence. Investigation formal akan memakan waktu lama dan mungkin tidak menghasilkan anything definitif. Namun ketidakpuasan publik terus meningkat dan media watching closely. Anda dalam posisi yang...",
        "options": [
            "Lakukan investigation internal secara menyeluruh, jika ditemukan staf yang terbukti melakukan maladministration, proses sesuai hukum tanpa pandang bulu termasuk staf yang memiliki koneksi politik, dan sampaikan hasilnya kepada publik secara transparan",
            "Diam saja sampai investigation selesai dan hindari komentar apapun ke media karena berbicara terlalu cepat bisa merugikan pihak yang tidak bersalah",
            "Pindahkan staf yang terlibat ke posisi lain yang tidak berhadapan langsung dengan publik, namun jangan dilakukan proses hukum karena akan menimbulkan 更多 problemas dengan pejabat yang connected",
            "Buat pernyataan publik bahwa Anda personally bertanggung jawab atas semua failures dan akan memastikan perbaikan sistem secara menyeluruh, tanpa memberikan detail tentang kasus individual karena itu adalah privacy matters",
            "Serahkan semua kasus kepada police karena maladministration yang melibatkan pejabat daerah dan KKN adalah tindak pidana yang harus ditangani olehAPH bukan oleh internal government"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas tertinggi: tidak menutupi masalah, tidak melindungi siapa pun karena koneksi politik, dan merespons dengan transparency terhadap publik. Investigation menyeluruh memastikan fakta di meja sebelum action diambil. Bukan B yang pasif dan membiarkan krisis kepercayaan berlanjut, bukan C yang sekadar memindahkan masalah, bukan D yang terlalu vague tanpa akuntabilitas individual, bukan E yang offloading tanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_004", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda ditarik menjadi narasumber dalam rapat koordinasi yang membahas kebijakan要将所有政府服务集中到一个移动应用程序中. Kebijakan ini promoted by sebuah startup teknologi yang bekerja sama dengan investor asing, dan akan menggantikan semua platform digital yang sudah berjalan di berbagai kementerian dan lembaga. Startup tersebut mengklaim bahwa konsolidasi akan meningkatkan efisiensi dan mengurangi duplikasi layanan. Namun data dari berbagai kementerian menunjukkan bahwa platform existing sudah berjalan dengan baik dan migrasi akan memakan waktu 2-3 tahun dengan biaya yang sangat besar. Di saat yang sama, Anda tahu bahwa pejabat yang mempromosikan kebijakan ini memiliki stakes financieres di startup tersebut. Anda diminta memberikan pandangan sebagai perwakilan pemerintah daerah. Position Anda adalah...",
        "options": [
            "Dukung kebijakan karena platform tunggal akan memudahkan warga mengakses semua layanan dari satu tempat dan modernisasi government services adalah langkah yang positif",
            "Tolak kebijakan karena migrasi akan mengganggu layanan yang sudah berjalan dengan baik dan biaya yang diperlukan lebih besar dari benefit yang ditawarkan",
            "Minta akses ke data analysis yang digunakan startup untuk mendukung klaim mereka, lakukan evaluasi independen terhadap cost-benefit, dan sampaikan findings secara objektif tanpa memihak kepentingan siapapun termasuk pejabat yang mempromosikan",
            "Netral saja karena ini adalah keputusan yang harus dibuat oleh level yang lebih tinggi dan Anda sebagai pejabat daerah tidak perlu campur tangan dalam kebijakan tingkat pusat",
            "Dukung kebijakan tapi minta audit independen terhadap hubungan financiero pejabat promosi dengan startup sebelum implementasi dimulai"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme dan integritas: tidak langsung mendukung atau menolak berdasarkan klaim yang belum terverifikasi, meminta data untuk dievaluasi secara independen, dan menyampaikan findings berdasarkan evidence. Pendekatan ini melindungi kepentingan publik sambil menjaga netralitas terhadap kebijakan yang memiliki konflik kepentingan. Bukan A yang naif, bukan B yang premature rejection, bukan D yang avoid responsibility, bukan E yang conflates support dengan investigation.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_005", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda sekretaris daerah yang mengetahui bahwa salah satu kepala Organisasi Perangkat Daerah (OPD) di lingkungan Anda telah menjalankan program pembangunan infrastruktur yang tidak sesuai dengan spesifikasi teknis yang ditetapkan dalam kontrak. Pekerjaan sudah mencapai 70% dan dana sudah dicairkan 60%. Kondisi ini baru terungkap melalui laporan warga yang kemudian dikuatkan oleh findings dari tim audit internal. Kepala OPD tersebut adalah sosok yang memiliki hubungan politik kuat dengan salah satu pasangan kandidat dalam Pemilida yang akan datang. Jika Anda eskalasi kasus ini, Anda khawatir akan dituduh menggunakan kasus ini untuk tujuan politik praktis. Jika Anda diam, pekerjaan akan continue dengan spesifikasi yang tidak sesuai dan korupsi infrastruktur akan berlanjut. Masyarakat juga sudah mulai mempertanyakan kualitas pekerjaan. Position Anda yang sangat kompleks adalah...",
        "options": [
            "Eskalasi kasus melalui channel resmi ke inspektorat dengan bukti-bukti yang sudah terkumpul, karena integritas pembangunan infrastruktur lebih penting dari kontroversi politik dan Anda tidak bisa diam melihat potensi korupsi，不管 timing politik apapun",
            "Tunda eskalasi sampai بعد Pemilida karena Anda khawatir eskalasi sekarang akan terlihat sebagai abuse of power untuk kepentingan politik salah satu kandidat",
            "Konfrontasi langsung kepala OPD dan minta dia memperbaiki spesifikasi pekerjaan dalam waktu tertentu, jika tidak baru eskalasi ke inspektorat",
            "Serahkan temuan kepada media agar publik tahu tentang masalah ini dan mendorong system untuk memperbaiki sendiri tanpa intervensi politik Anda",
            "Diam saja karena ini adalah urusan internal OPD dan inspektorat harusnya sudah menemukan masalah ini sendiri tanpa perlu laporan dari sekretaris daerah"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas yang tidak bisa diganggu oleh kalkulasi politik. Pembangunan infrastruktur yang tidak sesuai spesifikasi adalah korupsi yang merugikan masyarakat regardless dari timing politik. Channel resmi ke inspektorat adalah prosedur yang benar dan melindungi Anda dari tuduhan abuse of power. Bukan B yang menggunakan timing politik sebagai alasan untuk tidak bertindak, bukan C yang terlalu lenient dengan peluang cover-up, bukan D yang offloading ke media, bukan E yang pasif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_006", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola layanan pengaduan masyarakat di sebuah pemerintah kota. Sistem pengaduan digital yang Anda launch 8 bulan lalu telah successfully handled lebih dari 5000 pengaduan dan satisfaction rate warga mencapai 82%. Namun dalam 2 bulan terakhir, Anda mulai melihat pola yang mengkhawatirkan: ratusan pengaduan yang semuanya menggunakan frase yang sama, направленные ke topik yang sama, dari números de telepon yang berbeda. Investigation awal menunjukkan bahwa ini kemungkinan adalah coordinated complaint attack dari sebuah kelompok yang tidak puas dengan kebijakan zonasi terbaru. Beberapa pengaduan ini valid dan legitimate tapi majority adalah manufactured. Anda tahu bahwa jika Anda membedakan treatment antara pengaduan yang legitimate dan manufactured, Anda membuka diri untuk dituduh melakukan diskriminasi. Tapi jika semua diperlakukan sama, resources akan terbuang untuk memproses pengaduan yang tidak legitimate. Anda harus memutuskan...",
        "options": [
            "Proses semua pengaduan dengan standar yang sama karena setiap warga memiliki hak yang sama untuk menyampaikan pengaduan dan Anda tidak memiliki wewenang untuk menilai legitimacy pengaduan",
            "Buat sistem classification yang secara objective membedakan pengaduan berdasarkan content dan pattern tanpa memandang siapa pengadu, dan proses masing-masing sesuai klasifikasinya, dengan transparency kepada publik tentang criteria yang digunakan",
            "Abaikan semua pengaduan dari pola yang suspect karena tidak etis menggunakan sumber daya publik untuk mengolah manufactured complaints",
            "Laporkan coordinated attack ini kepada police karena pengaduan yang dimanufacture secara sistematis adalah penyalahgunaan sistem publik dan bisa dikategorikan sebagai cybercrime",
            "Buat kebijakan baru yang mengharuskan semua pengaduan disertai verifikasi identity sebelum diproses, untuk memastikan only legitimate complaints masuk"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan yang sophisticated: tidak discriminant berdasarkan siapa pengadu tapi berdasarkan objective criteria content dan pattern. Transparansi criteria menghindari tuduhan diskriminasi. Resources tetap digunakan secara efisien. Pendekatan ini menghormati hak pengaduan warga sambil tetap pragmatic tentang resource management. Bukan A yang inefficient, bukan C yang terlalu dismissive, bukan D yang terlalu legalistic untuk patterned complaints yang mungkin legitimate, bukan E yang membatasi akses pengaduan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_007", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda kepala desa yang mengelola anggaran desa yang sangat terbatas. Satu-satunya sumber pendapatan asli desa Anda berasal dari tanah kas desa yang disewakan kepada pengusaha untuk/perkebunan. Kontrak sewa akan berakhir dalam 6 bulan dan pengusaha meminta perpanjangan dengan kondisi yang sama. Namun warga desa mulai mempertanyakan apakah tanah kas desa tersebut sebenarnya milik desa atau milik pemerintah daerah, dan beberapa warga mengklaim bahwa tanah tersebut seharusnya digunakan untuk kepentingan村民而不是 menjadi sumber pendapatan desa yang kontroversial. Di waktu bersamaan, desa Anda membutuhkan非常大 pendanaan untuk membangun infrastruktur air bersih yang sudah lama dibutuhkan. Jika Anda perpanjang kontrak, warga yang mempertanyakan akan marah. Jika Anda tidak perpanjang, desa kehilangan pendapatan dan proyek air bersih tidak bisa funded. Jika tanah adalah milik pemerintah daerah, desa tidak punya wewenang untuk memutuskan apapun. Anda tidak memiliki kejelasan hukum tentang status tanah ini. Situation Anda sangat sulit.",
        "options": [
            "Perpanjang kontrak karena pendapatan desa sangat dibutuhkan untuk membiayai proyek air bersih dan desa tidak bisa memfasilitasi pembangunan tanpa pendapatan",
            "Jangan perpanjang kontrak dan gunakan tanah untuk proyek air bersih karena warga membutuhkan infrastruktur dasar lebih dari pendapatan desa",
            "Tunda keputusan sampai kejelasan hukum tentang status tanah diperoleh dari pengadilan atau instansi yang berwenang, namun sampaikan kepada pengusaha dan warga bahwa kontrak tidak akan diperpanjang tanpa kejelasan hukum, sementara itu eksplorasi alternative pendanaan untuk air bersih",
            "Serahkan keputusan kepada warga melalui mekanisme musyawarah desa karena ini adalah aset desa dan warga berhak menentukan penggunaannya",
            "Minta pengusaha memberikan bagian yang lebih besar dari keuntungan sewa untuk warga agar keluhan warga bisa addressed tanpa mengubah arrangements yang ada"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan prudent governance: tidak membuat keputusan berdasarkan informasi yang incomplete, menjaga posisi hukum desa dengan tidak terbebani komitmen sebelum kejelasan, tetap proactive dalam mencari solusi alternative untuk kebutuhan warga. Pendekatan ini melindungi desa dari risiko hukum sambil tidak diam saja menghadapi kebutuhan pembangunan. Bukan A atau B yangpremature sebelum kejelasan hukum, bukan D yang terlalu democratic tanpa kerangka hukum, bukan E yang compromise yang mungkin tidak efektif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_008", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda ditarik menjadi anggota tim оценка эффективности программы pemerintah yang telah berjalan selama 3 tahun dengan budget sangat besar. Program ini designed untuk meningkatkan kualitas pendidikan di daerah terpencil dengan menyediakan infrastruktur digital, pelatihan guru, dan scholarships untuk siswa. Evaluation menunjukkan hasil yang mixed: beberapa daerah menunjukkan improvement yang signifikan tapi majority justru tidak menunjukkan dampak yang berarti. Lebih mengkhawatirkan, beberapa daerah dengan improvement ternyata memiliki 数据 yang diragukan integritasnya karena guru dan kepala sekolah memiliki insentif untuk menunjukkan результат yang positif karena terkait dengan penilaian kinerja mereka. Anda tahu bahwa hasil evaluasi ini akan digunakan oleh pemerintah untuk menentukan apakah program akan dilanjutkan, diperluas, atau dihentikan. Beberapa tim eval yang lain memiliki agenda masing-masing: ada yang sangat mendukung kelanjutan program karena mereka involved di dalamnya, ada yang sangat ingin menghentikan program karena mereka crítico dari awal. Anda dalam posisi yang sangat penting.",
        "options": [
            "Buat laporan evaluasi yang诚实地 menyampaikan mixed results dan termasuk kesimpulan bahwa diperlukan penelitian lebih lanjut dengan metodologi yang lebih ketat sebelum memutuskan kelanjutan program",
            "Buat laporan yang menunjukkan program berhasil secara keseluruhan karena sebagian daerah berhasil dan ini sudah cukup sebagai bukti efektivitas program",
            "Fokuskan laporan pada daerah yang berhasil dan omit data dari daerah yang gagal karena hanya best practices yang bisa dipelajari dari program ini",
            "Sampaikan bahwa metodologi evaluasi Anda tidak cukup kuat untuk memberikan rekomendasi apapun dan minta dilakukan evaluasi tambahan dengan resources yang lebih besar",
            "Buat dua versi laporan: satu versi lengkap untuk intern dan satu versi yang lebih positif untuk publik dan pengambil keputusan"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas akademik dan tanggung jawab evaluasi: jujur tentang mixed results tanpa memanipulasi narrative untuk memihak siapapun. Rekomendasi untuk penelitian lebih lanjut dengan metodologi lebih ketat adalah langkah yang responsible ketika data tidak conclusive. Bukan B atau C yang cherry-pick data, bukan D yang avoid memberikan penilaian sama sekali, bukan E yang membuat dua versi laporan yang tidak etis.",
        "difficulty": "hard"
    },
]

with open('assets/questions/tkp_2.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Written {len(questions)} questions (pelayanan publik 1-8)")
import re
bad = sum(1 for q in questions for key in ['question','answer','explanation'] if key in q and re.search(r'[^\x00-\x7F]', str(q[key])))
bad += sum(1 for q in questions for opt in q.get('options',[]) if re.search(r'[^\x00-\x7F]', str(opt)))
print(f"Non-ASCII issues: {bad}")