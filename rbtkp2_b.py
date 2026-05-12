import json

with open('assets/questions/tkp_2.json', encoding='utf-8') as f:
    data = json.load(f)

jejaring = [
    {
        "id": "tkp2_009", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda seorang pejabat eselon III yang baru rotasi ke SKPD baru setelah 8 tahun di instansi sebelumnya. Di SKPD baru, Anda menemukan tim kerja terbelah menjadi dua kubu: satu mendukung mantan pejabat sebelumnya yang sudah pensiun, satu lagi mendukung pejabat saingan internal yang masih aktif. Kedua kubu sama-sama mencoba mendapatkan dukungan Anda. Kinerja SKPD menurun karena energi terbuang untuk politik internal. Anda baru datang dan tidak mengenal siapa di antara kedua kelompok yang benar atau salah. Kondisi ini diperumit oleh fakta bahwa mantan pejabat yang sudah pensiun masih memiliki influence besar terhadap banyak staf karena prestasinya di masa lalu. Position Anda adalah...",
        "options": [
            "Dukung kubu mantan pejabat pensiun karena dialah yang membawa Anda ke posisi ini dan loyalitas personal penting dalam birokrasi",
            "Dukung pejabat yang masih aktif karena dia masih memiliki kekuasaan untuk mempengaruhi karier Anda ke depan",
            "Netral secara politik, fokuskan seluruh energi pada penyelesaian backlog kerja dan bangun kepercayaan dari tim berdasarkan kinerja objektif, namun tetap terbuka berkomunikasi dengan semua pihak secara profesional",
            "Pilih pihak yang menurut analisis Anda memiliki program kerja paling sejalan dengan kepentingan masyarakat meskipun mereka saat ini kalah dalam pertarungan internal",
            "Lapor ke inspektorat bahwa SKPD ini memiliki politik internal yang mengganggu kinerja sehingga perlu intervensi atasan"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme tinggi di lingkungan yang kompleks. Netralitas bukan ketidakpedulian tapi posisi strategis yang memungkinkan bekerja efektif tanpa memihak. Membangun kepercayaan berbasis kinerja melindungi integritas Anda dan melayani masyarakat.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_010", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda diundang ke forum internasional tentang good governance di mana harus presentasi tentang inovasi pelayanan publik di daerah Anda. Saat menyusun materi, Anda sadar inovasi yang dipromosikan daerah Anda merupakan adaptasi dari program daerah lain yang dulu pernah Anda lihat saat benchmarking, dengan sedikit modifikasi. Daerah Anda tidak pernah menuliskan sumber inspirasi tersebut. Presentasi besok dan Anda harus memutuskan...",
        "options": [
            "Presentasikan sebagaimana adanya karena semua daerah saling belajar dan tidak ada yang bisa mengklaim inovasi 100% asli, selama program ini benar-benar memberikan manfaat bagi warga",
            "Sebutkan bahwa program merupakan pengembangan dari best practice daerah lain yang pernah menjadi referensi, namun sampaikan secara umum tanpa menyebut nama spesifik",
            "Telusuri terlebih dahulu apakah program daerah asal sudah dilindungi secara kekayaan intelektual, jika tidak, sebutkan sumber inspirasi secara terbuka",
            "Ubah presentasi untuk menghapus semua elemen yang terlihat mirip dengan program daerah lain dan klaim sebagai hasil riset mandiri",
            "Batalkan presentasi karena tidak ada cukup waktu untuk memverifikasi sumber inspirasi dan lebih baik tidak presentasi daripada mengklaim sesuatu yang belum pasti"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan integritas akademik dan profesional. Mengakui sumber inspirasi bukan kelemahan tapi demonstrasi kejujuran intelektual yang dihormati di forum internasional. Riset-based, tidak memalsakan klaim, dan tetap memungkinkan presentasi berjalan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_011", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda kepala bidang yang memiliki relasi baik dengan narasumber dari dunia usaha, akademisi, dan LSM. Dalam menyusun kebijakan publik yang evidence-based, Anda bermaksud mengundang narasumber dari ketiga kelompok. Namun Anda sadar narasumber dunia usaha cenderung memiliki kepentingan ekonomi yang mungkin bertentangan dengan kepentingan masyarakat kecil, akademisi mungkin terlalu teoritis tanpa realitas lapangan, dan LSM mungkin memiliki agenda partainya sendiri. Bagaimana menyeimbangkan...",
        "options": [
            "Ajak LSM dan akademisi saja karena dua kelompok ini memiliki integritas lebih tinggi daripada dunia usaha yang hanya mementingkan untung",
            "Ajak semua narasumber tanpa diskriminasi, namun buat kerangka diskusi terstruktur dengan pertanyaan yang mengarahkan setiap kelompok memberikan perspektif yang seimbang dan mewaspadai bias masing-masing",
            "Lakukan semua perencanaan sendiri tanpa narasumber eksternal karena semua kelompok memiliki bias dan lebih baik mengandalkan penilaian internal yang netral",
            "Ajak dunia usaha saja karena merekalah yang paling memahami ekonomi dan akan memberikan data paling aktual tentang kondisi riil",
            "Serahkan sepenuhnya kepada narasumber untuk menentukan topik diskusi karena merekalah yang paling kompeten di bidangnya masing-masing"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan pluralistis yang memperkaya kebijakan dengan beragam perspektif, sekaligus moderasi profesional untuk memitigasi bias. Fasilitator yang baik bukan menghilangkan perspektif tapi mengorganisir mereka menjadi dialog yang konstruktif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_012", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda ditugaskan menyusun MoU dengan universitas ternama untuk program magang dan riset bersama. Negosiasi berjalan baik dan MoU hampir ditandatangani. Tiba-tiba Anda mendapat informasi bahwa salah satu profesor counterpart memiliki reputasi bermasalah: beberapa publikasinya dianggap plagiarisme oleh komunitas akademik internasional, dan ada konflik kepentingan dengan perusahaan tempat professor menjadi konsultan. Informasi ini belum dipublikasikan secara resmi dan bersifat rahasia. Anda perlu memutuskan...",
        "options": [
            "Tetap proceed dengan MoU karena informasi tersebut belum terbukti secara resmi dan hubungan institusional lebih penting dari reputasi individual professor",
            "Tunda penandatanganan MoU dan sampaikan kepada pimpinan universitas bahwa ada informasi perlu diklarifikasi terkait konflik kepentingan professor counterpart, dengan tetap menjaga kerahasiaan sumber informasi",
            "Batalkan semua negosiasi karena professor bermasalah akan merusak integritas seluruh institusi Anda",
            "Lanjutkan MoU namun ganti counterpart professor dengan staff lain yang lebih bersih, namun jangan sampaikan alasan pergantian kepada universitas",
            "Publikasikan informasi tentang plagiarisme professor di media agar transparansi terjaga dan masyarakat tahu bahwa Anda tidak tertipu"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan keseimbangan antara kehati-hatian institusional dan profesionalisme dalam hubungan antar institusi. Menunda bukan membatalkan, dan mengkomunikasikan ke pimpinan universitas menjaga hubungan baik sambil melindungi institusi dari risiko reputasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_013", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda seorang kepala bagian yang memiliki bawahan sangat kompeten namun memiliki reputasi tidak sedap: sering mengkritik kebijakan atasan secara terbuka di media sosial, menulis artikel opini yang kadang mengkontroversikan posisi instansi, dan aktif di organisasi profesi yang kadang berseberangan dengan kebijakan pemerintah. Secara kinerja ia terbaik di tim Anda. Sebagai atasan, Anda perlu...",
        "options": [
            "Tetap biarkan karena performa bagus dan kebebasan berpendapat adalah hak karyawan selama tidak ada pelanggaran hukum yang terang",
            "Panggil dan tegur secara tertutup dan minta agar tidak menulis atau bicara yang kontroversial yang bisa merusak citra instansi, ingatkan bahwa sebagai ASN ada aturan tentang ekspresi publik",
            "Berhentikan karena meskipun performanya bagus, perilakunya yang publik dan kontroversial sudah melampaui batas kesetiaan terhadap institusi",
            "Pindahkan ke divisi lain yang lebih sesuai dengan karakter personalnya agar tidak mengganggu lingkungan kerja tim Anda",
            "Apresiasi melalui kompensasi finansial lebih tinggi sebagai kompensasi atas ketidaknyamanan yang ditimbulkan perilakunya terhadap tim lainnya"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan kepemimpinan yang matur: menghargai kompetensi dan kebebasan berpendapat, namun mengingatkan batasan aturan kepegawaian ASN. Pendekatan tertutup melindungi dignity bawahan sambil menegaskan batas profesional.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_014", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda diminta menjadi narasumber dalam seminar nasional. Namun sehari sebelum seminar, Anda mengetahui moderator memiliki afiliasi politis yang sangat keras dan seminar kemungkinan besar akan digunakan sebagai platform politik praktis. Anda sudah menyiapkan materi berisi ilmu pengetahuan dan pengalaman praktis yang valid. Hadir berarti memberikan legitimasi pada acara bermuatan politis. Tidak hadir berarti mengecewakan harapan penyelenggara yang sudah mengundang Anda dengan baik. Anda perlu memutuskan...",
        "options": [
            "Tetap hadir dan sampaikan materi sesuai persiapan karena kontribusi Anda pada publik lebih penting dari konteks politik seminar, dan selama materi Anda tidak politis maka tidak ada masalah",
            "Batalkan kehadiran dengan alasan apapun karena memberikan legitimasi pada acara bermuatan politik praktis adalah pelanggaran terhadap netralitas ASN",
            "Kontak moderator dan sampaikan bahwa Anda bersedia hadir asalkan moderator menjamin seminar berjalan ilmiah dan tidak digunakan untuk kampanye politik, dan jika tidak bisa menjamin, batalkan kehadiran",
            "Tetap hadir namun ubah materi untuk secara halus mengoffset bias politik moderator sehingga seminar tetap balanced",
            "Serahkan keputusan kepada pimpinan instansi karena sebagai ASN Anda tidak seharusnya membuat keputusan sendiri yang berpotensi menimbulkan masalah politik"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme aktif: tidak membatalkan secara prematur tapi memberikan kesempatan perbaikan, dan tidak hadir begitu saja tanpa filter. Melindungi netralitas ASN sambil tetap memungkinkan kontribusi ilmiah jika kondisi memungkinkan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_015", "category": "TKP", "subcategory": "Jejaring Kerja",
        "question": "Anda mengelola unit kerja dengan budaya hierarkis dan rigid yang sudah berlangsung puluhan tahun. Pegawai muda cenderung pasif dan menunggu instruksi dari atas. Anda diminta mengubah budaya ini dalam waktu satu tahun. Target ini bersifat mengikat. Anda tahu perubahan budaya tidak bisa instan. Namun tekanan untuk menghasilkan perubahan dalam waktu singkat sangat besar.",
        "options": [
            "Terima saja bahwa target satu tahun tidak realistis dan sampaikan kepada atasan bahwa perubahan budaya butuh waktu minimal 3-5 tahun",
            "Implementasi program perubahan radikal dengan memberi reward besar bagi yang inisiatif dan punishment bagi yang tetap pasif, pastikan semua tahu budaya lama tidak lagi diterima",
            "Mulai dengan memperkenalkan sistem mentoring berpasangan antara pegawai senior dan junior, buat proyek pilot kecil yang menuntut inisiatif tanpa risiko besar, dan bangun narrative bahwa perubahan dimulai dari hal kecil yang konsisten",
            "Buat kebijakan baru yang memaksa semua pegawai menyampaikan ide minimal satu per bulan dan yang tidak menyampaikan akan dikurangi tunjangan kinerja",
            "Import praktisi dari luar organisasi yang sudah berhasil mengubah budaya di tempat lain dan mereka akan membawa metodologi yang sudah teruji"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pemahaman mendalam bahwa perubahan budaya adalah proses organik, bukan dekret. Mentoring memanfaatkan pengalaman senior sekaligus memunculkan energi junior. Proyek pilot memberi ruang aman untuk eksperimen tanpa risiko besar. Pendekatan gradual tapi terstruktur membangun traction nyata.",
        "difficulty": "hard"
    },
]

sosial = [
    {
        "id": "tkp2_016", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda kepala desa di daerah pedalaman dengan tradisi adat yang sudah berlangsung ratusan tahun. Sebagian warga mempraktikkan tradisi tersebut dan menganggapnya bagian integral identitas budaya mereka. Namun tradisi mengandung unsur yang menurut pemerintah pusat termasuk kekerasan terhadap anak. Pemerintah pusat mengancam sanksi bagi kepala desa yang tidak menjalankan penghentian. Sebagian besar warga mendukung pelestarian tradisi ini dan menganggap pemerintah pusat tidak memahami budaya lokal. Anda dalam posisi sulit: menjalankan perintah berarti kehilangan dukungan warga, namun tidak menjalankan berarti melanggar aturan.",
        "options": [
            "Lakukan komunikasi intensif dengan warga, jelaskan regulasi dan risiko sanksi, namun sampaikan bahwa Anda akan mencari jalan tengah: modifikasi tradisi agar unsur kekerasan dihilangkan tapi core ritual tetap ada dengan melibatkan tokoh adat",
            "Tolakkan keinginan pemerintah pusat karena tradisi adat adalah kedaulatan desa dan Anda siap menanggung konsekuensi",
            "Laporkan tradisi kekerasan ini ke pemerintah pusat karena sebagai kepala desa Anda tidak mungkin menjalankan tradisi yang melanggar hak anak",
            "Ikuti perintah pemerintah pusat secara strict tanpa komunikasi dengan warga, tegakkan aturan karena hukum lebih tinggi dari tradisi",
            "Minta waktu satu tahun untuk transisi dengan bukti bahwa Anda sedang berusaha melestarikan tradisi tanpa kekerasan, namun sampaikan kepada warga bahwa perubahan tidak bisa dihindari"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan kepemimpinan transformasional yang rumit: memahami tradisi dan hukum bisa dikomposisikan melalui modifikasi yang melibatkan stakeholder kunci. Pendekatan ini bukan kepatuhan buta atau penolakan buta tapi diplomasi berbasis solusi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_017", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda pejabat yang ditempatkan di daerah dengan konflik historis antaretnis yang sudah berminggu-minggu. Situasi panas dan korban sipil mulai muncul. Anda mendapat informasi bahwa dua kelompok mempersiapkan balasan yang keduanya berpotensi memicu eskalasi kekerasan berskala besar. Kelompok A berbasis di wilayah Anda dan kelompok B di kabupaten tetangga. Anda tidak memiliki cukup aparat untuk menengahi secara fisik, namun memiliki hubungan personal yang baik dengan tokoh kunci di kedua kelompok. Eskalasi diperkirakan dalam 48 jam.",
        "options": [
            "Segera minta reinforcements dari pusat karena situasinya di luar kapasitas Anda dan risiko eskalasi terlalu besar untuk ditangani sendiri",
            "Gunakan hubungan personal dengan tokoh kunci di kedua kelompok secara simultan, sampaikan bahwa Anda memiliki informasi tentang rencana balasan dan minta mereka bergabung dalam pertemuan tertutup darurat, serta sampaikan konsekuensi hukum jika eskalasi terjadi",
            "Hubungi hanya kelompok A karena mereka berbasis di wilayah Anda, kelompok B adalah tanggung jawab kabupaten tetangga",
            "Publikasikan peringatan bahwa eskalasi akan mengakibatkan intervensi militer sehingga kedua kelompok takut dan membatalkan rencana",
            "Lapor kepada pimpinan di pusat namun tidak mengambil tindakan lain karena tidak memiliki wewenang untuk keputusan lintas kabupaten"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan kepemimpinan krisis yang efektif: memanfaatkan modal sosial yang sudah dibangun untuk de-eskalasi, pendekatan simultan untuk menghindari persepsi bias, menetapkan pertemuan tertutup sebagai ruang dialog, dan menyampaikan konsekuensi hukum sebagai deterrent.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_018", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda ditugaskan menjadi fasilitator dalam rembug desa yang membahas rencana pembangunan jalan melewati area sakral. Kelompok warga sangat menolak karena area tersebut makam leluhur yang dikeramatkan. Kelompok lain sangat mendukung karena akses jalan akan membuka isolasi ekonomi desa. Kedua kelompok memiliki argumentasi kuat. Anda sebagai fasilitator perlu memastikan dialog berjalan adil dan menghasilkan solusi.",
        "options": [
            "Ajak warga yang menolak untuk memahami kebutuhan ekonomi desa dan minta mereka berkorban demi kemajuan bersama karena pembangunan lebih penting dari kepercayaan",
            "Ajak warga yang mendukung untuk memahami sensitivitas budaya dan minta mereka mencari alternatif rute jalan yang tidak melewati area sakral meskipun biayanya lebih mahal",
            "Facilitasi dialog terstruktur di mana kedua kelompok saling mempresentasikan argumentasi, lalu minta mereka bersama-sama mencari solusi kreatif: apakah akses jalan yang sama bisa dicapai melalui sedikit penyesuaian rute, atau apakah ada pengakuan simbolik terhadap area sakral sebagai bagian dari pembangunan",
            "Paksanakan saja keputusan Musrenbangdes karena pembangunan jalan perlu dilakukan dan warga harus bisa menerima karena musrenbangdes adalah mekanisme demokratis",
            "Sampaikan bahwa masalah ini harus dirujuk ke tingkat lebih tinggi karena sebagai fasilitator Anda tidak memiliki wewenang untuk keputusan sensitif secara budaya"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan fasilitasi yang matur: tidak memihak atau memaksakan solusi tapi menciptakan ruang dialog di mana stakeholder menemukan solusi mereka sendiri. Fasilitator yang baik menghasilkan solusi yang ownership-nya ada pada masyarakat.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_019", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda pejabat di kota besar yang menerima banyak buruh migrant dari daerah lain. Data menunjukkan budaya lokal mulai berubah karena enclave-enclave budaya dari daerah asal buruh migrant yang terbentuk di lingkungan kota. Beberapa warga lokal merasa terancam dan mulai menyalahkan buruh migrant atas perubahan budaya. Kondisi ini berpotensi menjadi konflik sosial jika tidak ditangani dengan baik.",
        "options": [
            "Ajak semua pihak untuk bersama-sama merumuskan aturan tentang kehidupan bermasyarakat yang mengakomodasi keragaman tanpa satu kelompok mendominasi yang lain, fasilitasi dialog lintas budaya secara berkala",
            "Tegaskan bahwa tidak ada yang bisa mengubah budaya lokal karena kota adalah milik warga asli dan buruh migrant adalah tamu yang harus mengikuti aturan lokal",
            "Ajak buruh migrant untuk berasimilasi sepenuhnya ke budaya lokal dan meninggalkan identitas budaya daerah asal mereka",
            "Biarkan saja karena perubahan budaya adalah proses alami yang tidak bisa diintervensi oleh pemerintah dan konflik akan selesai sendiri seiring waktu",
            "Ekspulsikan semua buruh migrant yang tinggal di enclave karena mereka berkontribusi pada fragmentasi sosial"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan pemahaman mendalam tentang multikulturalisme dan kohesi sosial: tidak ada kelompok yang harus dihapuskan atau dipaksakan tapi semua menemukan ruang koeksistensi. Pendekatan inklusif mencegah xenophobia dari warga lokal dan isolation dari migrant.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_020", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda ditugaskan melakukan assessment efektivitas program pemberdayaan perempuan di pedesaan. Program memberikan peningkatan signifikan pada metrik perempuan: pendapatan, partisipasi sosial, akses kesehatan. Namun program memperkuat dinamika gender yang tidak diinginkan: peningkatan pendapatan istri menyebabkan peningkatan kekerasan domestik karena suami tidak nyaman dengan perubahan hierarki. Data menunjukkan 40% penerima manfaat mengalami kekerasan domestik yang meningkat setelah program berjalan.",
        "options": [
            "Buat laporan yang hanya memfokuskan pada metrik positif karena program pada dasarnya berhasil dan kekerasan domestik adalah masalah terpisah dari program",
            "Buat laporan lengkap yang menyebutkan keberhasilan metrik dan konsekuensi negatif tidak diinginkan berupa peningkatan kekerasan domestik, beserta rekomendasi untuk penambahan komponen program yang mengatasi kekerasan dalam rumah tangga",
            "Sembunyikan data tentang kekerasan domestik karena dapat digunakan oleh pihak yang memprotes program pemberdayaan perempuan secara keseluruhan",
            "Berhentikan semua program segera karena bukti menunjukkan program menyebabkan kekerasan domestik yang meningkat",
            "Serahkan temuan kepada organisasi perempuan nasional karena ini di luar wewenang Anda"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan integritas riset dan tanggung jawab policy-making: tidak menyembunyikan temuan tidak nyaman, tidak langsung membatalkan program yang umumnya berhasil, tapi memberikan analisis lengkap yang memungkinkan perbaikan. Pendekatan ini jujur, konstruktif, dan bertanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_021", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda mengelola program konservasi lingkungan di daerah dengan populasi adat yang hidupnya bergantung pada hutan. Data menunjukkan hutan tersebut habitat kritis bagi spesies terancam punah. Konservasi akan mengusir populasi adat dari hutan yang sudah mereka huni ratusan tahun. Tidak melakukan konservasi berarti spesies punah dan ekosistem rusak permanen. Kondisi diperumit oleh fakta bahwa populasi adat secara historis tidak memiliki kejelasan status hukum atas tanah yang mereka huni.",
        "options": [
            "Prioritaskan konservasi spesies terancam punah karena kepunahan irreversibel dan lebih tinggi nilainya daripada hak tinggal populasi adat yang bisa direlokasi dengan kompensasi memadai",
            "Prioritaskan hak populasi adat karena mereka sudah menghuni hutan ratusan tahun dan memiliki hak tradisional yang tidak bisa diganggu gugat",
            "Cari solusi yang mungkin: zona non-core conservation untuk populasi adat, zona core conservation untuk spesies dengan akses terbatas, berikan kejelasan hukum tanah, dan libatkan mereka sebagai mitra stewardship dalam konservasi dengan insentif ekonomi sustainable",
            "Serahkan keputusan kepada pengadilan karena ini masalah hukum kompleks dan bukan wewenang Anda",
            "Lakukan kajian lingkungan lengkap terlebih dahulu sebelum mengambil keputusan apapun"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pemikiran sistemik dan kreatif yang mencari solusi win-win: tidak ada pihak kehilangan segalanya. Pendekatan participatory conservation yang melibatkan populasi adat sebagai mitra stewardship telah terbukti efektif secara global karena mereka memiliki insentif untuk melestarikan hutan tempat mereka tinggal.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_022", "category": "TKP", "subcategory": "Sosial Budaya",
        "question": "Anda pejabat yang menangani urusan agama di daerah dengan tradisi pembacaan kitab suci secara bersama-sama setiap tahun. Ratusan warga terlibat dan tradisi sudah puluhan tahun. Sebuah kelompok kecil namun vokal menganggap tradisi tidak sesuai dengan ajaran agama yang mereka anut karena dianggap mencampuradukkan dengan kepercayaan lokal. Kelompok tersebut menekan Anda untuk melarang tradisi dengan alasan pemerintah harus menjamin kebebasan beragama termasuk dari praktik yang dianggap tidak murni. Sebagian besar warga sangat terikat tradisi ini dan melarang akan menimbulkan konflik besar.",
        "options": [
            "Larang tradisi karena kebebasan beragama termasuk kebebasan untuk tidak berpartisipasi dalam praktik yang dianggap tidak murni, dan pemerintah harus melindungi hak minoritas",
            "Biarkan tradisi berjalan karena pemerintah tidak harus campur tangan dalam praktik agama selama tidak ada kekerasan atau eksploitasi",
            "Facilitasi dialog antara kelompok yang mendukung dan menentang tradisi, cari pemahaman bersama apakah tradisi bisa dimodifikasi untuk mengakomodasi keberatan tanpa menghilangkan esensi, dan jika tidak menemukan jalan tengah, sampaikan bahwa keputusan final ada pada warga yang berpartisipasi",
            "Larang tradisi karena pemerintah harus netral terhadap praktik agama yang tidak mainstream",
            "Serahkan keputusan ke pengadilan agama karena ini masalah teologis di luar wewenang pemerintah sipil"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pendekatan yang sangat nuanced: menjaga kebebasan beragama tanpa memilih salah satu interpretasi teologis sebagai benar, melibatkan semua pihak dalam dialog, dan mengembalikan keputusan kepada masyarakat yang terdampak langsung. Pemerintah sebagai fasilitator bukan arbiter teologis.",
        "difficulty": "hard"
    },
]

data.extend(jejaring)
data.extend(sosial)
with open('assets/questions/tkp_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Total now: {len(data)}")

import re
bad = sum(1 for q in data for key in ['question','answer','explanation'] if key in q and re.search(r'[^\x00-\x7F]', q[key]))
bad += sum(1 for q in data for opt in q.get('options',[]) if re.search(r'[^\x00-\x7F]', opt))
print(f"Non-ASCII issues: {bad}")