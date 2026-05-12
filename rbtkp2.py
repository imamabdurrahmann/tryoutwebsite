import json

# PELAYANAN PUBLIK (8)
pelayanan = [
    {
        "id": "tkp2_001", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda seorang kepala dinas di sebuah Pemerintah Daerah yang menghadapi situasi kritis: seorang pengusaha besar yang merupakan investor utama di daerah Anda menuntut percepatan perizinan untuk proyek infrastruktur yang akan menyerap ribuan tenaga kerja. Namun proses AMDAL baru mencapai 60% dan temuan awal menunjukkan potensi dampak lingkungan yang signifikan di daerah resapan air. Pengusaha tersebut memiliki hubungan dekat dengan pejabat tinggi di pemerintah pusat yang sudah memberikan dukungan terhadap proyek ini secara implisit. Masyarakat sekitar mulai mempertanyakan komitmen pemerintah terhadap lingkungan. Investigation internal menunjukkan beberapa irregularities dalam prosedur perizinan yang berpotensi melanggar aturan. Tekanan dari berbagai arah sangat kuat dan waktu terbatas. Langkah Anda adalah...",
        "options": [
            "Proses perizinan dipercepat dan izin segera dikeluarkan karena proyek akan menciptakan ribuan lapangan kerja dan dukungan pejabat tinggi pusat merupakan legitimasi yang cukup",
            "Izin ditunda sampai AMDAL selesai 100%, sampaikan kepada pengusaha bahwa regulasi lingkungan tidak bisa dikompromikan dan proses harus sesuai prosedur, namun jaga komunikasi tetap diplomatis",
            "Buat izin bersyarat yang mewajibkan pengusaha melakukan pemulihan lingkungan sebagai bagian dari persyaratan izin, dengan timeline yang tegas dan mekanisme monitoring independent",
            "Serahkan keputusan final kepada pengusaha: apakah mereka mau menunggu AMDAL selesai atau memilih membatalkan proyek, karena Anda tidak ingin menanggung risiko dari kedua pilihan",
            "Buat keputusan berdasarkan voting internal tim karena keputusan kolektif lebih aman jika kemudian terjadi masalah"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan keseimbangan antara tanggung jawab lingkungan dan kebutuhan ekonomi. Izin bersyarat bukan penundaan yang merugikan investasi, bukan penolakan tanpa dasar hukum, bukan pelepasan tanggung jawab. Instrumen ini adalah praktik terbaik dalam perizinan berkelanjutan yang menyeimbangkan semua kepentingan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_002", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola unit pelayanan publik yang sedang melakukan digitalisasi layanan. Setelah 6 bulan implementasi, data menunjukkan bahwa layanan digital meningkat efisiensi untuk kelompok usia produktif, namun terjadi peningkatan signifikan pengaduan dari lansia dan warga di daerah terpencil yang tidak memiliki akses internet memadai. Beberapa warga lansia tidak bisa mengakses layanan dasar karena tidak mampu menggunakan aplikasi digital. Anggaran untuk layanan non-digital sudah dipangkas untuk mendanai digitalisasi. Pejabat yang membidangi transformasi digital meminta semua layanan dimigrasikan ke digital dalam 3 bulan ke depan. Kondisi Anda rumit: efisiensi digital versus aksesibilitas universal, tekanan politik versus kebutuhan riil warga.",
        "options": [
            "Dukung migrasi penuh ke digital sesuai permintaan pejabat karena transformasi digital adalah arah kebijakan pemerintah dan aksesibilitas adalah urusan masing-masing warga untuk beradaptasi",
            "Minta perpanjangan deadline migrasi digital selama 6 bulan sambil secara agresif meningkatkan program pelatihan literasi digital untuk warga yang kesulitan, dengan resources yang dialokasikan secara proporsional",
            "Kembalikan semua layanan ke format non-digital karena digitalisasi jelas merugikan kelompok rentan dan efisiensi tidak boleh mengorbankan keadilan akses",
            "Biarkan warga memilih sendiri channel layanan yang mereka mau, digital atau non-digital, dan lihat angka saja tanpa intervensi apapun",
            "Serahkan keputusan kepada pejabat transformasi digital karena Anda tidak memiliki expertise untuk menilai apakah digitalisasi sudah waktunya atau belum"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan pragmatis dan inklusif: mendukung transformasi digital tapi dengan timeline yang realistis dan investasi konkret pada literasi digital warga. Pendekatan ini tidak menolak perubahan tapi memastikan tidak ada yang tertinggal. Bukan A yang tidak peka aksesibilitas, bukan C yang regressive, bukan D yang pasif, bukan E yang menghindari tanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_003", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda kepala bagian pelayanan masyarakat di sebuah pemerintah kota yang menghadapi krisis kepercayaan publik. Media memberitakan serangkaian kasus di mana warga mengalami kesulitan mengakses layanan dasar: perbaikan KTP memakan waktu berbulan-bulan, layanan kesehatan menolak pasien karena masalah administrasi, dan pengurusan izin usaha yang korup. Setiap kasus terdokumentasi dengan baik. Beberapa kasus melibatkan staf Anda secara personal dan Anda tahu setidaknya satu kasus melibatkan staf yang memiliki hubungan keluarga dengan pejabat daerah yang powerful. Investigation formal akan memakan waktu lama. Namun ketidakpuasan publik terus meningkat dan media watching closely.",
        "options": [
            "Lakukan investigation internal menyeluruh, jika ditemukan staf terbukti maladministration, proses sesuai hukum tanpa pandang bulu termasuk staf yang memiliki koneksi politik, dan sampaikan hasilnya kepada publik secara transparan",
            "Diam saja sampai investigation selesai dan hindari komentar apapun ke media karena berbicara terlalu cepat bisa merugikan pihak yang tidak bersalah",
            "Pindahkan staf yang terlibat ke posisi lain yang tidak berhadapan langsung dengan publik, namun jangan proses hukum karena akan menimbulkan lebih banyak masalah dengan pejabat yang connected",
            "Buat pernyataan publik bahwa Anda personally bertanggung jawab atas semua failures dan akan memastikan perbaikan sistem secara menyeluruh, tanpa memberikan detail tentang kasus individual karena itu privacy matters",
            "Serahkan semua kasus kepada police karena maladministration yang melibatkan pejabat daerah dan KKN adalah tindak pidana yang harus ditangani oleh APH bukan oleh internal government"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas tertinggi: tidak menutupi masalah, tidak melindungi siapa pun karena koneksi politik, merespons dengan transparansi terhadap publik. Investigation menyeluruh memastikan fakta sebelum action. Bukan B yang pasif, bukan C yang sekadar memindahkan masalah, bukan D yang terlalu vague, bukan E yang offloading tanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_004", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda ditarik menjadi narasumber dalam rapat koordinasi yang membahas kebijakan konsolidasi semua layanan pemerintah ke dalam satu aplikasi mobile. Kebijakan ini dipromosikan oleh sebuah startup teknologi yang bekerja sama dengan investor asing. Startup mengklaim konsolidasi akan meningkatkan efisiensi dan mengurangi duplikasi layanan. Data dari berbagai kementerian menunjukkan bahwa platform existing sudah berjalan dengan baik dan migrasi akan memakan waktu 2-3 tahun dengan biaya besar. Anda tahu bahwa pejabat yang mempromosikan kebijakan ini memiliki stakes financieres di startup tersebut. Anda diminta memberikan pandangan sebagai perwakilan pemerintah daerah.",
        "options": [
            "Dukung kebijakan karena platform tunggal akan memudahkan warga mengakses semua layanan dari satu tempat dan modernisasi government services adalah langkah yang positif",
            "Tolak kebijakan karena migrasi akan mengganggu layanan yang sudah berjalan dengan baik dan biaya lebih besar dari benefit yang ditawarkan",
            "Minta akses ke data analysis yang digunakan startup untuk mendukung klaim mereka, lakukan evaluasi independen terhadap cost-benefit, dan sampaikan findings secara objektif tanpa memihak siapapun termasuk pejabat yang mempromosikan",
            "Netral saja karena ini adalah keputusan yang harus dibuat oleh level yang lebih tinggi dan Anda sebagai pejabat daerah tidak perlu campur tangan dalam kebijakan tingkat pusat",
            "Dukung kebijakan tapi minta audit independen terhadap hubungan financeiro pejabat promosi dengan startup sebelum implementasi dimulai"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme dan integritas: tidak langsung mendukung atau menolak berdasarkan klaim yang belum terverifikasi, meminta data untuk dievaluasi secara independen. Pendekatan ini melindungi kepentingan publik sambil menjaga netralitas terhadap kebijakan yang memiliki konflik kepentingan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_005", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda sekretaris daerah yang mengetahui bahwa seorang kepala OPD telah menjalankan program pembangunan infrastruktur yang tidak sesuai spesifikasi teknis dalam kontrak. Pekerjaan sudah mencapai 70% dan dana dicairkan 60%. Kondisi ini terungkap melalui laporan warga dan dikuatkan oleh tim audit internal. Kepala OPD tersebut memiliki hubungan politik kuat dengan salah satu pasangan kandidat dalam Pemilda yang akan datang. Jika Anda eskalasi kasus ini, Anda khawatir dituduh menggunakan kasus ini untuk tujuan politik praktis. Jika Anda diam, korupsi infrastruktur berlanjut dan masyarakat mempertanyakan kualitas pekerjaan.",
        "options": [
            "Eskalasi kasus melalui channel resmi ke inspektorat dengan bukti-bukti yang sudah terkumpul, karena integritas pembangunan lebih penting dari kontroversi politik dan Anda tidak bisa diam melihat potensi korupsi",
            "Tunda eskalasi sampai setelah Pemilda karena khawatir eskalasi sekarang akan terlihat sebagai abuse of power untuk kepentingan politik salah satu kandidat",
            "Konfrontasi langsung kepala OPD dan minta dia memperbaiki spesifikasi pekerjaan dalam waktu tertentu, jika tidak baru eskalasi ke inspektorat",
            "Serahkan temuan kepada media agar publik tahu tentang masalah ini dan mendorong system untuk memperbaiki sendiri tanpa intervensi politik Anda",
            "Diam saja karena ini adalah urusan internal OPD dan inspektorat harusnya sudah menemukan masalah ini sendiri"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas yang tidak bisa diganggu oleh kalkulasi politik. Pembangunan infrastruktur yang tidak sesuai spesifikasi adalah korupsi yang merugikan masyarakat regardless dari timing politik. Channel resmi ke inspektorat adalah prosedur yang benar dan melindungi dari tuduhan abuse of power.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_006", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola layanan pengaduan masyarakat di sebuah pemerintah kota. Sistem pengaduan digital yang launch 8 bulan lalu telah successfully handled lebih dari 5000 pengaduan. Namun dalam 2 bulan terakhir, ratusan pengaduan menggunakan frase yang sama dan направленные ke topik yang sama dari nomor telepon berbeda. Investigation awal menunjukkan coordinated complaint attack dari kelompok yang tidak puas dengan kebijakan zonasi terbaru. Beberapa pengaduan valid tapi majority manufactured. Anda tahu bahwa jika memperlakukan berbeda antara pengaduan legitimate dan manufactured, Anda terbuka dituduh diskriminasi. Tapi jika semua diperlakukan sama, resources terbuang untuk pengaduan tidak legitimate.",
        "options": [
            "Proses semua pengaduan dengan standar yang sama karena setiap warga memiliki hak yang sama dan Anda tidak memiliki wewenang untuk menilai legitimacy pengaduan",
            "Buat sistem classification yang secara objective membedakan pengaduan berdasarkan content dan pattern tanpa memandang siapa pengadu, dan proses masing-masing sesuai klasifikasinya dengan transparansi criteria kepada publik",
            "Abaikan semua pengaduan dari pola yang suspect karena tidak etis menggunakan sumber daya publik untuk mengolah manufactured complaints",
            "Laporkan coordinated attack ini kepada police karena pengaduan yang dimanufacture secara sistematis adalah penyalahgunaan sistem publik",
            "Buat kebijakan baru yang mengharuskan semua pengaduan disertai verifikasi identity sebelum diproses"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan sophisticated: tidak diskriminatif berdasarkan siapa tapi berdasarkan objective criteria content dan pattern. Transparansi criteria menghindari tuduhan diskriminasi. Resources tetap efisien. Bukan A yang inefficient, bukan C yang terlalu dismissive, bukan D yang terlalu legalistic, bukan E yang membatasi akses pengaduan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_007", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda kepala desa yang mengelola anggaran desa sangat terbatas. Satu-satunya pendapatan asli desa berasal dari tanah kas desa yang disewakan untuk perkebunan. Kontrak sewa akan berakhir dalam 6 bulan dan pengusaha meminta perpanjangan dengan kondisi yang sama. Warga desa mempertanyakan apakah tanah kas desa tersebut milik desa atau milik pemerintah daerah, dan beberapa warga mengklaim tanah seharusnya untuk kepentingan warga. Di saat bersamaan, desa membutuhkan pendanaan besar untuk infrastruktur air bersih. Jika perpanjang kontrak, warga yang mempertanyakan akan marah. Jika tidak perpanjang, desa kehilangan pendapatan. Anda tidak memiliki kejelasan hukum tentang status tanah ini.",
        "options": [
            "Perpanjang kontrak karena pendapatan desa sangat dibutuhkan untuk membiayai proyek air bersih dan desa tidak bisa memfasilitasi pembangunan tanpa pendapatan",
            "Jangan perpanjang kontrak dan gunakan tanah untuk proyek air bersih karena warga membutuhkan infrastruktur dasar lebih dari pendapatan desa",
            "Tunda keputusan sampai kejelasan hukum tentang status tanah diperoleh dari pengadilan, namun sampaikan kepada pengusaha dan warga bahwa kontrak tidak akan diperpanjang tanpa kejelasan hukum, sementara eksplorasi alternative pendanaan untuk air bersih",
            "Serahkan keputusan kepada warga melalui musyawarah desa karena ini aset desa dan warga berhak menentukan penggunaannya",
            "Minta pengusaha memberikan bagian lebih besar dari keuntungan sewa untuk warga agar keluhan warga bisa addressed tanpa mengubah arrangements yang ada"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan prudent governance: tidak membuat keputusan berdasarkan informasi tidak lengkap, menjaga posisi hukum desa, tetap proactive mencari solusi alternative untuk kebutuhan warga. Pendekatan ini melindungi desa dari risiko hukum sambil tidak diam menghadapi pembangunan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_008", "category": "TKP", "subcategory": "Pelayanan Publik",
        "question": "Anda ditarik menjadi anggota tim evaluasi program pemerintah yang telah berjalan 3 tahun dengan budget sangat besar. Program ini dirancang untuk meningkatkan kualitas pendidikan di daerah terpencil. Evaluation menunjukkan hasil mixed: beberapa daerah improvement signifikan tapi majority tidak menunjukkan dampak berarti. Lebih mengkhawatirkan, beberapa daerah dengan improvement memiliki data yang diragukan integritasnya karena guru dan kepala sekolah memiliki insentif untuk menunjukkan hasil positif karena terkait dengan penilaian kinerja mereka. Hasil evaluasi akan digunakan untuk menentukan apakah program dilanjutkan atau dihentikan. Beberapa tim eval memiliki agenda masing-masing: ada yang sangat mendukung kelanjutan karena involved di dalamnya, ada yang ingin menghentikan karena kritikus dari awal.",
        "options": [
            "Buat laporan evaluasi yang jujur menyampaikan mixed results dan menyimpulkan bahwa diperlukan penelitian lebih lanjut dengan metodologi lebih ketat sebelum memutuskan kelanjutan program",
            "Buat laporan yang menunjukkan program berhasil secara keseluruhan karena sebagian daerah berhasil dan ini sudah cukup sebagai bukti efektivitas program",
            "Fokuskan laporan pada daerah yang berhasil dan omit data dari daerah yang gagal karena hanya best practices yang bisa dipelajari",
            "Sampaikan bahwa metodologi evaluasi tidak cukup kuat untuk memberikan rekomendasi dan minta dilakukan evaluasi tambahan dengan resources lebih besar",
            "Buat dua versi laporan: satu versi lengkap untuk intern dan satu versi lebih positif untuk publik dan pengambil keputusan"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas akademik dan tanggung jawab evaluasi: jujur tentang mixed results tanpa memanipulasi narrative untuk memihak siapapun. Rekomendasi untuk penelitian lebih lanjut adalah langkah responsible ketika data tidak conclusive.",
        "difficulty": "hard"
    },
]

with open('assets/questions/tkp_2.json', 'w', encoding='utf-8') as f:
    json.dump(pelayanan, f, ensure_ascii=False, indent=2)
print(f"Written {len(pelayanan)} pelayanan publik questions")

import re
bad = 0
for i, q in enumerate(pelayanan):
    for key in ['question', 'answer', 'explanation']:
        if re.search(r'[^\x00-\x7F]', q[key]):
            print(f"  Q{i+1} {key}: NON-ASCII FOUND")
            bad += 1
    for opt in q['options']:
        if re.search(r'[^\x00-\x7F]', opt):
            print(f"  Q{i+1} option: NON-ASCII FOUND")
            bad += 1
print(f"Non-ASCII issues: {bad}")