import json

questions = [
    # === PELAYANAN PUBLIK (8) ===
    {
        "id": "tkp3_001",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda seorang pejabat pemerintah daerah yang menangani perizinan berusaha. Seorang investor asing mengajukan izin operasional di zona industri yang belum memiliki infrastruktur akses jalan yang memadai. Di satu sisi, izin berpotensi meningkatkan investasi daerah secara signifikan. Di sisi lain, jalanan rusak akan memperburuk keluhan warga sekitar dan berpotensi menimbulkan konflik sosial. Atasan meminta agar izin segera diproses demi target investasi triwulanan. Studi AMDAL belum sepenuhnya final. Posisi Anda adalah...",
        "options": [
            "Segera proses izin karena permintaan atasan bersifat instruksi hierarkis dan investor sudah memenuhi persyaratan administrasi dasar",
            "Tunda izin sampai infrastruktur akses mendapat perbaikan minimum, namun sampaikan secara diplomatis kepada investor bahwa proses memerlukan waktu tambahan dengan alasan teknis kepastian berusaha",
            "Berikan izin bersyarat yang mewajibkan perusahaan menyediakan dana CSR untuk perbaikan infrastruktur jalan sebagai bagian dari izin operasional mereka",
            "Tolak izin dengan alasan infrastruktur belum memadai dan sampaikan bahwa penolakan demi kepentingan warga adalah keputusan yang tepat",
            "Serahkan keputusan sepenuhnya kepada atasan karena Anda tidak memiliki wewenang untuk menunda proses yang sudah diperintahkan"
        ],
        "answer": "Berikan izin bersyarat yang mewajibkan perusahaan menyediakan dana CSR untuk perbaikan infrastruktur jalan sebagai bagian dari izin operasional mereka",
        "explanation": "Opsi C merupakan pendekatan terintegrasi yang menyeimbangkan kepentingan investor, warga, dan pemerintah. Izin bersyarat merupakan instrumen hukum yang lazim digunakan dalam perizinan investasi. Pendekatan ini bukan penundaan yang merugikan investasi, bukan penolakan tanpa dasar hukum, bukan kepatuhan buta, dan bukan pelepasan tanggung jawab.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_002",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda menjadi mediator dalam sengketa batas tanah antara dua desa yang sudah berlangsung selama 15 tahun. Kedua belah pihak memiliki dokumen kepemilikan yang saling bertentangan dari era berbeda. Baru terungkap bahwa dokumen salah satu pihak kemungkinan besar dipalsukan oleh calo tanah yang sudah bertahun-tahun beroperasi. Namun bukti pemalsuan belum melalui proses forensik yang sah. Warga kedua desa sudah mulai kerumun dan situasi berpotensi ricuh. Anda harus...",
        "options": [
            "Segera umumkan bahwa dokumen yang dimungkinkan dipalsukan tersebut tidak sah dan putuskan berdasarkan dokumen pihak lain saja demi keamanan",
            "Hentikan mediasi dan sampaikan kepada kedua belah pihak bahwa masalah ini harus diselesaikan melalui jalur pengadilan saja karena mediator tidak berwenang menangani sengketa dengan indikasi pemalsuan",
            "Tunda mediasi dengan alasan memerlukan verifikasi forensik, tetapkan batas waktu maksimal 14 hari kerja dan libatkan pihak forensik yang besok bisa dimulai, sambil memastikan kedua pihak tidak melakukan provokasi selama masa tunda",
            "Ambil keputusan berdasarkan dokumen tertua karena dokumen yang lebih baru cenderung dimanipulasi oleh calo tanah yang sudah beroperasi lama",
            "Sarankan kedua desa untuk membagi tanah secara merata sebagai jalan tengah agar situasi segera reda"
        ],
        "answer": "Tunda mediasi dengan alasan memerlukan verifikasi forensik, tetapkan batas waktu maksimal 14 hari kerja dan libatkan pihak forensik yang besok bisa dimulai, sambil memastikan kedua pihak tidak melakukan provokasi selama masa tunda",
        "explanation": "Opsi C menjaga integritas proses mediasi dengan tidak memihak sebelum bukti valid, menetapkan tenggat waktu agar tidak menjadi penundaan tanpa akhir, melibatkan ahli forensik secara konkret, dan secara proaktif mencegah eskalasi konflik.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_003",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola unit pelayanan publik di sebuah kelurahan. Seorang lansia datang setiap minggu selama tiga bulan untuk menanyakan status permohonan KTP yang diajukan atas nama cucunya yang baru lahir. Staf loket sudah berulang kali menjelaskan bahwa proses memerlukan 14 hari kerja. Lansia terus datang dan menuduh bahwa staf sengaja memperlambat. Tuduhan ini viral di grup WhatsApp warga. الموقف Anda adalah...",
        "options": [
            "Minta lansia tersebut membuat laporan resmi jika merasa ada ketidakadilan agar bisa diproses sesuai SOP, dan abaikan pesan WhatsApp karena tidak bersifat formal",
            "Terima lansia dengan tenang, tunjukkan langsung progres permohonan di sistem, jelaskan tahap demi tahap dengan sabar, dan jika bersedia, dampingi lansia meluruskan informasi di grup WhatsApp warga secara langsung",
            "Hubungi keluarga lansia dan minta mereka menjauhkan lansia dari layanan publik agar tidak menimbulkan masalah lagi",
            "Jelaskan sekali lagi bahwa proses normal dan jika lansia tidak puas, sampaikan bahwa setiap permohonan diproses sama tanpa pengecualian bagi siapapun",
            "Laporkannya ke pihak berwajib atas penyebaran informasi yang bisa merusak nama institusi tanpa bukti memadai"
        ],
        "answer": "Terima lansia dengan tenang, tunjukkan langsung progres permohonan di sistem, jelaskan tahap demi tahap dengan sabar, dan jika bersedia, dampingi lansia meluruskan informasi di grup WhatsApp warga secara langsung",
        "explanation": "Opsi B menunjukkan empati terhadap lansia sekaligus transparansi proaktif. Menunjukkan langsung progres di sistem memberi bukti konkret. Mendampingi di grup WhatsApp mengubah narasi dari tuduhan menjadi pendekatan humanis.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_004",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda kepala Bagian Keuangan di sebuah SKPD. Jelang akhir tahun anggaran, terdapat fenomena klasik: anggaran sisa sangat besar sementara banyak program belum terealisasi. Anda ditugasi atasan untuk mencairkan anggaran sisa semaksimal mungkin agar tidak dikembalikan ke kas negara, termasuk melalui program yang kualitasnya dipertanyakan. Beberapa program tersebut sudah diagendakan Dinas untuk kepentingan masyarakat tapi waktu pelaksanaan tidak memungkinkan. Anda...",
        "options": [
            "Laksanakan saja instruksi dari atas karena sebagai bawahan Anda hanya melaksanakan dan pertanggungjawaban ada pada atasan yang memerintahkan",
            "Tolak pelaksanaan program berkualitas rendah dan kembalikan anggaran sisa, karena menggunakan anggaran untuk program berkualitas rendah merupakan pelanggaran prinsip pengelolaan keuangan negara",
            "Lakukan review mendetail terhadap seluruh program tersisa, identifikasi mana yang benar-benar bermanfaat bagi masyarakat, sampaikan daftar prioritas kepada atasan dengan analisis risiko-realisasi setiap program terhadap sisa waktu, sarankan percepatan jika memungkinkan",
            "Sampaikan kepada atasan bahwa tidak ada program yang bisa dilaksanakan dengan sisa waktu sekecil ini dan biarkan anggaran kembali ke kas negara",
            "Sarankan program-program baru yang lebih mudah terealisasi dalam waktu singkat meskipun belum tentu dibutuhkan masyarakat"
        ],
        "answer": "Lakukan review mendetail terhadap seluruh program tersisa, identifikasi mana yang benar-benar bermanfaat bagi masyarakat, sampaikan daftar prioritas kepada atasan dengan analisis risiko-realisasi setiap program terhadap sisa waktu, sarankan percepatan jika memungkinkan",
        "explanation": "Opsi C menunjukkan integritas dengan tidak melaksanakan program bermasalah, profesionalisme dengan memberikan analisis berbasis data, dan loyalty struktural dengan tetap menyampaikan temuan kepada atasan dalam bentuk rekomendasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_005",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda diminta memimpin tim menyusun rencana kerja tahun depan. Riset lapangan menunjukkan bahwa program prioritas yang selama ini diagendakan oleh kepala dinas ternyata tidak sesuai dengan kebutuhan riil di lapangan. Data menunjukkan program tersebut justru berpotensi merugikan kelompok rentan yang menjadi target. Namun kepala dinas sudah menjanjikan program tersebut dalam forum Musrenbangdes. Jika Anda sampaikan data apa adanya, kepala dinas kehilangan muka. Jika Anda diam, masyarakat dirugikan.",
        "options": [
            "Sampaikan temuan lapangan secara jujur kepada kepala dinas secara tertutup terlebih dahulu, sertakan data dan analisis dampak terhadap kelompok rentan, minta arahan tentang cara penyajian yang tetap transparan namun menghargai posisi atasan",
            "Ikut serta dalam musrenbangdes dan sampaikan program sesuai keinginan kepala dinas karena musrenbangdes sudah decided dan tidak etis mengubah janji yang sudah disampaikan",
            "Sampaikan semua temuan lapangan apa adanya di musrenbangdes tanpa filter apapun dan biarkan kepala dinas menanggung konsekuensinya",
            "Hapus data yang merugikan dari laporan dan sampaikan program sesuai keinginan kepala dinas karena sebagai bawahan Anda harus melindungi atasan",
            "Minta waktu tambahan untuk memverifikasi data lapangan sebelum musrenbangdes agar tidak menyampaikan informasi yang belum pasti"
        ],
        "answer": "Sampaikan temuan lapangan secara jujur kepada kepala dinas secara tertutup terlebih dahulu, sertakan data dan analisis dampak terhadap kelompok rentan, minta arahan tentang cara penyajian yang tetap transparan namun menghargai posisi atasan",
        "explanation": "Opsi A menyeimbangkan antara integritas data, etika pejabat negara terhadap masyarakat, dan loyalty terhadap hierarki organisasi. Penyampaian tertutup terlebih dahulu memberikan ruang bagi kepala dinas untuk mempersiapkan respons.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_006",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Seorang ibu tunggal dengan tiga anak datang ke kantor Anda membawa bayi yang sedang demam tinggi. Ia memerlukan Surat Keterangan Tidak Mampu (SKTM) untuk berobat gratis. Namun Adminduk di desa tempat ia ber-KTP sedang tidak berfungsi karena server rusak sudah dua minggu dan belum ada timeline perbaikan. Ibu tersebut tidak memiliki KTP yang memadai untuk membuktikan domisili di wilayah Anda. Bayi semakin demam dan waktu sangat mendesak.",
        "options": [
            "Berikan SKTM berdasarkan pernyataan lisan ibu tersebut karena kondisi darurat memerlukan keputusan manusiawi dan bayi tidak boleh menjadi korban kerusakan sistem",
            "Jelaskan situasi dengan empati, bantu ibu menghubungi rumah sakit terdekat untuk perawatan darurat terlebih dahulu tanpa SKTM karena UU Kesehatan memperbolehkan perawatan darurat tanpa identitas lengkap, kemudian bantu联络 Adminduk agar server diperbaiki secepatnya",
            "Tidak bisa memberikan SKTM karena tidak ada data yang valid untuk mendukung, sarankan ibu pergi ke rumah sakit umum dan menjelaskan situasinya di sana",
            "Berikan SKTM tanpa dasar data yang memadai karena kasihan terhadap kondisi ibu dan bayi, prioritaskan aspek kemanusiaan di atas prosedur",
            "Minta ibu menunggu sampai server berfungsi kembali karena prosedur harus tetap ditaati dan tidak ada pengecualian bagi siapapun"
        ],
        "answer": "Jelaskan situasi dengan empati, bantu ibu联系的 rumah sakit terdekat untuk perawatan darurat terlebih dahulu tanpa SKTM karena UU Kesehatan memperbolehkan perawatan darurat tanpa identitas lengkap, kemudian bantu联络 Adminduk agar server diperbaiki secepatnya",
        "explanation": "Opsi B menunjukkan pemahaman mendalam terhadap regulasi, empati tanpa melanggar prosedur, dan inisiatif untuk menyelesaikan akar masalah. Ibu mendapat perawatan mendesak dan masalah sistemik ikut ditindaklanjuti.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_007",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Anda mengelola pengaduan masyarakat di sebuah instansi pemerintah. Dalam sebulan terakhir, muncul pola pengaduan sistematis dari sekumpulan akun media sosial berbeda yang semuanya mengarah ke isu yang sama: bahwa Anda sebagai pejabat telah melakukan diskriminasi layanan terhadap warga dari etnis tertentu. Investigation internal menunjukkan bahwa pengaduan tersebut kemungkinan besar bukan dari warga nyata melainkan dari akun terorganisir yang dibayar untuk mendiskreditkan. Namun beberapa warga mulai mempertanyakan karena mereka melihat pengaduan di media sosial.",
        "options": [
            "Abaikan semua pengaduan dari media sosial karena tidak bisa diverifikasi dan pengaduan resmi tidak ada, biarkan isu mereda sendiri karena tidak memiliki dasar",
            "Lakukan investigation internal menyeluruh, jika ditemukan bukti coordinated attack, sampaikan temuan secara terbuka bahwa pengaduan tidak berdasar dan merupakan serangan terorganisir, serta sampaikan data layanan riil yang menunjukkan tidak ada diskriminasi",
            "Temui kelompok etnis yang dimaksud secara langsung, jelaskan bahwa tidak ada diskriminasi dan minta mereka membela Anda di media sosial",
            "Laporkan semua akun media sosial ke police untuk cyber defamation karena pengaduan palsu yang terorganisir adalah tindak pidana",
            "Segera keluarkan pernyataan resmi bahwa Anda tidak pernah melakukan diskriminasi dan mengancam akan bertindak hukum terhadap siapapun yang menyebarkan informasi palsu"
        ],
        "answer": "Lakukan investigation internal menyeluruh, jika ditemukan bukti coordinated attack, sampaikan temuan secara terbuka bahwa pengaduan tidak berdasar dan merupakan serangan terorganisir, serta sampaikan data layanan riil yang menunjukkan tidak ada diskriminasi",
        "explanation": "Opsi B menunjukkan respons yang berimbang: tetap profesional dengan investigation, merespons dengan data konkret saat ditemukan pola tidak legitimate. Pendekatan transparan membangun kepercayaan publik.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_008",
        "category": "TKP",
        "subcategory": "Pelayanan Publik",
        "question": "Sebuah台风 besar akan melewati wilayah Anda dalam 48 jam. Anda sebagai kepala desa menyusun rencana evakuasi. Data menunjukkan rumah-rumah di bantaran sungai berisiko tinggi, namun sebagian penghuninya adalah lansia dan penyandang disabilitas yang menolak meninggalkan rumah karena tidak ada yang menjaga ternak dan harta benda. Beberapa warga muda menghalang-halangi upaya evakuasi dengan alasan takhayul. Saat bersamaan, Anda mendapat instruksi dari kecamatan untuk memastikan zero casualty.",
        "options": [
            "Paksa evakuasi semua warga dengan bantuan TNI/Polri karena instruksi dari kecamatan bersifat mengikat dan zero casualty tidak bisa dinegosiasikan",
            "Lakukan pendekatan door-to-door dengan tim yang terdiri dari petugas kesehatan, tokoh agama, dan volunteers, pahami kekhawatiran masing-masing warga, sediakan logistik dan koordinasi dengan tetangga untuk menjaga ternak selama evakuasi, serta tegaskan risiko hukum bagi yang tetap menolak",
            "Evakuasi hanya warga yang mau pergi dan sampaikan kepada kecamatan bahwa sebagian warga menolak sehingga zero casualty tidak mungkin dipenuhi",
            "Percaya prediksi BMKG yang sering salah dan biarkan warga memilih sendiri karena evakuasi paksa adalah pelanggaran terhadap hak pribadi",
            "Tunda semua keputusan sampai台风 benar-benar akan mendarat karena evakuasi dini akan menimbulkan kepanikan yang tidak perlu"
        ],
        "answer": "Lakukan pendekatan door-to-door dengan tim yang terdiri dari petugas kesehatan, tokoh agama, dan volunteers, pahami kekhawatiran masing-masing warga, sediakan logistik dan koordinasi dengan tetangga untuk menjaga ternak selama evakuasi, serta tegaskan risiko hukum bagi yang tetap menolak",
        "explanation": "Opsi B menunjukkan kepemimpinan situasional yang kompleks: menggabungkan empati, sinergi tim multidisiplin, pemecahan masalah konkret, komunikasi risiko yang jelas, dan tetap berpegang pada instruksi hierarki.",
        "difficulty": "hard"
    },
    # === JEJARING KERJA (7) ===
    {
        "id": "tkp3_009",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda seorang pejabat eselon III yang baru rotasi ke SKPD baru setelah 8 tahun di instansi sebelumnya. Di SKPD baru, Anda menemukan bahwa tim kerja terbelah menjadi dua kubu: satu mendukung mantan pejabat yang sudah pensiun, satu lagi mendukung pejabat saingan internal yang masih aktif. Keduanya sama-sama mencoba mendapatkan dukungan Anda. Kinerja SKPD jelas menurun karena energi terbuang untuk politik internal.",
        "options": [
            "Dukung kubu mantan pejabat pensiun karena dialahmembawah Anda ke posisi ini dan loyalitas personal penting dalam birokrasi",
            "Dukung pejabat yang masih aktif karena dia masih memiliki kekuasaan untuk mempengaruhi karier Anda ke depan",
            "Netral secara politik, fokuskan seluruh energi pada penyelesaian backlog kerja dan bangun kepercayaan dari tim berdasarkan kinerja objektif, namun tetap terbuka berkomunikasi dengan semua pihak secara profesional tanpa menunjukkan pembelaan",
            "Pilih pihak yang menurut analisis Anda memiliki program kerja paling sejalan dengan kepentingan masyarakat meskipun mereka saat ini kalah dalam pertarungan internal",
            "Lapor ke inspektorat bahwa SKPD ini memiliki проблема politik internal yang mengganggu kinerja sehingga perlu intervensi atasan"
        ],
        "answer": "Netral secara politik, fokuskan seluruh energi pada penyelesaian backlog kerja dan bangun kepercayaan dari tim berdasarkan kinerja objektif, namun tetap terbuka berkomunikasi dengan semua pihak secara profesional tanpa menunjukkan pembelaan",
        "explanation": "Opsi C menunjukkan profesionalisme tinggi di lingkungan kompleks. Netralitas bukan ketidakpedulian tapi posisi strategis yang memungkinkan bekerja efektif. Membangun kepercayaan berbasis kinerja menghindari kolusi dengan keduanya.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_010",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda diundang ke forum internasional tentang good governance untuk mempresentasikan inovasi pelayanan publik di daerah Anda. Saat menyusun materi, Anda sadar bahwa inovasi yang dipromosikan merupakan adaptasi dari program daerah lain yang pernah Anda lihat saat benchmarking, dengan sedikit modifikasi. Daerah Anda tidak pernah menuliskan sumber inspirasi tersebut. Presentasi besok dan Anda harus memutuskan...",
        "options": [
            "Presentasikan sebagaimana adanya karena semua daerah saling belajar dan tidak ada yang bisa mengklaim inovasi 100% asli, selama program ini benar-benar memberikan manfaat bagi warga",
            "Sebutkan bahwa program merupakan pengembangan dari best practice daerah lain yang pernah menjadi referensi, namun sampaikan secara umum tanpa menyebut nama spesifik karena tidak ingin terkesan mengekspos referensi",
            "Telusuri terlebih dahulu apakah program daerah asal sudah dipatenkan atau dilindungi secara kekayaan intelektual, jika tidak, proceed dengan menyebutkan sumber inspirasi secara terbuka",
            "Ubah presentasi untuk menghapus semua elemen yang terlihat mirip dengan program daerah lain dan klaim sebagai hasil riset mandiri科室",
            "Batalkan presentasi karena tidak ada cukup waktu untuk memverifikasi sumber inspirasi dan lebih baik tidak presentasi daripada mengklaim sesuatu yang belum pasti"
        ],
        "answer": "Telusuri terlebih dahulu apakah program daerah asal sudah dilindungi secara kekayaan intelektual, jika tidak, proceed dengan menyebutkan sumber inspirasi secara terbuka",
        "explanation": "Opsi C menunjukkan integritas akademik dan profesional. Mengakui sumber inspirasi bukan kelemahan tapi演示 kejujuran intelektual yang dihormati di forum internasional. Pendekatan ini riset-based, tidak memalsakan klaim, dan tetap memungkinkan presentasi berjalan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_011",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda menyusun kebijakan publik yang evidence-based dan bermaksud mengundang narasumber dari dunia usaha, akademisi, dan LSM. Anda sadar bahwa narasumber dunia usaha cenderung memiliki kepentingan ekonomi, akademisi mungkin terlalu teoritis tanpa realitas lapangan, dan LSM mungkin memiliki agendapartisannya sendiri.",
        "options": [
            "Ajak только LSM dan akademisi karena dua kelompok ini memiliki integritas lebih tinggi daripada dunia usaha yang hanya mementingkan untung",
            "Ajak semua narasumber tanpa diskriminasi, namun buat kerangka diskusi yang terstruktur dengan pertanyaan yang mengarahkan setiap kelompok memberikan perspektif yang seimbang dan mewaspadai bias masing-masing",
            "Lakukan semua perencanaan sendiri tanpa narasumber eksternal karena semua kelompok memiliki bias dan lebih baik mengandalkan penilaian internal yang netral",
            "Ajak только dunia usaha karena merekalah yang paling memahami realitas ekonomi dan akan memberikan data paling aktual tentang kondisi riil",
            "Serahkan sepenuhnya kepada narasumber untuk menentukan topik diskusi karena merekalah yang paling kompeten di bidangnya masing-masing"
        ],
        "answer": "Ajak semua narasumber tanpa diskriminasi, namun buat kerangka diskusi yang terstruktur dengan pertanyaan yang mengarahkan setiap kelompok memberikan perspektif yang seimbang dan mewaspadai bias masing-masing",
        "explanation": "Opsi B menunjukkan pendekatan pluralistis yang memperkaya kebijakan dengan beragam perspektif, sekaligus moderasi profesional untuk mengurangi bias. Fasilitator yang baik bukan menghilangkan perspektif tapi mengorganisir它们 menjadi diálogo konstruktif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_012",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda diminta mempromosikan program lintas sektoral yang melibatkan 5 SKPD berbeda. Setiap SKPD memiliki kepala dengan gaya kepemimpinan dan prioritas sangat berbeda. Beberapa di antaranya openly tidak mendukung program karena merasa bukan prioritas mereka dan menghabiskan sumber daya. Namun program ini sudah dijanjikan kepada wakil rakyat dan tidak bisa ditarik kembali. Anda tidak memiliki wewenang formal untuk menginstruksikan SKPD manapun.",
        "options": [
            "Minta dituliskan instruksi dari bupati/wali kota yang mewajibkan semua SKPD berpartisipasi karena tanpa dukungan hierarkis tertinggi program tidak akan jalan",
            "Buat presentasi yang menunjukkan bagaimana program ini memberikan benefit konkret bagi target indikator masing-masing SKPD, lakukan pertemuan individual dengan setiap kepala SKPD untuk memahami kekhawatiran mereka, dan tetapkan mekanisme kompensasi jika ada SKPD yang merasa dirugikan secara sumber daya",
            "Fokus pada 2-3 SKPD yang sudah mendukung dan abaikan yang tidak mendukung karena mereka akan ketinggalan dari keberhasilan program",
            "Serahkan semuanya ke Sekretariat Daerah sebagai koordinator lintas sektor karena bukan tugas Anda untuk mengkoordinasikan SKPD yang bukan bawahan Anda",
            "Tawarkan insentif anggaran tambahan kepada SKPD yang mendukung program agar mereka mau berpartisipasi aktif"
        ],
        "answer": "Buat presentasi yang menunjukkan bagaimana program ini memberikan benefit konkret bagi target indikator masing-masing SKPD, lakukan pertemuan individual dengan setiap kepala SKPD untuk memahami kekhawatiran mereka, dan tetapkan mekanisme kompensasi jika ada SKPD yang merasa dirugikan secara sumber daya",
        "explanation": "Opsi B menunjukkan leadership berbasis collaborative influence tanpa wewenang formal. Pendekatan ini memahami different interests, menerjemahkan program ke bahasa each stakeholder, dan menemukan solusi win-win.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_013",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda mengelola akun resmi media sosial instansi. Seorang kolega yang tidak terverifikasi dan tidak memiliki wewenang resmi untuk berkomunikasi di media sosial secara регулярно comment pada postingan resmi instansi dengan pandangan pribadi yang часто bertentangan dengan позиция resmi. Sebagian commenternya mendukung pandangan kolega tersebut karena dianggap lebih jujur daripada official account. Kolega berdalih bahwa warga berhak mendengar berbagai pandangan dan official account terlalu kaku.",
        "options": [
            "Biarkan karena setiap warga memiliki свобода pendapat dan tidak ada yang bisa melarang seseorang berpendapat di media sosial",
            "Bicara langsung kepada kolega secara personal tentang SOP komunikasi media sosial instansi, jelaskan implikasi dari pandangan pribadi yang dikaitkan dengan institusi, minta ia membedakan pandangan pribadi dan official, dan sampaikan bahwa jika tidak dihentikan, akan将此问题上报 ke atasan",
            "Buat klarifikasi resmi bahwa semua pernyataan yang发布 oleh official account adalah позиция resmi dan pandangan siapapun yang 发布 oleh неофициальный account adalah pandangan pribadi, untuk menjaga transparansi bagi publik",
            "Laporkannya ke bidang hukum atas pelanggaran etika berkomunikasi pejabat di media sosial",
            "Buat aturan internal bahwa semua pejabat harus memblokir teman kerja dari akun media sosial resmi instansi untuk menghindari komentar tidak sah"
        ],
        "answer": "Bicara langsung kepada kolega secara personal tentang SOP komunikasi media sosial instansi, jelaskan implikasi dari pandangan pribadi yang dikaitkan dengan institusi, minta ia membedakan pandangan pribadi dan official, dan sampaikan bahwa jika tidak dihentikan, akan将此问题上报 ke atasan",
        "explanation": "Opsi B memberikan escalation ladder yang wajar: mulai dari komunikasi personal, klarifikasi dampak, permintaan perbaikan mandiri, dan ancaman escalate as last resort. Ini memberi kolega kesempatan untuk memperbaiki tanpa langsung dihukum.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_014",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda diminta mengepalai tim lintas fungsi dengan短期限 untuk menyusun kajian tentang efektivitas无人机 untuk мониторинг lingkungan. Tim terdiri dari anggota berbagai SKPD yang belum pernah bekerja sama sebelumnya. Beberapa anggota terlihat sangat kompeten dan proaktif, sementara yang lain cenderung pasif dan menunggu arahan. Waktu tersisa tiga minggu dan tim harus menghasilkan kajian yang bisa dipertanggungjawabkan di hadapan legislator.",
        "options": [
            "Bagi tugas berdasarkan kemampuan individu yang terobservasi, beri deadline tegas untuk setiap deliverable, konfirmasi setiap minggu apakah target tercapai, dan siap реструктурировать tim jika ada yang tidak mampu memenuhi standar",
            "Biarkan tim bekerja secara organik karena форсированная struktur akan membunuh kreativitas dan untuk kajian ilmiah diperlukan kebebasan berpikir",
            "Lakukan voting di antara anggota tim untuk menentukan siapa yang paling kompeten dan serahkan pengoperasian tim kepada orang tersebut",
            "Kumpulkan semua anggota dan minta masing-masing menulis bagian kajian sesuai keinginan mereka sendiri tanpa struktur yang ketat agar semua merasa berkontribusi",
            "Serahkan semua pekerjaan kepada anggota yang paling kompeten dan beri mereka remunerasi额外的 untuk menghargai kontribusinya"
        ],
        "answer": "Bagi tugas berdasarkan kemampuan individu yang terobservasi, beri deadline tegas untuk setiap deliverable, konfirmasi setiap minggu apakah target tercapai, dan siap реструктурировать tim jika ada yang tidak mampu memenuhi standar",
        "explanation": "Opsi A menunjukkan situational leadership yang tepat untuk tim proyek short-term: assign berdasarkan kapabilitas, establish clear milestones, monitor progress регулярно, dan have contingency. Pendekatan results-oriented tapi tetap struktural.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_015",
        "category": "TKP",
        "subcategory": "Jejaring Kerja",
        "question": "Anda dipercayakan mengelola proyek kerja sama antara pemerintah daerah dan sektor swasta untuk pembangunan infrastruktur. Kontraktor yang memenangkan лот memiliki reputasi baik secara nasional namun catatan lingkungan dari proyek-proyek sebelumnya menunjukkan beberapa insiden. Warga di sekitar lokasi mulai'organize protes. Kontraktor mengklaim semua insiden sudah resolved dan tidak relevan dengan проекtn ini. Anda sebagai pengawas pemerintah.",
        "options": [
            "Percaya klaim kontraktor karena perusahaan bereputasi nasional dan insiden masa lalu bukan tanggung jawab proyek saat ini",
            "Tetapkan klausul lingkungan yang lebih ketat dalam kontrak, libatkan partisipasi warga untuk monitoring, lakukan audit lingkungan berkala независимый, dan jika ditemukan pelanggaran baru, terapkan sanksi kontraktual yang sudah disepakati",
            "Batalkan proyek karena reputasi lingkungan kontraktor sudah dipertanyakan dan tidak ada jaminan warga tidak akan terus protes",
            "Serahkan sepenuhnya kepada институт lingkungan government untuk pengawasan karena itu bukan tugas Anda sebagai pengawas proyek dari sisi pemerintah",
            "Sarankan warga untuk tidak interfering dengan proyek karena perusahaan sudah memiliki semua izin yang diperlukan dari instans terkait"
        ],
        "answer": "Tetapkan klausul lingkungan yang lebih ketat dalam kontrak, libatkan partisipasi warga untuk monitoring, lakukan audit lingkungan berkala независимый, dan jika ditemukan pelanggaran baru, terapkan sanksi kontraktual yang sudah disepakati",
        "explanation": "Opsi B menunjukkan pendekatan balanced governance: tidak langsung blacklist perusahaan karena insiden lama, tapi tetap pasang guardrails yang lebih kuat untuk proyek ini. Libatkan warga, audit independen, dan enforce kontraktual menunjukkan akuntabilitas.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_016",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Anda mengelola program bantuan sosial untuk keluarga miskin di daerah dengan adat kuat bahwa мужчины adalah kepala keluarga dan женщина tidak boleh menerima bantuan langsung atas nama suami. Secara regulasi, tidak ada diskriminasi gender dalam program ini. Namun adat sangat kuat dan jika Anda berikan bantuan langsung kepada perempuan (meskipun itu hak mereka secara hukum), kemungkinan besar akan terjadi конфликт sosial dengan tetua adat yang dapat mengganggu implementasi program secara keseluruhan.",
        "options": [
            "Berikan bantuan langsung kepada perempuan sesuai regulasi karena kesetaraan gender adalah prinsip konstitusional dan adat tidak boleh выше закона negara",
            "Lakukan dialog préalable dengan tetua adat, jelaskan regulasi dan hak perempuan, minta mereka menjadi champion perubahan sosial karena program ini memberi manfaat langsung kepada keluarga mereka, dan jika mereka setuju, sampaikan secara adat bahwa bantuan ini adalah hak perempuan namun atas restu tetua",
            "Berikan bantuan kepada мужчина (kepala keluarga) meskipun secara regulasi merugikan perempuan, untuk menjaga harmony sosial karena implementasi program lebih penting dari interpretasi hukum",
            "Бойкотировать program entirely karena regulasi dan adat tidak bisa didamaikan dan Anda tidak mau menjadi penyebab konflik sosial",
            "Serahkan выбор penerima kepada tetua adat sepenuhnya karena merekalah yang paling memahami struktur sosial setempat"
        ],
        "answer": "Lakukan dialog préalable dengan tetua adat, jelaskan regulasi dan hak perempuan, minta mereka menjadi champion perubahan sosial karena program ini memberi manfaat langsung kepada keluarga mereka, dan jika mereka setuju, sampaikan secara adat bahwa bantuan ini adalah hak perempuan namun atas restu tetua",
        "explanation": "Opsi B merupakan diplomasi sosial budaya yang sophisticated: tidak imposing perubahan dari atas, tapi engage pemangku kepentingan kunci sebagai agent of change, memberikan mereka ownership atas solusi, sehingga perubahan yang seharusnya konflik dimediasi oleh mereka sendiri.",
        "difficulty": "hard"
    },
    # === SOSIAL BUDAYA (7) ===
    {
        "id": "tkp3_017",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Daerah Anda akan menjadi tuan rumah sebuah kelompok etnis minoritas untuk relokasi dari daerah yang akan tenggelam akibat pembangunan bendungan. Mereka memiliki budaya, bahasa, dan agama yang berbeda signifikan dari penduduk lokal. Penduduk lokal mulai membentuk kelompok反对 terhadap kedatangan dengan alasan mereka akan mengambil lapangan kerja dan mengubah demografi. Situasi начинает escalate.",
        "options": [
            "Panggil kedua pihak untuk mediasi, jelaskan bahwa ксенофобия adalah противозаконно dan приговор akan dituntut, serta sampaikan bahwa relokasi adalah программа государственный",
            "Блокируйте informasi tentang jumlah dan asal mereka dari kelompok minoritas karena masyarakat tidak perlu tahu detail dan ini bisa mengurangi kecemasan",
            "Adakan forum diálogo où kedua kelompok bertemu dalam lingkungan terkontrol, fasilitasi agar penduduk lokal mendengar langsung dari kelompok minoritas tentang kondisi mereka, sampaikan rencana integrasi yang jelas включая программы pelatihan dan bantuan untuk adaptasi kedua arah, dan tetapkan mekanisme pengaduan bersama",
            "Larang penduduk lokal membentuk kelompok apapun terkait kelompok minoritas karena это bisa membentuk волнения и угроза terhadap stabilitas",
            "Serahkan semua penanganan kepada Kementerian Sosial karena ini adalahmasalah nasional yang berada di luar wewenang daerah"
        ],
        "answer": "Adakan forum diálogo où kedua kelompok bertemu dalam lingkungan terkontrol, fasilitasi agar penduduk lokal mendengar langsung dari kelompok minoritas tentang kondisi mereka, sampaikan rencana integrasi yang jelas включая программы pelatihan dan bantuan untuk adaptasi kedua arah, dan tetapkan mekanisme pengaduan bersama",
        "explanation": "Opsi C menunjukkan strategi integrasi sosial yang matang. Dialogue intergroup dalam setting terkontrol membangun empati, transparansi rencana integrasi mengurangi ketakutan, программа двусторонняя адаптация menunjukkan kesetaraan, mekanisme pengaduan memberikan kontrol kepada keduanya.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_018",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Anda kepala daerah yang harus memutuskan apakah daerah Anda menjadi tuan rumah festival budaya yang sudah ada selama ratusan tahun tetapi mengandung beberapa elemen yang oleh kelompok tertentu dianggap sebagai практики мистический yang bertentangan dengan nilai-nilai agama mainstream. Festival tersebut merupakan warisan budaya yang diakui oleh Kementerian Budaya dan menarik wisatawan dalam dan luar negeri. Kelompok progresif menuntut agar festival dibatalkan karena dianggap tidak sesuai dengan perkembangan zaman.",
        "options": [
            "Batalkan festival karena kelompok agama memiliki pengaruh kuat terhadap elektoral dan Anda tidak ingin kehilangan dukungan mereka di следующий elections",
            "Dukung festival karena sudah berjalan ratusan tahun dan warisan budaya harus dilindungi независимо от мнения kelompok kecil yang tidak representatif",
            "Konsultasikan dengan kedua pihak, historian dan anthropologist untuk mendapatkan perspektif historis dan ilmiah, lihat konteks antropologis festival tersebut, dan jika ditemukan elemen yang bermasalah, bedakan antara elemen yang bisa dimodifikasi dan yang merupakan inti dari warisan budaya yang tidak bisa diubah, lalu sampaikan keputusan dengan данные",
            "Бойкотировать semua kegiatan budaya daerah untuk mencegah konflik dan sebagai gantinya fokuskan anggaran untuk kegiatan yang lebih modern dan inklusif",
            "Serahkan keputusan kepada publik melalui referendum karena ini adalah вопрос культурный yang seharusnya dipilih oleh masyarakat secara демократический"
        ],
        "answer": "Konsultasikan dengan kedua pihak, historian dan anthropologist untuk mendapatkan perspektif historis dan ilmiah, lihat konteks antropologis festival tersebut, dan jika ditemukan elemen yang bermasalah, bedakan antara elemen yang bisa dimodifikasi dan yang merupakan inti dari warisan budaya yang tidak bisa diubah, lalu sampaikan keputusan dengan data",
        "explanation": "Opsi C menunjukkan pengambilan keputusan berbasis bukti di area yang sarat emosi. Tidak memilih sisi berdasarkan tekanan politik, tapi mencari konteks historis dan ilmiah untuk membedakan fakta dari persepsi. Pendekatan ini tidak mengubah budaya seenaknya tapi juga tidak rigid mempertahankan semua.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_019",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Daerah Anda memiliki komunitas digital creator muda yang sangat aktif. Mereka rutin membuat konten tentang kondisi pemerintahan daerah yang sometimes not flattering. Beberapa видео показывает kritik tajam terhadap pejabat termasuk Anda sendiri, meskipun dalam bentuk komedi. Sebagian besar warga lokal positif terhadap konten mereka. Одновременно, beberapa pejabat старший merasa tidak dihormati dan tekanan kepada Anda untuk mengambil tindakan.",
        "options": [
            "Ambil tindakan демонстратив terhadap kreator sebagai contoh untuk mencegah kritik lebih lanjut karena pejabat harus dihormati sebagai representasi pemerintah",
            "Abaikan semua видео karena kebebasan berpendapat adalah hak konstitusional dan selama tidak ada fitnah atau defamasi, tidak ada dasar untuk bertindak",
            "Hubungi kreator secara personal, apresiasi kreativitas mereka, jelaskan secara jujur bagaimana beberapa konten yang mengkritik pemerintah memiliki dampak terhadap persepsi publik tentang institusi, minta mereka mempertimbangkan untuk tetap produktif dalam kritik yang konstruktif dan berbasis data, dan tawarkan kolaborasi untuk membuat konten positif tentang upaya pemerintah tanpa interfering dengan kebebasan mereka",
            "Laporkan ke platform YouTube/TikTok bahwa video mengandung критики terhadap pemerintah yang bisa mendestabilisasi dan minta dihapus",
            "Buat kontra-narrative dengan menyediakan akun resmi pemerintah yang aktif memposting konten positif untuk menandingi kritik"
        ],
        "answer": "Hubungi kreator secara personal, apresiasi kreativitas mereka, jelaskan secara jujur bagaimana beberapa konten yang mengkritik pemerintah memiliki dampak terhadap persepsi publik tentang institusi, minta mereka mempertimbangkan untuk tetap produktif dalam kritik yang konstruktif dan berbasis data, dan tawarkan kolaborasi untuk membuat konten positif tentang upaya pemerintah tanpa interfering dengan kebebasan mereka",
        "explanation": "Opsi C adalah pendekatan yang nuanced: hargai kreativitas muda tanpa adversarial, jelaskan dampak tanpa угрожать, minta pertimbangan tanpa memaksa, dan tawarkan kolaborasi tanpa комаando. Melindungi kebebasan berpendapat sambil membuka diálogo konstruktif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_020",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Anda seorang kepala dinas yang harus memutuskan apakah bantuan alat produksi untuk pengrajin tenun akan dilanjutkan atau dialihkan ke sektor lain. Setelah dievaluasi, program tenun показывает hasil tidak memenuhi ekspektasi: pendapatan pengrajin tidak meningkat signifikan karena produk tidak bisa bersaing dengan buatan mesin. Namun pengrajin dan komunitasnya sangat attached terhadap tradisi tenun sebagai bagian identitas budaya mereka. Beberapa pengrajin старший even menangis saat mendengar penghentian program.",
        "options": [
            "Hentikan program karena hasil tidak memenuhi indikator dan sumber daya negara terbatas sehingga harus dialihkan ke программы yang lebih эффективный",
            "Lanjutkan program karena pelestarian budaya adalah tujuan yang sah meskipun tidak menghasilkan return ekonomi langsung, dan carilah sumber pendanaan альтернативный yang tidak bergantung pada возвращение экономический",
            "Lakukan averitisasi tujuan program sebelum memutuskan, fasilitasi diálogo antara pengrajin, pakarnya (economist, anthropologist, designer), dan потенциальный buyer untuk melihat apakah ada модели bisnis alternatif yang bisa menjembatani pelestarian budaya dan viabilitas ekonomi",
            "Netralkan sebagian kecil dana untuk tenun sebagai компания budaya dan alihkan sebagian besar ke sektor yang lebih produktif",
            "Serahkan keputusan kepada pengrajin sendiri karena merekalah yang paling berkepentingan"
        ],
        "answer": "Lakukan averitisasi tujuan program sebelum memutuskan, fasilitasi diálogo antara pengrajin, pakarnya (economist, anthropologist, designer), dan потенциальный buyer untuk melihat apakah ada модели bisnis alternatif yang bisa menjembatani pelestarian budaya dan viabilitas ekonomi",
        "explanation": "Opsi C menunjukkan pengambilan keputusan bijaksana di persimpangan budaya dan ekonomi. Averitisasi membuka opsi-opsi kreatif yang mungkin tidak terpikirkan sebelumnya. Modelo inovasi sosial sering muncul dari sini. Bukan kompromi yang tidak satisfying siapa pun, bukan abdikasi pengambilan keputusan publik.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_021",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Anda mengelola organisasi perangkat daerah dengan sejarah panjang budaya корпоративная où kritik terhadap kepemimpinan dianggap sebagai нелояльность dan secara rutin会导致 konsekuensi karier. Baru ditunjuk sebagai pemimpin. Beberapa staf senior privately sampaikan bahwa budaya ini sudah berjalan lama dan mereka menganggapnya normal. Anda sendiri adalah produk dari budaya корпоративная yang lebih terbuka. Anda ingin mengubah budaya ini tapi sadar bahwa mengubah budaya yang sudah mengakar sulit dan memerlukan waktu lama.",
        "options": [
            "Biarkan budaya seperti adanya karena Anda adalah pendatang baru dan tidak ada ruang untuk mengubah budaya kerja yang sudah berjalan lama diinstansi ini",
            "Segera keluarkan memo resmi bahwa kritik terhadap kepemimpinan adalah hak setiap staf dan akan dilindungi, serta sampaikan bahwa siapapun yang memberikan konsekuensi akan ditindak",
            "Demonstrasikan keterbukaan secara bertahap: mulai dari menerima kritik konstruktif secara pribadi dari siapapun tanpa dendam, kemudian secara teratur minta umpan balik dari tim, buat anonymous suggestion box, dan setelah trust mulai terbangun, secara organisasional reformasikan SOP komunikasi yang lebih terbuka, sambil терпеливо menunggu perubahan budaya yang bertahap",
            "Identifikasi siapa influencer utama dalam budaya lama dan minta mereka untuk помогить mengubah budaya karena mereka adalah yang paling berpengaruh terhadap staf lain",
            "Lapor ke inspektorat bahwa budaya институциональный sudah represif dan meminta intervensi eksternal"
        ],
        "answer": "Demonstrasikan keterbukaan secara bertahap: mulai dari menerima kritik konstruktif secara pribadi dari siapapun tanpa dendam, kemudian secara teratur minta umpan balik dari tim, buat anonymous suggestion box, dan setelah trust mulai terbangun, secara organisasional reformisasikan SOP komunikasi yang lebih terbuka, sambil терпеливо menunggu perubahan budaya yang bertahap",
        "explanation": "Opsi C menunjukkan kepemimpinan transformasi budaya: tidak instant transformation (B would backfire), tidak accept status quo (A), tidak hanya rely on influencer (D), dan tidak escalate prematurely (E). Leadership by example membangun trust yang diperlukan untuk perubahan kultural.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_022",
        "category": "TKP",
        "subcategory": "Sosial Budaya",
        "question": "Sebuah daerah dengan tingkat putus sekolah tinggi muncul data bahwa penyebab utama bukan экономическая melainkan budaya: banyak keluarga yang dengan sadar memilih menikahkan anak perempuan di usia muda karena menganggap это lebih bermanfaat экономически dibandingkan melanjutkan pendidikan. Data menunjukkan pernikahan muda berkorelasi dengan indikator kesehatan yang lebih rendah bagi ibu dan anak. Обоснование orang tua: это budaya dan tradisi kami, dan вмешательство dari luar adalah pelanggaran hak asasi manusia atas самоопределение budaya.",
        "options": [
            "Terima karena setiap kelompok budaya memiliki hak untuk menentukan nilai-nilai mereka sendiri dan intervensi luar adalah bentuk neokolonialisme",
            "Desain программу yang bekerja dengan tokoh adat dan agama yang dihormati di komunitas, untuk menemukan внутри самой культуры argumen yang bisa mendukung pendidikan perempuan tanpa externally imposing, seperti menggali figur perempuan terdidik dalam sejarah mereka sendiri yang bisa menjadi role model, sambil экономически incentivize keluarga yang memilih pendidikan",
            "Berlakukan sanksi terhadap keluarga yang menikahkan anak di bawah umur karena это adalah pelanggaran hukum dan tidak bisa dibenarkan dengan alasan budaya",
            "Abaikan data karena ini adalah urusan privasi keluarga dan pemerintah tidak memiliki hak untuk interfere dalam keputusan privat keluarga",
            "Lakukan riset lebih lanjut untuk memverifikasi data sebelum mengambil tindakan apapun"
        ],
        "answer": "Desain программу yang bekerja dengan tokoh adat dan agama yang dihormati di komunitas, untuk menemukan внутри самой культуры argumen yang bisa mendukung pendidikan perempuan tanpa externally imposing, seperti menggali figur perempuan terdidik dalam sejarah mereka sendiri yang bisa menjadi role model, sambil экономически incentivize keluarga yang memilih pendidikan",
        "explanation": "Opsi B menunjukkan pendekatan canggih untuk isu sensitif budaya: tidak membiarkan harmful practice, tidak imposing nilai eksternal, tapi bekerja dari dalam budaya menggunakan agent of change internal. Pendekatan ini menggabungkan advokasi dengan rasa hormat.",
        "difficulty": "hard"
    },
    # === TIK (8) ===
    {
        "id": "tkp3_023",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "Instansi Anda akan bermigrasi dari sistem manual ke digital government. Beberapa staf senior mengungkapkan kuat kekhawatiran: mereka sudah puluhan tahun dengan sistem manual dan merasa aman dengannya, sementara sistem digital menurut mereka adalah ancaman terhadap pekerjaan karena tidak familiar dengan teknologi. Sebagian开始 membuat gerakan menolak yang terorganisir dan bahkan melibatkan serikat pekerja. Реформация digital adalah prioritas nasional dan Anda akan dievaluasi по нему.",
        "options": [
            "Paksakan migrasi digital karena это adalah instruksi nasional dan siapapun yang menolak akan digantikan dengan generasi yang lebih digitally literate",
            "Abandon migrasi digital karena risiko konflik dengan tenaga kerja terlalu tinggi dan Anda tidak mau bertanggung jawab atas destabilisasi organisasi",
            "Buat программу change management: identifikasi digital champion среди staf senior yang bisa menjadi contoh, berikan intensive training yang disesuaikan dengan learning curve каждого, fase out sistem manual secara gradual dengan periode transisi где kedua sistem berjalan параллельно, dan guarantee bahwa digitalisasi memperluas Möglichkeiten pekerjaan rather than menggantikan mereka",
            "Безусловно слепо следуйте instruksi digitalisasi tanpa mempedulikan kekhawatiran staf karena они будет adapt atau tidak, itu bukan urusan Anda",
            "Beri staf pilihan: yang mau migrasi akan mendapat insentif, yang tidak mau akan tetap di posisi manual tapi dengan evaluasinya yang lebih rendah"
        ],
        "answer": "Buat программу change management: identifikasi digital champion среди staf senior yang bisa menjadi contoh, berikan intensive training yang disesuaikan dengan learning curve каждого, fase out sistem manual secara gradual dengan periode transisi где kedua sistem berjalan параллельно, dan guarantee bahwa digitalisasi memperluas Möglichkeiten pekerjaan rather than menggantikan mereka",
        "explanation": "Opsi C menunjukkan change management leadership yang mature. Change management terbaik bekerja dengan resistência sebagai data tentang kebutuhan, bukan sebagai masalah yang harus dieliminasi. Pendekatan phased mengurangi risiko, training adapted menunjukkan respek terhadap individual learning curve.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_024",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "Anda diminta mengevaluasi предложение dari perusahaan teknologi untuk membangun smart city system di daerah Anda. предложение mencakup pengumpulan data warga yang sangat luas termasuk perilaku mobilitas, pola belanja, dan interaksi sosial. Perusahaan mengklaim data hanya akan digunakan untuk optimization services dan tidak akan dibagikan ke pihak manapun. Namun perusahaan tidak bisa menjamin 100% bahwa data tidak akan disadap oleh pihak ketiga. Masyarakat дает reaksi campur aduk.",
        "options": [
            "Terima предложение karena smart city adalah forward-thinking initiative dan privasi bisa disesuaikan dengan undang-undang perlindungan data pribadi yang baru",
            "Tolak karena privasi adalah hak asasi yang tidak bisa dikompromikan dengan janji manfaat ekonomi dari sektor swasta manapun",
            "Minta perusahaan: data anonymization yang strict sebelum meninggalkan perangkat daerah, kontrak yang secara hukum mengikat penggunaan data hanya untuk tujuan yang disepakati dengan severe penalties untuk pelanggaran, third-party audit regular, dan citizens right to access and delete their data, lalu baru terima dengan ketentuan tersebut, edukasi masyarakat tentang hak mereka",
            "Serahkan keputusan kepada masyarakat melalui voting publik karena data mereka yang dikumpulkan sehingga merekalah yang harus memutuskan",
            "Minta компании untuk mendemonstrasikan sistem terlebih dahulu pada dataset dummy tanpa data nyata warga sebelum keputusan final"
        ],
        "answer": "Minta perusahaan: data anonymization yang strict sebelum meninggalkan perangkat daerah, kontrak yang secara hukum mengikat penggunaan data hanya untuk tujuan yang disepakati dengan severe penalties untuk pelanggaran, third-party audit regular, dan citizens right to access and delete their data, lalu baru terima dengan ketentuan tersebut, edukasi masyarakat tentang hak mereka",
        "explanation": "Opsi C menunjukkan governance yang prudent dalam era digital. Anonymization, contractual binding, audit, dan citizen rights adalah four pillars of responsible data governance. Bukan blindly accept, bukan outright reject, bukan delegate to popular vote without proper information.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_025",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "Ваш институт baru saja mengadopsi sistem informasi baru setelah использования years Excel. Beberapa сотрудник старший mulai mengeluh bahwa sistem информационная terlalu lambat untuk dipelajari dan lebih suka menyimpan data di personal computer mereka karena they feel lebih memiliki kontrol. Anda memahami bahwa ada конфликт antara standardisasi dan fleksibilitas персонала. Namun Anda juga sadar bahwa data di personal computer adalah риск безопасности dan tidak ada backup jika komputer hilang atau rusak. Sistemas baru ainda belum stabil dan beberapa fungsi belum работают.",
        "options": [
            "Larang tegas seluruh karyawan menyimpan data di personal computer karena merupakan pelanggaran keamanan informasi dan terapkan sanksi к нарушителям",
            "Izinkan pengecualian dengan kondisi bahwa data yang disimpan di personal computer harus dienkripsi dan secara berkala di-backup ke server terpusat, sambil percepat perbaikan sistem informasi yang masih bermasalah",
            "Biarkan karyawan memilih sendiri mau pakai sistem baru atau Excel karena они lebih tahu apa yang terbaik untuk produktivitas mereka sendiri",
            "Buat hybrid: функционал yang belum tersedia di sistem baru tetap bisa menggunakan Excel temporarily dengan ketentuan data harus disubmit ke sistem dalam bentuk digital terstruktur yang bisa diimpor, sementara функционал baru yang sudah tersedia wajib menggunakan sistem baru",
            "Serahkan kepada departemen ИТ untuk memutuskan karena merekalah spesialis dalam вопросах keamanan informasi"
        ],
        "answer": "Buat hybrid: функционал yang belum tersedia di sistem baru tetap bisa menggunakan Excel temporarily dengan ketentuan data harus disubmit ke sistem dalam bentuk digital terstruktur yang bisa diimpor, sementara функционал baru yang sudah tersedia wajib menggunakan sistem baru",
        "explanation": "Opsi D menunjukkan pragmatisme implementasi yang mengakui bahwa sistem baru tidak sempurna. Hybrid approach dengan standards transisi adalah jalan realistis menuju adopsi penuh. Bukan kompromi keamanan total, bukan ignore legitimate kebutuhan staf.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_026",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "During аудит систем информационная, Anda menemukan bahwa seorang staf yang Anda percaya telah secara berulang kali melanggar SOP by sharing login credentials with colleague untuk mempercepat proses pelayanan karena sistem terlalu lambat. Kolega merasa tidak ada niat jahat karena tujuannya mempercepat служба гражданам. Namun sharing credentials adalah pelanggaran serius yang bisa membuka celah bagi akses tidak sah dan data breach. Кolega yang menerima credentials juga melanggar SOP.",
        "options": [
            "Berikan Teguran Tertulis kepada keduanya karena pelanggaran SOP adalah pelanggaran SOP tanpa pengecualian, namun sampaikan dengan empati bahwa sistem sedang dalam perbaikan dan скоро akan lebih cepat, serta jangan laporkan ke pihak berwajib karena tidak ada kerugian finansial yang terjadi",
            "Laporan ke полиция karena sharing credentials adalah cybercrime yang dapat dituntut secara hukum независимо от намерения, untuk membuat contoh deterrent bagi semua staff",
            "Analis konteks: mengapa credentials sharing terjadi karena sistem lambat atau karena kenyamanan? Jika sistem, percepat perbaikan. Jika niat, tegur. Tapi в любом случае edukasi tentang keamanan informasi perlu diberikan kepada semua staff sebelum menerapkan sanksi",
            "Serahkan tanggung jawab kepada atasan langsung karena pelanggaran terjadi di bawahan Anda dan Anda tidak mau terlibat dalam драма internal",
            "Diam saja karena tidak ada kerugian nyata yang terjadi dan menimbulkan konflik dengan персонал tidak worth it untuk administrasi"
        ],
        "answer": "Analis konteks: mengapa credentials sharing terjadi karena sistem lambat atau karena kenyamanan? Jika sistem, percepat perbaikan. Jika niat, tegur. Tapi в любом случае edukasi tentang keamanan informasi perlu diberikan kepada semua staff sebelum menerapkan sanksi",
        "explanation": "Opsi C menunjukkan respons yang proporsional dan bijaksana terhadap insiden keamanan. Root cause analysis penting karena kebijakan keamanan hanya efektif jika staff memahami alasan di baliknya. Education first, sanction as last resort.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_027",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "Anda ditugasi mengevaluasi efektivitas chatbot layanan publik yang baru запущен месяц lalu. Data показывает: 70% пользователей menyelesaikan masalah mereka melalui chatbot tanpa perlu escalate ke человеческий оператор, но 30% остальных merasa frustrasi dan beberapa bahkan марш social media抱怨 bahwa chatbot tidak bisa memahami masalah kompleks mereka. Kritikus internally mengatakan anggaran chatbot sebaiknya dialihkan ke manusia оператор. Сторонники же argue bahwa 70% успеха sudah baik.",
        "options": [
            "Hentikan программу chatbot karena 30% failure rate tidak bisa ditoleransi dalam служба publik критических",
            "Lanjutkan karena 70% успеха sudah lebih dari cukup dan tidak perlu investasi tambahan untuk memperbaiki 30%",
            "Lakukan analisis mendalam: kategorikan 30% yang gagal, apakah техническая (chatbot tidak bisa handle complex language), process-related (masalah memerlukan eskalasi karena di luar cakupan layanan), atau user-related (warga tidak familiar dengan teknologi). Untuk setiap kategori, разработкайте solusi spesifik: improve NLP for technical, expand scope untuk process-related, dan sediakan manusia оператор hotline untuk user-related. Lalu implement improvements iteratively.",
            "Pindahkan semua anggaran ke человеческий оператор karena они lebih efektif dan publik lebih suka услуги manusiawi",
            "Adakan public survey untuk menentukan apakah warga lebih suka chatbot atau manusia оператор"
        ],
        "answer": "Lakukan analisis mendalam: kategorikan 30% yang gagal, apakah техническая (chatbot tidak bisa handle complex language), process-related (masalah memerlukan eskalasi karena di luar cakupan layanan), atau user-related (warga tidak familiar dengan teknologi). Untuk setiap kategori, разработкайте solusi spesifik: improve NLP for technical, expand scope untuk process-related, dan sediakan manusia оператор hotline untuk user-related. Lalu implement improvements iteratively.",
        "explanation": "Opsi C menunjukkan pengambilan keputusan berbasis data tanpa bias ideologis. Pendekatan iterative based on categorized failure memungkinkan optimization bertahap yang realistic. Tidak menolak teknologi karena imperfection, tidak mempertahankan status quo karena angka好看.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_028",
        "category": "TKP",
        "subcategory": "TIK",
        "question": "Seorang programmer diinstansi Anda privately сообщает bahwa ia telah menemukan kerentanan keamanan kritis dalam sistem informasi daerah yang sedang digunakan untuk menyimpan data kependudukan hampir satu juta warga. Kerentanan memungkinkan unauthorized access к pribadi data. Namun programmer tersebut juga сообщает bahwa ia belum menyampaikan temuan kepada vendor sistem karena takut bahwa vendor akan dituntut atau akan ada masalah hukum bagi dirinya pribadi karena ia mungkin telah mengakses sistem di luar scope normal saat menemukannya.",
        "options": [
            "Minta programmer untuk diam karena pengungkapan kerentanan tanpa izin dapat menciptakan masalah hukum bagi pemerintah daerah dan vendor dalam konteks kontrak",
            "Лари ke полиция karena programmer admitted to accessing sistem dengan cara yang mungkin violate terms of service, sehingga bisa menjadi masalah криминальный",
            "Apresiasi programmer untuk etis whistleblowing, pastikan dia dilindungi oleh kebijakan perlindungan Whistleblower, lalu escalate findings kepada vendor melalui saluran resmi dengan крайним срок patching yang mendesak, dan notify instansi pengawas perlindungan data tentang insiden ini",
            "Abaikan karena tidak ada bukti bahwa kerentanan sudah dieksploitasi dan vendor mungkin sudah знает tentang masalah ini",
            "Serahkan sepenuhnya kepada programmer untuk memutuskan karena itu adalah инициатива его pribadi"
        ],
        "answer": "Apresiasi programmer untuk etis whistleblowing, pastikan dia dilindungi oleh kebijakan perlindungan Whistleblower, lalu escalate findings kepada vendor melalui saluran resmi dengan крайним срок patching yang mendesak, dan notify instansi pengawas perlindungan data tentang insiden ini",
        "explanation": "Opsi C menunjukkan governance yang bertanggung jawab atas insiden keamanan. Melindungi whistleblower adalah critical untuk budaya keamanan informasi. Escalation vendor melalui resmi channel memastikan akuntabilitas. Notify pengawas perlindungan data adalah требование regulasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_029",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda seorang pejabat yang menyusun keputusan bersama dengan rekan seprofesi tentang apakah mendukung реформу структура organization yang предложил oleh pemerintah pusat. Reformasi memiliki keunggulan potensial untuk meningkatkan efektivitas, namun juga berarti beberapa позиции manajerial saat ini akan dihapus termasuk beberapa должность gdzie pejabat saat ini adalah teman dekat Anda dan sudah bekerja sama selama bertahun-tahun. Keputusan akan дискусия besok. Hubungan Anda mempengaruhi позицию Anda.",
        "options": [
            "Suarakan untuk reformasi karena ini secara objektif lebih baik untuk organisasi meskipun berarti kehilangan teman dekat, karena profesionalisme harus выше дружеских обязательств",
            "Suarakan против karena teman-teman Anda telah mengorbankan banyak untuk organisasi dan Anda tidak ingin menjadi penyebab hilangnya должность mereka",
            "Lakukan analisis independen terhadap setiap позиции yang berpotensi dihapus: apakah fungsional (memang tidak diperlukan setelah reformasi) atau только политический (dihapus untuk efisiensi kekuasaan)? sampaikan temuan kepada teman dekat Anda dan bersama-sama найти альтернатива untuk mereka jika memang posisinya extraneous, независимо от suara Anda dalam pemungutan suara",
            "Abstain dari голосование karena konflik interest yang tidak bisa diatasi karena позиция Anda secara pribadi akan diintegrasikan dengan голосование Anda",
            "Bicara dengan atasan terlebih dahulu untuk mendapatkan kejelasan tentang apakah reformasi bisa dimodifikasi untuk сохранить beberapa должность критический"
        ],
        "answer": "Lakukan analisis independen terhadap setiap позиции yang berpotensi dihapus: apakah fungsional (memang tidak diperlukan setelah reformasi) или только политический (dihapus untuk efisiensi kekuasaan)? sampaikan temuan kepada teman dekat Anda dan bersama-sama найти альтернатива untuk mereka jika memang posisinya extraneous, независимо от suara Anda dalam pemungutan suara",
        "explanation": "Opsi C menunjukkan profesionalisme yang teguh: tidak pilih berdasarkan persahabatan, tidak pilih berdasarkan идеология saja, tidak abstain. Pendekatan analytically independent, справедливо terhadap teman, dan tetap fokus pada tujuan reformasi.",
        "difficulty": "hard"
    },
    # === PROFESIONALISME (8) ===
    {
        "id": "tkp3_030",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda mengelola proyek dengan anggaran besar dan banyak pemangku kepentingan. Saat прогресс достиг 60%, terungkap bahwa satu komponen kritis проекта menggunakan teknologi yang sudah usang dan vendor asli sudah tidak ada support. Jika melanjutkan dengan teknologi saat ini, proyek akan functionally obsolete dalam 2 tahun. Jika pivot ke teknologi baru, perlu anggaran tambahan dan waktu, yang akan menyebabkan pengulangan 20% pekerjaan. Tim proyek overwhelmingly反对 perubahan karena sudah invested месяцы и emotional attachment to their work.",
        "options": [
            "Требовать pivot immediately karena obsolete technology tidak bisa ditoleransi dalam proyek strategis meskipun tim反对 dan akan menyebabkan cost overrun",
            "Biarkan karena teknologi masih berfungsi dan 2 tahun adalah waktu yang cukup untuk depresiasi sebelum evaluasi следующий proyek",
            "Lakukan аудит технический independen untuk memvalidasi klaim tentang teknologi usang, jika valid, buat perbandingan cost-benefit antara continue dan pivot termasuk dampak terhadap timeline, stakeholder, dan kualitas produk, lalu sampaikan temuan solution yang terstruktur kepada tim dan stakeholders dengan transparan, termasuk kemungkinan solusi hybrid dimana transisi happens gradually",
            "Serahkan kepada tim karena they are ближе to technical reality dan Anda bukan teknisi",
            "Panggil semua stakeholder untuk vote pada keputusan karena semua akan terpengaruh"
        ],
        "answer": "Lakukan аудит технический independen untuk memvalidasi klaim tentang teknologi usang, jika valid, buat perbandingan cost-benefit antara continue dan pivot termasuk dampak terhadap timeline, stakeholder, dan kualitas produk, lalu sampaikan temuan solution yang terstruktur kepada tim dan stakeholders dengan transparan, termasuk kemungkinan solusi hybrid dimana transisi happens gradually",
        "explanation": "Opsi C menunjukkan kematangan dalam governance proyek. Tidak berdasarkan ego atau inertia, tapi bukti dan analisis. Validasi independen penting karena klaim teknis perlu diverifikasi sebelum keputusan besar. Transparan terhadap tim menunjukkan rasa hormat.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_031",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda seorang konsultan independen yang dikontrak untuk mengevaluasi kinerja sebuah SKPD yang sedang dalam proses reprofilamento руководства. Selama evaluasi, Anda menemukan bahwa beberapa данные kinerja yang disampaikan oleh руководитель current kepada atasannya are systematically overestimated. Namun Anda juga tahu bahwa target kinerja yang ditetapkan oleh atasannya sebelumnya adalah unreasonably high и tidak mungkin dicapai oleh unit manapun. Руководитель current menyadari hal ini и appears to have been inflating numbers untuk nampak seolah-olah kinerja memuaskan. Это создает dilemma profesional.",
        "options": [
            "Laporka apa adanya: data inflation adalah fraud dan harus dilaporkan regardless of context bahwa targetnya unreasonable",
            "Sampaikan kepada руководитель bahwa Anda tahu tentang inflation dan minta dia untuk memperbaiki data sebelum Anda submit final report, karena meskipun Anda sympathize dengan situasinya, Anda tidak bisa memvalidasi data yang tidak akurat",
            "Dalam laporan Anda, sebutkan kedua masalah: target yang unreasonable dan systematic data inflation, dan sarankan solusi dua langkah: pertama revisi target berdasarkan standar yang realistis, lalu audit data aktual terhadap target yang sudah direvisi",
            "Игнорируйте инфляцию данных karena она была реакцией на нереалистичные цели, установленные руководством, dan сосредоточьтесь только pada masalah sistemik sejak awal",
            "Откажитесь от участия dalam проекте karena Anda оказались dalam situasi konflik интересов"
        ],
        "answer": "Dalam laporan Anda, sebutkan kedua masalah: target yang unreasonable dan systematic data inflation, dan sarankan solusi dua langkah: pertama revisi target berdasarkan standar yang realistis, lalu audit data aktual terhadap target yang sudah direvisi",
        "explanation": "Opsi C menunjukkan integritas profesional yang kompleks. Dengan mengakui kedua masalah — unreasonable target dan dishonest response — laporan memberikan perbaikan sistemik yang holistic. Ini bukan cover-up tapi analisis yang adil terhadap semua pihak.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_032",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda seorang inspektorat daerah yang sedang melakukan проверка penggunaan anggaran bencana alam dari tahun lalu. На данных awal, Anda menemukan bahwa seorang pejabat menengah yang Anda personally kagumi karena dedikasinya terhadap masyarakat, telah menggunakan sebagian anggaran bencana untuk keperluan mendesak lainnya di saat situasi darurat. Secara formal это adalah pelanggaran penggunaan anggaran. Namun situasi darurat yang melatarbelakangi keputusan tersebut adalah nyata dan dia menghadapi tekanan dari warga yang membutuhkan bantuan.",
        "options": [
            "Laporka pelanggaran karena aturan anggaran bersifat tegas tanpa pengecualian dan profesionalisme memerlukan kepatuhan terhadap SOP even in emergencia situations",
            "Abaikan karena niat baik pejabat tersebut tidak salah dan situasinya действительно darurat, serta melaporkan akan merusak karier seseorang yang berdedikasi tinggi",
            "Rapikan dalam laporan bahwa telah terjadi deviasi dari SOP dengan konteks situasi, namun nyatakan bahwa pejabat telah bertindak dalam niat baik untuk memenuhi kebutuhan mendesak warga dan tidak ada bukti penyimpangan untuk keuntungan pribadi, serta sarankan pembuatan mekanisme kontinjensi untuk situasi darurat future agar pejabat tidak harus memilih antara melanggar aturan atau membiarkan warga menderita",
            "Переведите ответственность ke atas karena Anda tidak ingin menentang keputusan emergency yang diambil pejabat senior meskipun Anda tahu itu melanggar rules",
            "Tutup karena anggaran bencana bersifat sensitif dan laporan publik akan menimbulkan panic tentang penggunaan anggaran darurat"
        ],
        "answer": "Rapikan dalam laporan bahwa telah terjadi deviasi dari SOP dengan konteks situasi, namun nyatakan bahwa pejabat telah bertindak dalam niat baik untuk memenuhi kebutuhan mendesak warga dan tidak ada bukti penyimpangan untuk keuntungan pribadi, serta sarankan pembuatan mekanisme kontinjensi untuk situasi darurat future agar pejabat tidak harus memilih antara melanggar aturan atau membiarkan warga menderita",
        "explanation": "Opsi C menunjukkan integritas yang sophisticated. Laporan yang jujur dengan konteks memungkinkan learning dari pengalaman dan perbaikan sistemik. Suggesti mekanisme kontinjensi mencegah recurrence tanpa memarahi orangnya.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_033",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda diminta memberikan рекомендация kepada kepala daerah tentang реструктуризация персонала yang akan affecting 50 работник kontrak. Data menunjukkan bahwa sebagian besar работник kontrak memiliki kinerja di bawah standar, namun ada juga sebagian kecil yang performanya sangat baik dan sulit direkrut ulang jika di-PHK. Secara bersamaan, serikat pekerja угрожает akan demo besar jika pemotongan рабочих мест affecting работник yang sudah lama mengabdi meskipun kinerjanya rendah.",
        "options": [
            "Рекомендуйте phk semua работник kontrak tanpa pengecualian karena standar kinerja harus ditegakkan tanpa kompromi, demo adalah risiko yang harus ditanggung sebagai bagian dari реструктуризация yang perlu",
            "Pertahankan semua работник karena mempertahankan employment adalah prioritas sosial dan demo serikat akan mendestabilisasi organisasi",
            "Lakukan analisis bertingkat: untuk posisi yang membutuhkan kinerja tinggi dimana Anda tidak bisa berkompromi, dan untuk posisi yang bisa Anda berikan pelatihan dan masa transisi sebelum keputusan final. Untuk работник dengan kinerja sangat baik tapi di posisi yang tidak kritis, pertimbangkan retensi atau relokasi. Untuk yang di bawah standar dan tidak bisa ditraining, proseslah sesuai mekanisme yang tersedia. Komunikasikan secara transparan dengan serikat tentang standar yang Anda terapkan.",
            "Berikan semua работник kontrak opsi untuk переподготовка into posisi baru yang lebih relevan dengan kebutuhan organisasi modernisation",
            "Serahkan kepada кадровый отдел untuk membuat матрица kinerja tanpa melibatkan Anda secara pribadi dalam решение yang akan непопулярно"
        ],
        "answer": "Lakukan analisis bertingkat: untuk posisi yang membutuhkan kinerja tinggi dimana Anda tidak bisa berkompromi, dan untuk posisi yang bisa Anda berikan pelatihan dan masa transisi sebelum keputusan final. Untuk работник dengan kinerja sangat baik tapi di posisi yang tidak kritis, pertimbangkan retensi atau relokasi. Untuk yang di bawah standar dan tidak bisa ditraining, proseslah sesuai mekanisme yang tersedia. Komunikasikan secara transparan dengan serikat tentang standar yang Anda terapkan.",
        "explanation": "Opsi C menunjukkan HR management yang berprinsip tapi humana. Pendekatan differentiated terhadap workforce mencerminkan realitas kompleksitas organisasi. Transparansi dengan serikat membangun dialog daripada konfrontasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_034",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda seorang архитектор kebijakan publik yang dalam proses penyusunan стандарт pelayanan для служба yang akan diterapkan di seluruh daerah Anda. Eksperimen menemukan bahwa meskipun стандарт telah ditetapkan berdasarkan best practice, implementasi lapangan membutuhkan penyesuaian yang berbeda untuk konteks perkotaan dan сельский. Anda harus menentukan bagaimana стандарты harus diterapkan où ada kekhawatiran bahwa terlalu fleksibel akan menciptakan ketidakadilan layanan antar daerah.",
        "options": [
            "Terapkan standar yang sama untuk semua daerah tanpa pengecualian karena ketidakadilan layanan bisa terjadi jika standar terlalu berbeda antar daerah, uniformitas adalah kunci keadilan",
            "Izinkan setiap daerah untuk определять sendiri apa yang terbaik untuk konteks lokal mereka karena mereka lebih memahami kondisi lapangan",
            "Buat kerangka kerja dimana элементы центрльные (waktu承诺, informasi yang harus disediakan, mekanisme pengaduan) adalah wajib dan tidak bisa divariasikan, sementara элементы поддерживающие (metode delivery, каналы layanan) bisa disesuaikan dengan konteks lokal dengan catatan harus mendapat persetujuan dari tingkat daerah dan wajib memenuhi stand-alone критический metrics. Lakukan мониторинг ketat dengan независимый evaluator untuk memastikan variasi tidak menjadi逃避 dari standar minimum.",
            "Serahkan kepada депутаты weil они mewakili rakyat dan akan lebih tahu apa yang rakyat butuhkan",
            "Lakukan satu пилотный проект di beberapa daerah sebelum menentukan apakah fleksibilitas atau rigidity adalah pendekatan yang lebih baik"
        ],
        "answer": "Buat kerangka kerja dimana элементы центрльные (waktu承诺, informasi yang harus disediakan, mekanisme pengaduan) adalah wajib dan tidak bisa divariasikan, sementara элементы поддерживающие (metode delivery, каналы layanan) bisa disesuaikan dengan konteks lokal dengan catatan harus mendapat persetujuan dari tingkat daerah dan wajib memenuhi stand-alone критический metrics. Lakukan мониторинг ketat dengan независимый evaluator untuk memastikan variasi tidak menjadi逃避 dari standar minimum.",
        "explanation": "Opsi C menunjukkan regulatory design thinking yang sophisticated. Membedakan antara core standards yang harus sama everywhere untuk equity dan implementation flexibility yang memungkinkan local adaptation. Independent monitoring memastikan compliance tidak erode over time.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_035",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda menjadi saksi bahwa rekan kerja yang sedang mengalami kesulitan keluarga karena anaknya sakit kritis, telah secara berulang menggunakan номер вашего kartu credit untuk покупки keperluan pribadi anaknya di rumah sakit dengan alasan bahwa Anda memiliki hubungan dengan компания медицинская страховая dan bisa klaim возмещение later. Rekan Anda percaya bahwa hal ini tidak akan merepotkan Anda. Secara formal, это adalah penggunaan data третьих лиц tanpa izin dan bisa merupakan fraud.",
        "options": [
            "Report karena penyalahgunaan kartu credit adalah pelanggaran hukum dan meskipun niat baik, Anda tidak bisa mengabaikan преступления karena akan создать прецедент untuk perilaku sejenis",
            "Biarkan karena niat baik dan situasi yang tidak mungkin, dan tidak ada kerugian nyata bagi Anda karena bisa diklaim",
            "Bicara baik-baik dengan rekan, sampaikan bahwa Anda mengerti situasinya dan akan membantunya secara langsung dengan cara yang benar (membantu secara finansial atau membantu proses klaim asuransi yang proper), dan tegaskan bahwa penggunaan kartu third party tanpa izin tidak bisa ditoleransi even dalam situasi apapun karena ini menyangkut prinsip trust yang fundamental, namun tanpa melaporkan ke pihak berwenang karena Anda percaya niat baik dari rekan",
            "Mandatkan rekan untuk mengembalikan semua dana yang sudah digunakan dalam waktu tertentu, dan jika tidak bisa, baru laporan keatasan",
            "Diskusikan dengan keluarga partner Anda tentang apakah Anda nyaman dengan situasi ini karena это adalah keputusan pribadi yang akan mempengaruhi Anda dan keluarga"
        ],
        "answer": "Bicara baik-baik dengan rekan, sampaikan bahwa Anda mengerti situasinya dan akan membantunya secara langsung dengan cara yang benar (membantu secara finansial atau membantu proses klaim asuransi yang proper), dan tegaskan bahwa penggunaan kartu third party tanpa izin tidak bisa ditoleransi even dalam situasi apapun karena ini menyangkut prinsip trust yang fundamental, namun tanpa melaporkan ke pihak berwenang karena Anda percaya niat baik dari rekan",
        "explanation": "Opsi C menunjukkan integritas yang humanist. Approach ini mengambil tanggung jawab personal untuk membantu tanpa memvalidasi metode yang salah. Klarifikasi bahwa penggunaan tanpa izin tidak bisa diterima même in extremis menjaga prinsip integritas yang tidak подлежит обсуждению.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_036",
        "category": "TKP",
        "subcategory": "Profesionalisme",
        "question": "Anda seorang аудитор кадровый yang diminta untuk mengevaluasi apakah departemen yang dipimpin oleh seseorang yang akan pensiun soon perlu direstrukturisasi atau tidak. Jika restructure, banyak должности в departemen tersebut mungkin akan dihapus, affecting staff yang telah bekerja di sana untuk десять лет. Jika tidak restructure, departemen akan tetap неэффективный dan anggaran akan continue terbuang. Также, jika restructure, возможно Anda akan ditawari posisi baru dalam struktur yang baru karena Anda dianggap kompetен." ,
        "options": [
            "Реструктуризировать karena эффективность организации является lebih penting dari pada individual kepentingan работников, dan ini tidak terkait dengan потенциальная выгода для Anda pribadi",
            "Не реструктуризировать karena это справедливо terhadap работников yang telah loyally bekerja selama decade, dan Anda tidak mau bertanggung jawab atas увольнения",
            "Lakukan audit objectif yang independen tanpa pengaruh dari kemungkinan manfaat atau kerugian bagi Anda secara pribadi, ukur produktivitas, efisiensi, dan kelayakan departemen terhadap standar organisasi sejenis, buat rekomendasi based только pada data dan analisis, nyatakan secara transparan bahwa Anda memiliki potential conflict of interest и已经从 recursive tersebut untuk menjaga integritas proses, dan minta pihak independen untuk memvalidasi temuan Anda sebelum rekomendasi final disampaikan kepada pengambil keputusan",
            "Уклониться от задачи karena konflik интересов yang jelas dan tidak bisa dihindari",
            "Lakukan audit tapi hasilnya akan bergantung pada apakah restructure akan memberi Anda posisi yang lebih baik atau tidak"
        ],
        "answer": "Lakukan audit objectif yang independen tanpa pengaruh dari kemungkinan manfaat atau kerugian bagi Anda secara pribadi, ukur produktivitas, efisiensi, dan kelayakan departemen terhadap standar organisasi sejenis, buat rekomendasi based только pada data dan analisis, nyatakan secara transparan bahwa Anda memiliki potential conflict of interest и已经从 recursive tersebut untuk menjaga integritas proses, dan minta pihak independen untuk memvalidasi temuan Anda sebelum rekomendasi final disampaikan kepada pengambil keputusan",
        "explanation": "Opsi C menunjukkan pendekatan profesional terhadap conflict of interest. Declaration of interest secara proaktif adalah standar profesional yang diakui. Validation independen menambah kredibilitas temuan. Rekomendasi berdasarkan чисто pada data melindungi Anda dari kedua arah.",
        "difficulty": "hard"
    },
    # === INTEGRITAS DIRI (7) ===
    {
        "id": "tkp3_037",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang pejabat tinggi yang telah lama mengidap penyakit kronis yang memerlukan pengobatan rutin dengan biaya очень besar melebihi kemampuan finansial. Perusahaan асикуранси где Anda adalah nasal соискатель tanpa sengaja mencantumkan diri sebagai держатель polis асикуранси жизни где премии ditanggung perusahaan dan полис bisa digunakan untuk pengobatan termasuk penyakit pre-existing. Anda mengetahui bahwa ini technical tidak sesuai dengan syarat полис namun jika tidak menggunakan, Anda mungkin tidak bisa mendapatkan pengobatan yang diperlukan. Situasi ini terjadi tahun lalu dan Anda sekarang memiliki cukup uang dari реимбурс for pengobatan Anda.",
        "options": [
            "Биkeep it as your secret karena компания asuransi tidak akan pernah tahu dan tidak ada kerugian bagi siapapun karena премия sudah dibayar oleh perusahaan",
            "Анонisi perusahaan dan minta clarify apakah полис bisa digunakan untuk kondisi Anda karena Anda memerlukan clarity untuk kesehatan Anda ke depan",
            "Segera возвращать uang yang sudah diklaim dari асикуранси kepada perusahaan karena ini adalah penggunaan dana yang tidak sesuai untuk tujuan mereka, сообщите juga kepada компания асикуранси tentang ситуации untuk mencegah mereka dari terus менять polis yang tidak sesuai, dan konsultasikan dengan компания асикуранси Anda untuk menemukan альтернатива financing yang tepat untuk kondisi Anda ke depan, meskipun ini berarti Anda harus membayar dari pocket значительно lebih banyak",
            "Игнорируйте и продолжайте использовать karena Anda membutuhkannya dan tidak ada yang bisa Anda lakukan tentang itu",
            "Отказ отсрочки karena Anda sudah klaim dan tidak ada механизм untuk возврата yang sudah disbursed"
        ],
        "answer": "Segera возвращать uang yang sudah diklaim dari асикуранси kepada perusahaan karena ini adalah penggunaan dana yang tidak sesuai untuk tujuan mereka, сообщите juga kepada компания асикуранси tentang ситуации untuk mencegah mereka dari terus менять polis yang tidak sesuai, dan konsultasikan dengan компания асикуранси Anda untuk menemukan альтернатива financing yang tepat untuk kondisi Anda ke depan, meskipun ini berarti Anda harus membayar dari pocket значительно lebih banyak",
        "explanation": "Opsi C menunjukkan integritas yang teruji. Pengembalian dana yang tidak sesuai adalah konsekuensi natural dari penggunaan yang salah. Notification kepada asuransi melindungi mereka dari future claims yang tidak sesuai. Pencarian alternative financing yang mungkin lebih mahal menunjukkan Anda готов платить за целостность.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_038",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang inspektur yang sedang melakukan проверка на месте terhadap proyek pembangunan sekolah di daerah terpencil. Подрядчик secara pribadi mendekati Anda di akhir hari kerja dan menjelaskan bahwa проверка завтра akan menemukan beberapa несоответствия небольшой because материал yang digunakan memiliki спецификации di bawah standar karena masalah rantai pasok. Kontraktor tersebut adalah teman masa kecil Anda. Dia also hints bahwa ada beberapa teman bersama yang mungkin akan звонок Anda untuk membicarakan ini.",
        "options": [
            "Lanjutkan проверка как запланировано dan laporkan semua ketidaksesuaian sesuai temuan karena apapun alasan, standar harus ditegakkan",
            "Отложить проверка karena Anda telah menerima предупреждение dan mungkin ada консекуэнсия tidak menyenangkan dari teman-teman jika Anda tidak mengikuti социальные нормы about this situation",
            "Проведите проверка как запланировано dan jika menemukan ketidaksesuaian, dokumentasikan dengan фото dan видео sebagai bukti, namun sampaikan kepada kontraktor terlebih dahulu bahwa Anda tahu tentang aproximра approaching warning dan bahwa Anda akan bertindak sesuai temuan tanpa takut atau mengistimewakan siapapun kepada teman masa kecil atau tekanan sosial, namun tetap profesional dengan memberinya waktu untuk menjelaskan konteks sebelum решения final",
            "Требуйте dari kontraktor kontrak дополнительные penjelasan sebelum проверка начинается karena Anda menghormati old friend dan ingin memberikan справедливости tanpa favoritisme",
            "Batalkan проверка karena tekanan sosial dari teman-teman terlalu besar dan Anda takut kehilangan друзей"
        ],
        "answer": "Проведите проверка как запланировано dan jika menemukan ketidaksesuaian, dokumentasikan dengan фото dan видео sebagai bukti, namun sampaikan kepada kontraktor terlebih dahulu bahwa Anda tahu tentang aproximра approaching warning dan bahwa Anda akan bertindak sesuai temuan tanpa takut atau mengistimewakan siapapun kepada teman masa kecil atau tekanan sosial, namun tetap profesional dengan memberinya waktu untuk menjelaskan konteks sebelum решения final",
        "explanation": "Opsi C menunjukkan integritas yang tidak dikompromikan oleh hubungan pribadi atau tekanan sosial. Pemberitahuan proaktif kepada kontraktor bahwa Anda sudah dinasihati menunjukkan bahwa upaya mempengaruhi sudah gagal bahkan sebelum dimulai.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_039",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang kepala SKPD yang selama tiga tahun telah membangun sistem yang sangat tertipis dan dipercaya oleh masyarakat berdasarkan integritas Anda yang tidak pernah menerima suap atau комаisi dari siapapun. Sekarang, saat Anda akan meninggalkan posisi untuk promosi ke posisi yang lebih tinggi, ada tekanan dari beberapa kolega давать Anda instruksi что Anda harus menominasikan replacement yang akan Anda percaya untuk menjaga integritas системы. Replacement yang Anda percaya secara moral adalah seseorang yang tidak populer di среди руководства karena sering ментор kritis terhadap praktik Manajemen saat ini. Nominate mereka berarti Anda mungkin может потерять beberapa поддержки from current leadership for your future career.",
        "options": [
            "Номинируйте someone who does not share your values tapi populer di руководства karena itu akan lebih baik untuk карьеры Anda ke depan, dan organisasi akan tetap функционировать karena системный уже установлен",
            "Номинируйте someone yang menurut Anda memiliki integritas sama dengan Anda karena Anda tidak bisa berkompromi dengan prinsip yang telah Anda bangun selama tiga tahun demi profit карьерный Anda sendiri",
            "Если Anda ingin nominate seseorang berdasarkan принцип, сделайте ini transparan dengan menunjukkan kepada руководства kenapa Anda memilih orang ini karena track record integritas dan komitmen terhadap anti-korupsi, dan jika руководство tidak menyetujuinya, Anda harus memutuskan apakah akan mengubah nominasi atau mempertahankan prinsip и принять риск карьерный. Это может berarti Anda tidak akan maju, tapi Anda не будете жить с компромиссом этики.",
            "Номинация berdasarkan siapa yang paling loyal kepada Anda karena они akan menjaga legacy Anda и это lebih penting dari semua pertimbangan lain",
            "Безразлично siapa di номинаasikan karena Anda tidak akan быть там untuk melihat apa yang terjadi anyway"
        ],
        "answer": "Jika Anda ingin nominate seseorang berdasarkan принцип, сделайте ini transparan dengan menunjukkan kepada руководства kenapa Anda memilih orang ini karena track record integritas dan komitmen terhadap anti-korupsi, dan jika руководство tidak menyetujuinya, Anda harus memutuskan apakah akan mengubah nominasi atau mempertahankan prinsip и принять риск карьерный. Это может berarti Anda tidak akan maju, tapi Anda не будете жить с компромиссом этики.",
        "explanation": "Opsi C menunjukkan karakter yang teruji. Transparansi dengan alasan yang jelas memberikan руководства kesempatan untuk memahami. Risiko карьерный yang ditanggung menunjukkan bahwa integritas имеет свою цену. Это принципиальный pragmatism.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_040",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang руководитель proyek yang telah dikontrak untuk mengelola pembangunan infrastruktur критический untuk masyarakat. Minggu lalu, подрядчик memberikan Anda amplop berisi jumlah uang yang cukup besar dengan penjelasan bahwa ini adalah年末 bonus dari компания yang Anda tidak pernah tahu existed as bagian dari organizational structure mereka. Anda belum membuka karena situasi terasa tidak benar. Hari ini, kontraktor yang sama remind Anda bahwa banyak perusahaan lain menggunakan практика ini as standard.",
        "options": [
            "Вернуть amplop dengan penjelasan bahwa Anda tidak bisa menerima hadiah yang dapat mempengaruhi беспристрастность Anda sebagai руководитель проекта критический",
            "Принять karena semua компании делают это и это действительно практика bisnis normal в некоторых отраслях, особенно в конце года",
            "Сохраните пока Anda tidak menyelesaikan проверку: jika uang berasal dari sumber yang sah и digunakan untuk tujuan yang tidak bertentangan dengan позиция Anda, Anda bisa возвращать; namun jika menimbulkan masalah, возвращать; ini обеспечивает гибкость и защиту Anda",
            "Jangan membuka amplop dan pura-pura tidak tahu, karena Anda tidak ingin terlibat dalam situasi yang tidak menyenangkan apapun keputusannya",
            "Buka amplop dan hitung isinya, jika nominalnya kecil terima tapi jika besar kembalikan"
        ],
        "answer": "Вернуть amplop dengan penjelasan bahwa Anda tidak bisa menerima hadiah yang dapat mempengaruhi беспристрастность Anda sebagai руководитель проекта критический",
        "explanation": "Opsi A menunjukkan integritas yang konsisten. Prinsip anti-korupsi tidak memiliki grey area: bahkan kecil, mesmo年末 bonus, mesmo banyak orang melakukannya adalah mekanisme sistematis untuk membeli pengaruh. Consistency adalah kunci integritas.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_041",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang pengawas internal yang telah memberikan рекомендации keras terhadap praktik manajemen sebuah SKPD tempat Anda sebelumnya bekerja. SKPD tersebut sekarang dalam proses реструктуризация yang hasilnya akan decided by atasan Anda pada minggu depan. Если реструктуризация berjalan sesuai temuan Anda, beberapa manajer in SKPD tersebut, termasuk seseorang yang помогал вам berkembang dalam карьере, akan kehilangan должность. Secara pribadi Anda tahu bahwa这些人 tidak bersalah secara kriminal tapi telah menciptakan budaya organisasi yang tidak sehat yang годами damaging institution.",
        "options": [
            "Укрепите позицию Anda dengan menunjukkan bahwa integritas Anda sebagai pengawas akan selalu tegak независимо от apakah Anda kehilangan teman atau potential sponsors карьерный, karena Anda tidak bisa menjadi эффективный pengawas jika Anda mulai memetik whom you are supposed to oversee",
            "Мягко переформулируйте temuan Anda dalam lebih мягкий язык yang tidak требует увольнения manajer karena Anda tidak mau menjadi bertanggung jawab atas hilangnya должность untuk teman-teman baik Anda",
            "Оставьте свою рекомендацию tanpa изменение karena temuan sudah didokumentasikan dengan bukti dan это akan lebih baik untuk kesehatan jangka panjang organisasi untuk membersihkannya dari budaya yang tidak sehat даже если это berarti kehilangan teman baik",
            "Предложите план переподготовки или раннего выхода на пенсию вместо увольнения, чтобы дать manajer выход yang спасает их достоинство, sambil tetap membersihkan организационную культуру",
            "Откажитесь от участия dalam proses реструктуризации ini karena личные конфликты yang telah dibuat"
        ],
        "answer": "Оставьте свою рекомендацию without изменение karena temuan sudah didokumentasikan dengan bukti dan это akan lebih baik для долгосрочного здоровья организации untuk membersihkannya dari budaya yang tidak sehat даже jika это berarti kehilangan teman baik",
        "explanation": "Opsi C menunjukkan profesionalisme yang mature. Your job as pengawas adalah memberikan objective findings. Bagaimana organisasi merespons adalah keputusan mereka. Anda tidak memiliki kontrol atas konsekuensi, hanya atas akurasi dan integritas proses.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_042",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda mengetahui bahwa seseorang dari teman dekat Anda telah menggunakan dokumen palsu untuk mendapatkan льгота yang ditujukan untuk keluarga miskin. Teman tidak mengetahui tentang связь Anda dengan правительственное учреждение которое обрабатывает dokumen ini. Ketika teman menemukan tentang позиция Anda, dia meminta Anda использовать влияние Anda untuk menyembunyikan дело или setidaknya дать ему waktu untuk найти решение. Teman угрожает, bahwa jika Anda tidak akan помогите, это может повредить дружбе, dan dia будет рассказывать всем, что Anda tidak mau помогать в критический момент.",
        "options": [
            "Свяжитесь с расследования отделом самостоятельно dan сообщите о dokumen palsu другом, даже если ini berarti потеря дружбы и последствия для друга, karena jika Anda tidak melapor, Anda menjadi участник мошенничества",
            "Используйте влияние Anda untuk отложить расследование dan дать другу waktu untuk найти решение, karena дружба важнее dari pada pelanggaran dokumen, dan Anda bisa memperbaiki ini позже",
            "Откровенно поговорите dengan другому tentang seriusnya ситуации, объясните, что покрытие ini akan нарушать вашу профессиональную этику, dan настоятельно рекомендуйте ему добровольно сознаться dan memperbaiki документы, предложив помочь найти юридическую поддержку, dan дать время untuk memikirkannya, tapi jelaskan bahwa jika dia tidak сознается добровольно, Anda akan обязаны сообщить об этом согласно вашим профессиональным обязательствам, и это решение должно быть его собственный, а не ваш",
            "Притворитесь, что Anda tidak tahu tentang этом деле, karena это может быть решением antara друга dan pemerintah, dan Anda не хотите вмешиваться",
            "Предложите деньги untuk membantu другому получить legal advice, dan попросите его не втягивать вас dalam это дело"
        ],
        "answer": "Откровенно поговорите dengan другому tentang seriusnya ситуации, объясните, что покрытие ini akan нарушать вашу профессиональную этику, dan настоятельно рекомендуйте ему добровольно сознаться dan memperbaiki документы, предложив помочь найти юридическую поддержку, dan дать waktu untuk memikirkannya, tapi jelaskan bahwa jika dia tidak сознается добровольно, Anda akan обязаны сообщить об этом согласно вашим профессиональным обязательствам, dan это решение должно быть его собственный, а не ваш",
        "explanation": "Opsi C menunjukkan keseimbangan yang sophisticated antara loyalty personal dan integritas profesional. Dengan berbicara langsung, Anda memberikan teman kesempatan untuk membuat keputusan yang benar tanpa ditekan dari posisi otoritas. Pemberian ultimatum yang jelas adalah batas yang tegas tapi adil.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_043",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang специалист кадровый и dalam proses rekrutmen terbuka untuk formasi cpns daerah, Anda menemukan bahwa beberapa pelamar memiliki nilai тест yang sangat tinggi tapi memiliki celah dalam interview mereka которые указывают bahwa mereka mungkin telah mendapatkan akses к вопросам теста sebelum waktu due to unknown leak. Namun Anda tidak bisa membuktikan karena pola tersebut bisa juga просто berarti mereka memang berbakat. При этом, Anda juga menemukan bahwa beberapa pelamar dari daerah terpencil dengan nilai тест sedikit lebih rendah tapi dengan motivasi yang sangat jelas dan рекомендации письма yang genuinely compelling menunjukkan potensi jangka panjang yang lebih tinggi.",
        "options": [
            "Квалифицируйте всех pelamar berdasarkan nilai тест kuantitas karena тест adalah ukur yang objektif dan tidak bisa disangkal, dan interview terlalu субъективно untuk dijadikan dasar keputusan",
            "Ambillah keputusan berdasarkan pertimbangan komprehensif dari nilai тест, interview, рекомендации, и potensi jangka panjang, dengan transparan menjelaskan kepada committee bahwa ada kekhawatiran tentang potential тест leak и bahwa meskipun tidak ada bukti konklusif, Anda propose additional interview round untuk pelamar yang mencurigakan agar mereka memiliki kesempatan untuk mendemonstrasikan kemampuan secara nyata, sambil tetap memberikan bobot pada pelamar dari daerah terpencil yang memiliki motivasi jelas и potensi pengembangan jangka panjang yang lebih baik untuk институт building daerah",
            "Disqualified pelamar yang Anda curigai telah melihat bank вопросов karena integritas proses lebih важно dari pada siapa yang punya nilai tertinggi",
            "Ambil semua pelamar tanpa selection karena Anda не хотите принимать решение дискриминационное berdasarkan kecurigaan tanpa bukti",
            "Laporkan ke полиция tentang kemungkinan kebocoran тест karena это adalah угроза integrity отбора кадров государственный"
        ],
        "answer": "Ambillah keputusan berdasarkan pertimbangan komprehensif dari nilai тест, interview, рекомендации, и potensi jangka panjang, dengan transparan menjelaskan kepada committee bahwa ada kekhawatiran tentang potential тест leak и bahwa meskipun tidak ada bukti konklusif, Anda propose additional interview round untuk pelamar yang mencurigakan agar mereka memiliki kesempatan untuk mendemonstrasikan kemampuan secara nyata, sambil tetap memberikan bobot pada pelamar dari daerah terpencil yang memiliki motivasi jelas и potensi pengembangan jangka panjang yang lebih baik untuk институт building daerah",
        "explanation": "Opsi B menunjukkan pengambilan keputusan yang bernuansa di area grey. Ronda interview tambahan adalah solusi cerdas yang memberikan fairness kepada yang mencurigakan tanpa mengorbankan yang berbakat, sambil menjaga integritas proses.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_044",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda seorang медиа official pemerintah и dalam perjalanan resmi ke daerah lain, Anda menyaksikan bagaimana sebuah perusahaan yang baru saja memenangkan тендер dari daerah Anda telah secara terbuka memberikan взятка kepada pejabat daerah yang Anda kenal, di depan mata Anda. Anda mengenal keduanya: perusahaan tersebut telah дискредитировать Anda dalam media previously karena Anda pernah mengkritisi mereka, dan pejabat daerah tersebut adalah teman baik Anda который telah поддерживал Anda through difficult times. Никто tidak ada yang tahu bahwa Anda menyaksikan此事. Even если Anda melapor, hampir tidak mungkin untuk dibuktikan karena tidak ada bukti dokumenter.",
        "options": [
            "Melapor karena integritas Anda sebagai pejabat public tidak bisa dikompромисkan regardless of siapa yang involved или bagaimana hubungan personal Anda dengan keduanya, karena jika Anda tidak melapor, Anda menjadi bagian dari rantai korupsi yang Anda критиковали secara publik",
            "Diam saja karena hampir tidak mungkin untuk dibuktikan и akan lebih banyak вреда bagi Anda secara pribadi untuk terlibat dalam perselisihan dengan dua orang yang berpengaruh tanpa bukti yang cukup, especially когда salah satu dari mereka adalah teman baik Anda",
            "Bicara secara personal dengan masing-masing: kepada pejabat daerah, jelaskan bahwa Anda tahu dan bahwa Anda perlu dia untuk mundur atau mengklarifikasi; kepada perusahaan, sampaikan bahwa jika mereka tidak mengklarifikasi, Anda akan melapor karena mereka telah mendiskreditkan Anda sebelumnya dan sekarang memberi Anda leverage untuk bertindak tanpa harus merasa como pengkhianat друзей",
            "Abaikan sepenuhnya karena Anda tidak memiliki cukup informasi atau wewenang untuk menangani situasi ini и Anda tidak terlibat dalam тендер process данный",
            "Дать waktu untuk melihat apakah ada повторяющаяся pattern yang bisa Anda dokumentasikan untuk membangun case yang lebih kuat sebelum melapor dengan bukti yang lebih substansiel"
        ],
        "answer": "Bicara secara personal dengan masing-masing: kepada pejabat daerah, jelaskan bahwa Anda tahu dan bahwa Anda perlu dia untuk mundur atau mengklarifikasi; kepada perusahaan, sampaikan bahwa jika mereka tidak mengklarifikasi, Anda akan melapor karena mereka telah mendiskreditkan Anda sebelumnya dan sekarang memberi Anda leverage untuk bertindak tanpa harus merasa como pengkhianat друзей",
        "explanation": "Opsi C menunjukkan integritas strategis. Pemberian umpan balik langsung tanpa угрожать adalah profesional dan memberikan kesempatan untuk perbaikan sebelum eskalasi. Leverage dari diskredit sebelumnya membuat pendekatan ini tidak feel like pengkhязatif tapi seperti fair play.",
        "difficulty": "hard"
    },
    {
        "id": "tkp3_045",
        "category": "TKP",
        "subcategory": "Integritas Diri",
        "question": "Anda профессионал dengan reputasi tinggi yang dikontrak pemerintah untuk mengevaluasi потенциальный партнер dalam государственно-частное партнерство bernilai miliar. В процессе evaluacji ditemukan bahwa компания-партнер memiliki sejarah seriusных нарушений экологии и прав человека в других странах, tapi belum di Indonesia dimana они еще belum bekerja. Anda harus memutuskan apakah включить informasi ini dalam laporan meskipun secara teknis mereka tidak нарушали indonesian law, atau diskreditkan потенциально berguna партнерство bernilai miliar для общественности.",
        "options": [
            "Включите всю историю компании lengkap dalam laporan karena компания telah menunjukkan паттерн поведения yang tidak sesuai dengan nilai-nilai прав человека dan lingkungan, dan ini является relevant для принятия решений, даже jika они tidak нарушали indonesian law specifically",
            "Tidak masukkan informasi ini karena secara teknis компания tidak melanggar hukum di Indonesia, dan Anda tidak boleh menjadi hakim untuk поведения экстра-территориальный, ini будет за пределами ваших полномочий",
            "Включите semua informasi secara transparan dalam laporan, dengan jelas menunjukkan bahwa ini adalah нарушения экстра-территориальные dan bukan pelanggaran hukum Indonesia secara spesifik, namun nyatakan bahwa pola-pola ini relevan untuk оценка рисков jangka panjang компании dan bisa mempengaruhi reputasi государственно-частного партнерства ke depan, serta рекомендуйте bahwa Правительство harus membuat kebijakan yang требуют due diligence terhadap lingkungan dan hak asasi manusia secara universal untuk партнеров masa depan",
            "Включите всю информацию tapi сформулируйте ini secara ambigu sehingga tidak terlalu jelas negatif terhadap компании, tapi juga memenuhi вашу этическую обязательства untuk transparansi",
            "Переложить ответственность pada правительство karena они sudah memiliki akses к информации melalui другие каналы, dan Anda hanya советник"
        ],
        "answer": "Включите semua informasi secara transparan dalam laporan, dengan jelas menunjukkan bahwa ini adalah нарушения экстра-территориальные dan bukan pelanggaran hukum Indonesia secara spesifik, namun nyatakan bahwa pola-pola ini relevan untuk оценка рисков jangka panjang компании dan bisa mempengaruhi reputasi государственно-частного партнерства ke depan, serta рекомендуйте bahwa Правительство harus membuat kebijakan yang требуют due diligence terhadap lingkungan dan hak asasi manusia secara universal untuk партнеров masa depan",
        "explanation": "Opsi C menunjukkan integritas yang sophisticated dalam dunia yangglobalized. Pendekatan ini transparan tapi fair: perusahaan tidak bisa dihukum untuk violations di luar jurisdiction tapi informasi tersebut still relevant untuk risk assessment. Рекомендация untuk kebijakan universal menunjukkan bahwa Anda tidak targeting компания ini specifically tapi menetapkan standar untuk semua.",
        "difficulty": "hard"
    }
]

# Verify JSON structure
for i, q in enumerate(questions):
    assert 'id' in q, f"Q{i+1} missing id"
    assert 'question' in q, f"Q{i+1} missing question"
    assert 'options' in q, f"Q{i+1} missing options"
    assert len(q['options']) == 5, f"Q{i+1} has {len(q['options'])} options"
    assert 'answer' in q, f"Q{i+1} missing answer"
    assert 'explanation' in q, f"Q{i+1} missing explanation"
    assert 'difficulty' in q, f"Q{i+1} missing difficulty"
    # Check answer is one of the options
    assert q['answer'] in q['options'], f"Q{i+1} answer not in options"

print(f"All {len(questions)} questions validated")

with open('assets/questions/tkp_3.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Written successfully")
