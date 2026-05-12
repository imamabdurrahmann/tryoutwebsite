import json, re

def q(id, sq, cat, qt, opts, ans, exp):
    return {
        "id": id, "questionId": id, "category": "TWK",
        "subcategory": cat,
        "questionText": qt,
        "options": opts,
        "answer": ans,
        "explanation": exp,
        "difficulty": "hard"
    }

N = "Nasionalisme"
I = "Integritas"
B = "Bela Negara"
P = "Pilar Negara"
L = "Bahasa Indonesia"

questions = [
    # NASIONALISME
    q("twk3_001", "twk3_001", N,
      "Seorang diplomat senior ditugaskan di negara yang sedang mengalami krisis politik dalam. Pemerintah negara tersebut resmi mengakui Taiwan dan membuka hubungan diplomatik formal. Taiwan menawarkan investasi besar untuk proyek infrastruktur yang akan menciptakan puluhan ribu lapangan kerja. China sebagai sekutu Indonesia bersikeras bahwa hubungan dengan Taiwan adalah garis merah. Keputusan Anda akan menentukan hubungan bilateral dengan China dan reputasi Indonesia di kawasan.",
      ["Terima investasi dari Taiwan karena kepentingan ekonomi warga lokal lebih prioritas",
       "Tolak investasi dari Taiwan dan jaga hubungan baik dengan China karena kepentingan strategis regional lebih penting",
       "Negosiasikan investasi dari Taiwan dengan syarat hubungan tidak disebut sebagai pengakuan diplomatik tetapi sebagai kerja sama ekonomi",
       "Serahkan keputusan kepada pemerintah pusat karena masalah ini bersifat strategis",
       "Tunda keputusan sampai krisis politik di negara tersebut selesai"],
      "C",
      "Opsi C menunjukkan prinsip kebijakan luar negeri Indonesia: tidak memihak salah satu superpower, menjaga hubungan dengan semua pihak, mencari solusi kreatif yang menghormati semua kepentingan. Menerima kerja sama ekonomi tanpa pengakuan diplomatik adalah posisi yang konsisten dengan prinsip Satu China."),

    q("twk3_002", "twk3_002", N,
      "Media sosial di Indonesia mengalami polarisasi tajam terkait isu pengelolaan sumber daya alam. Satu kelompok menginginkan nasionalisasi penuh seluruh sektor pertambangan dengan menghapus semua investasi asing. Kelompok lain menuntut liberalisasi penuh untuk menarik investasi asing sebesar-besarnya. Kedua kelompok memiliki argumentasi kuat dan masing-masing memiliki pendukung dari berbagai kalangan.",
      ["Dukung sepenuhnya nasionalisasi karena kekayaan alam adalah milik rakyat Indonesia",
       "Dukung sepenuhnya liberalisasi karena investasi asing adalah satu-satunya cara Indonesia berkembang di era globalisasi",
       "Publikasikan analisis mendalam yang menunjukkan bahwa solusi yang pragmatis adalah kombinasi regulated nationalization",
       "Netralkan diri dengan tidak memberitakan isu ini secara mendalam karena terlalu sensitif secara politik",
       "Selenggarakan debat terbuka antar kedua kubu dan biarkan penonton yang menilai"],
      "C",
      "Opsi C menunjukkan peran media yang bertanggung jawab: tidak memihak secara buta tapi memberikan analisis yang membantu publik memahami kompleksitas isu. Responsible journalism bukan about having no opinion but about presenting facts that help audiences form their own views."),

    q("twk3_003", "twk3_003", N,
      "Indonesia mengajukan diri menjadi tuan rumah organisasi internasional yang berpengaruh. Dalam negosiasi, negara-negara pesaing menempelkan persyaratan agar Indonesia memilih sisi secara tegas dalam konflik geopolitik tertentu. Tanpa komitmen ini, kandidat negara pesaing yang lebih besar akan memenangkan hak hosting. Keikutsertaan Indonesia dipandang strategis untuk pengaruh regional.",
      ["Terima persyaratan dan dukung sisi yang diminta karena manfaat menjadi tuan rumah lebih besar dari risiko berkompromi",
       "Tolak persyaratan dan mundur dari proses bidding karena menjual posisi diplomatik demi keuntungan ekonomi adalah pengkhianatan",
       "Ajukan kontra-proposal yang mempertahankan posisi netral tapi menawarkan kontribusi lebih besar dalam bentuk SDM",
       "Serahkan keputusan kepada rakyat melalui referendum karena isu ini terlalu besar untuk diputuskan oleh pemerintah saja",
       "Negosiasikan persyaratan sambil mengancam mundur jika tidak ada kompromi yang bisa diterima"],
      "C",
      "Opsi C menunjukkan kemampuan diplomasi tingkat tinggi: tidak menerima ultimatum tapi juga tidak langsung menolak, mencari solusi yang memenuhi kebutuhan organisasi tanpa mengorbankan prinsip."),

    q("twk3_004", "twk3_004", N,
      "Indonesia menerima gelombang besar tenaga kerja asing yang kompeten dari negara tetangga yang sedang mengalami sentimen anti-asing. Mereka mengisi posisi-posisi teknis yang dibutuhkan industri lokal tapi tidak bisa diisi oleh tenaga kerja dalam negeri. Perusahaan-perusahaan lokal mulai mengeluh dan menekan agar pemerintah membatasi masuknya tenaga kerja asing secara ketat.",
      ["Batasi masuknya tenaga kerja asing sesuai permintaan perusahaan lokal karena lapangan kerja warga negara harus prioritas utama",
       "Tetap buka pintu untuk tenaga kerja asing yang kompeten karena kebutuhan industri tidak bisa ditunda",
       "Buat kebijakan yang membedakan antara tenaga kerja asing untuk posisi yang tidak bisa diisi tenaga lokal versus posisi yang bisa dilatih",
       "Hapus semua pembatasan dan biarkan mekanisme pasar yang menentukan siapa yang bekerja di Indonesia",
       "Larang semua tenaga kerja asing karena sentimen anti-asing di negara tetangga bisa digunakan sebagai justifikasi"],
      "C",
      "Opsi C menunjukkan kebijakan yang berprinsip dan berbasis evidence: tidak memihak proteksionisme buta atau pasar bebas buta, tapi membuat differentiated policy berdasarkan data konkret."),

    q("twk3_005", "twk3_005", N,
      "Dalam negosiasi perjanjian perdagangan bebas bilateral, mitra Indonesia menuntut agar Indonesia menghapus subsidi di sektor pertanian yang mereka klaim sebagai praktik tidak fair. Subsidi melindungi jutaan petani kecil yang hidup di bawah garis kemiskinan. Tanpa subsidi harga pangan lokal akan naik dan ketahanan pangan terancam. Dengan subsidi, Indonesia dianggap tidak fair oleh mitra yang subsidy pertaniannya jauh lebih besar.",
      ["Hapus subsidi pertanian karena perjanjian perdagangan akan membuka pasar lain dan kesejahteraan petani bisa ditangani melalui program lain",
       "Pertahankan semua subsidi pertanian karena ketahanan pangan adalah kedaulatan yang tidak bisa dikompromikan",
       "Negosiasikan phase-out subsidi secara gradual dengan timeline yang memungkinkan petani beradaptasi",
       "Gugat perjanjian perdagangan bilateral di forum internasional karena mitra dagang sendiri hipokrit",
       "Batalkan seluruh perjanjian perdagangan bebas karena tidak ada bukti manfaat neto bagi rakyat"],
      "C",
      "Opsi C menunjukkan sophisticated approach: tidak naively accepting maupun rejecting, tapi mencari middle ground yang pragmatis. Phase-out gradual dengan alternative support mechanisms mengakui realitas ekonomi sambil memenuhi prinsip fair trade."),

    q("twk3_006", "twk3_006", N,
      "Sekelompok aktivis muda Indonesia membentuk gerakan politik baru berbasis semangat nasionalisme dengan agenda mengurangi ketergantungan pada asing dalam semua aspek kehidupan nasional. Gerakan ini mendapat dukungan massa sangat besar dan mulai mempengaruhi kebijakan pemerintah. Namun ada unsur-unsur yang mulai mengeksklusikan warga negara yang memiliki pandangan berbeda atau berasal dari latar belakang tertentu.",
      ["Dukung gerakan tersebut karena semangat nasionalisme adalah hal positif dan pemerintah harus mendengarkan suara rakyat",
       "Kritik gerakan tersebut karena eksklusivitas mereka bertentangan dengan semangat bhinneka tunggal ika",
       "Pantau gerakan tersebut dan jika melanggar hukum ambil tindakan tegas, jika beroperasi dalam koridor hukum hormati hak mereka",
       "Dekati gerakan tersebut dan tawarkan kolaborasi untuk agenda positif sambil sampaikan concerns tentang unsur eksklusivitas",
       "Biarkan gerakan tersebut berkembang karena pemerintah tidak perlu campur tangan dalam politik non-resmi"],
      "C",
      "Opsi C menunjukkan keseimbangan antara menghormati hak sipil dan mempertahankan prinsip negara hukum: tidak mendukung atau menolak berdasarkan ideologi tapi berdasarkan perilaku."),

    # INTEGRITAS
    q("twk3_007", "twk3_007", I,
      "Anda anggota DPR yang menerima informasi bahwa vendor besar yang memenangkan tender proyek infrastruktur di daerah pemilihan memiliki hubungan keluarga dengan menteri terkait. Tender secara teknis sudah comply dengan prosedur namun ada irregularities yang jika diinvestigasi bisa membuka pertanyaan tentang fairness process. Vendors lain yang kalah adalah konstituen Anda.",
      ["Lakukan investigation independen di komisi budget dan minta klarifikasi dari menteri, sampaikan hasilnya secara transparan",
       "Diam karena semua proses tender sudah comply secara teknis dan hubungan keluarga tidak bisa jadi dasar pembatalan",
       "Hubungi menteri secara pribadi dan minta dia memastikan prosesnya fair tanpa written record",
       "Publikasikan informasi tentang hubungan keluarga tersebut di media sosial agar publik bisa menilai sendiri",
       "Sampaikan ke konstituen bahwa tender sudah comply dan jika tidak puas bisa menempuh jalur hukum"],
      "A",
      "Opsi A menunjukkan integritas legislatif yang tepat: tidak menutup mata terhadap potential conflict of interest tapi tidak langsung mempublikasikan tanpa investigation. Channel komisi budget adalah mekanisme checks and balances yang tepat."),

    q("twk3_008", "twk3_008", I,
      "Anda kepala daerah yang menerima laporan bahwa realisasi anggaran pembangunan di daerah memiliki selisih sangat signifikan antara perencanaan dan implementasi: banyak proyek dianggarkan tidak terealisasi tapi dananya sudah dicairkan. Audit internal awal menunjukkan dokumen-dokumen pendukung tampaknya telah dimanipulasi. Beberapa pejabat tinggi mungkin terlibat dan memiliki hubungan politik erat dengan pimpinan pusat.",
      ["Eskalasi temuan ke BPKP dan inspektorat dengan semua bukti karena korupsi anggaran adalah kejahatan terhadap rakyat",
       "Lakukan audit internal menyeluruh terlebih dahulu sebelum eskalasi agar memiliki bukti lebih kuat",
       "Konfrontasi pejabat yang dicurigai dan minta mereka memperbaiki situasi secara sukarela tanpa eskalasi",
       "Buat laporan audit yang soft-pedal temuan dan sampaikan bahwa semuanya adalah kesalahan teknis bukan korupsi",
       "Serahkan temuan kepada media agar publik mengetahui dan bisa menekan system untuk bertindak"],
      "A",
      "Opsi A menunjukkan integritas leadership yang tidak bisa dikompromikan: korupsi anggaran pembangunan adalah pengkhianatan terhadap trust masyarakat. Channel eskalasi ke BPKP dan inspektorat adalah mekanisme yang tepat."),

    q("twk3_009", "twk3_009", I,
      "Anda inspektur daerah yang menerima anonymous laporan tentang praktik gratifikasi yang meluas di beberapa OPD. Hampir semua pejabat menerima gratifikasi dalam berbagai bentuk dan sudah menjadi budaya yang dinormalisasi. Jika semua ditindaklanjuti, hampir seluruh leadership OPD akan terjerat kasus dan pelayanan publik akan lumpuh total.",
      ["Tindaklanjuti semua laporan secara penuh karena tidak ada forgivenes untuk korupsi: korupsi tetap korupsi",
       "Buat program amnesty terbatas untuk gratifikasi masa lalu dengan syarat pengungkapan penuh dan zero tolerance ke depan",
       "Abaikan laporan anonymous tersebut karena tidak bisa diverifikasi"],
      "B",
      "Opsi B menunjukkan pragmatic approach terhadap masalah sistemik: tidak amnesty untuk korupsi tapi mengakui bahwa normalisasi gratifikasi menciptakan situasi di mana pejabat tertentu tidak punya pilihan realistis selain berpartisipasi."),

    q("twk3_010", "twk3_010", I,
      "Anda mengelola sistem e-procurement yang digunakan seluruh pemerintah daerah. Anda menemukan vulnerability yang memungkinkan vendor tertentu mendapatkan informasi tentang bid kompetitor sebelum batas waktu submission. Anda sudah memastikan vulnerability diperbaiki tapi tidak memiliki bukti bahwa ada vendor yang sebenarnya telah mengeksploitasi ini untuk memenangkan kontrak secara tidak fair.",
      ["Lakukan audit forensik untuk mencari bukti apakah vulnerability dieksploitasi, proses semua kontrak yang affected",
       "Amankan vulnerability dan pertimbangkan selesai karena tidak ada bukti eksploitasi dan audit akan memakan biaya besar",
       "Publikasikan vulnerability yang sudah ditemukan sebagai transparansi kepada publik",
       "Laporkan ke police karena eksploitasi vulnerability adalah tindak pidana meskipun tidak ada bukti",
       "Ceritakan kepada vendor-vendor bahwa vulnerability sudah diperbaiki agar mereka tenang"],
      "A",
      "Opsi A menunjukkan pendekatan yang bertanggung jawab: tidak mengabaikan risiko bahwa vulnerability mungkin dieksploitasi tapi juga tidak langsung menuduh tanpa bukti. Audit forensik memberikan basis untuk action yang proportionate."),

    q("twk3_011", "twk3_011", I,
      "Anda pemimpin partai politik yang sedang proses rekonsiliasi dengan elit dari era Orde Baru yang dikritik karena penyimpangan. Menerima mereka kembali akan memberikan dukungan finansial dan infrastruktur politik yang dibutuhkan untuk memenangkan pemilu. Namun supporter partai yang sebagian adalah korban atau keturunan korban penyimpangan era tersebut dengan keras menolak rekonsiliasi ini.",
      ["Terima rekonsiliasi karena politik adalah coalition building dan masa lalu tidak bisa diubah",
       "Tolak rekonsiliasi karena nilai-nilai partai tidak bisa dikompromikan untuk alasan elektoral",
       "Terima rekonsiliasi tapi dengan persyaratan transparansi tentang penyimpangan masa lalu, pemulihan korban, dan monitoring system",
       "Serahkan keputusan kepada seluruh members partai melalui voting karena ini keputusan fundamental tentang identitas partai",
       "Tunda rekonsiliasi sampai setelah pemilu karena membuka luka lama akan mengganggu fokus elektoral"],
      "C",
      "Opsi C menunjukkan sophisticated political judgment: tidak blindly accepting maupun rejecting tapi menggunakan posisi leverage untuk добиться justice. Persyaratan transparansi dan monitoring adalah cara rekonsiliasi tanpa mengorbankan prinsip."),

    q("twk3_012", "twk3_012", I,
      "Anda hakim yang preside dalam sidang korupsi besar. Terdakwa adalah pengusaha kaya yang jelas-jelas bersalah. Namun jika menghukum penuh sesuai undang-undang, perusahaan milik Terdakwa yang employer terbesar di daerah akan bangkrut dan ribuan warga kehilangan pekerjaan. Jika membebaskan Terdakwa Anda merusak integritas sistem hukum.",
      ["Hukum Terdakwa sesuai undang-undang karena rule of law tidak bisa dikompromikan dengan pertimbangan ekonomi",
       "Bebaskan Terdakwa karena menghukum pengusaha yang salah bukan решение bijaksana jika konsekuensinya ribuan pengangguran",
       "Hukum Terdakwa dengan hukuman percobaan dan denda besar, dengan syarat operasi perusahaan tetap jalan",
       "Minta penundaan persidangan dan kirimkan rekomendasi kepada eksekutif untuk menyelamatkan perusahaan sebelum memutus",
       "Hukum sesuai hukum tapi sampaikan bahwa konsekuensi ekonomi adalah tanggung jawab bersama yang harus diaddress oleh pemerintah"],
      "E",
      "Opsi E menunjukkan judicial integrity tertinggi: menghukum sesuai hukum tanpa compromise, namun secara jujur acknowledge konsekuensi sistemik. Mendelegasikan konsekuensi ekonomi kepada branch yang tepat sambil mempertahankan prinsip bahwa keadilan tidak bisa diukur dengan uang."),

    # BELA NEGARA
    q("twk3_013", "twk3_013", B,
      "Negara tetangga mempermasalahkan batas wilayah laut di kawasan yang rich dengan sumber daya ikan dan possible hydrocarbon deposits. Indonesia klaim berdasarkan UNCLOS 1982 yang sudah diratifikasi kedua negara. Negara tetangga klaim berdasarkan interpretasi historis berbeda. Masyarakatnelayan dari kedua negara sudah puluhan tahun menangkap ikan di waters tersebut.",
      ["Kompromikan klaim berdasarkan UNCLOS demi perdamaian dengan membagi zona berdasarkan historical fishing patterns",
       "Gunakan full military force untuk mempertahankan klaim karena UNCLOS sudah jelas",
       "Ajak negara tetangga ke meja negosiasi dengan mediator internasional, sampaikan posisi berdasarkan UNCLOS",
       "Serahkan sengketa kepada pengadilan internasional karena semua klaim berdasarkan hukum internasional",
       "Lakukan joint development zone di mana kedua negara berbagi sumber daya tanpa menyelesaikan sengketa klaim terlebih dahulu"],
      "E",
      "Opsi E menunjukkan pragmatic maritime diplomacy: tidak menyelesaikan sengketa yang bisa memakan decade tapi mulai menghasilkan manfaat bersama bagi masyarakat yang sudah bergantung pada waters tersebut selama generations."),

    q("twk3_014", "twk3_014", B,
      "Sebuah grup teroris internasional menyatakan niat untuk menyerang fasilitas strategis Indonesia. Inteligensia menunjukkan mereka memiliki kapasitas untuk executes attack tapi belum tentu memiliki motivasi kuat unless mereka bisa mendapat publicity besar dari serangan tersebut. Di saat bersamaan media mengekspos berita tentang kelemahan keamanan infrastruktur kritis sebagai bagian dari investigasi journalism yang legitimate.",
      ["Batasi sementara semua reporting tentang infrastruktur kritis di media karena tidak ada keamanan yang bisa dijamin jika informasi terus dipublikasikan",
       "Koordinasikan dengan media untuk menunda publikasi tertentu sampai situasi keamanan membaik tanpa memaksa media untuk服从",
       "Tidak mengambil tindakan apapun terhadap media karena kebebasan pers adalah prinsip yang tidak bisa dikompromikan",
       "Bagikan semua informasi tentang ancaman terror kepada publik agar masyarakat bisa vigilance",
       "Tingkatkan security di semua fasilitas kritis berdasarkan threat intelligence tanpa mengubah kebijakan media sama sekali"],
      "E",
      "Opsi E menunjukkan bahwa langkah keamanan yang responsible tidak harus mengorbankan kebebasan pers. Inteligensia tentang ancaman digunakan untuk security upgrade, sementara pers memiliki kebebasan untuk memberitakan apa yang menjadi interesse publik."),

    q("twk3_015", "twk3_015", B,
      "Indonesia ditawari bergabung dalam aliansi keamanan baru dengan perlindungan kuat terhadap ancaman eksternal. Keikutsertaan berarti Indonesia harus mengurangi konsultasi dengan beberapa negara lain yang menjadi mitra strategis. Beberapa mitra ini adalah negara yang memiliki hubungan baik dengan China maupun AS sekaligus dan posisi mediator telah memberikan Indonesia leverage diplomatik yang berharga.",
      ["Terima keikutsertaan dalam aliansi karena perlindungan terhadap ancaman eksternal adalah prioritas utama",
       "Tolak keikutsertaan karena posisi mediator dan koneksi dengan semua blok adalah aset strategis yang tidak boleh dikorbankan",
       "Negosiasikan status asosiasi non-keanggotaan penuh dalam aliansi sehingga可以获得 beberapa manfaat tanpa memilih сторона secara tegas",
       "Lakukan tinjauan keamanan nasional terlebih dahulu dengan melibatkan semua pemangku kepentingan sebelum mengambil keputusan",
       "Ajukan referendum kepada rakyat karena bergabung dalam aliansi militer mengubah posisi strategis Indonesia secara fundamental"],
      "C",
      "Opsi C menunjukkan sophisticated strategic thinking: tidak menerima atau menolak secara biner tapi mencari posisi yang memberikan manfaat maksimal dengan biaya minimal. Associated status adalah middle ground yang pragmatic."),

    q("twk3_016", "twk3_016", B,
      "Rencana wajib militer untuk semua warga negara dipertimbangkan kembali. Pihak militer mendukung karena dianggap penting untuk bela negara dan pertahanan nasional. Kritikus mengeritik karena akan mengeluarkan young people dari pendidikan dan ekonomi selama 1-2 tahun dengan budget yang sangat besar.",
      ["Implementasikan wajib militer penuh sesuai permintaan militer karena bela negara adalah tanggung jawab setiap warga",
       "Tolak wajib militer karena biaya dan dampak sosial ekonomi terlalu besar",
       "Buat program wajib militer yang terdiferensiasi: untuk yang punya keahlian bisa pengabdian dalam bentuk lain, untuk yang lain lebih pendek",
       "Lakukan пилотный проект wajib militer di beberapa daerah terlebih dahulu untuk mengevaluasi efektivitas",
       "Serahkan keputusan kepada generasi muda melalui survei nasional karena merekalah yang paling affected"],
      "C",
      "Opsi C menunjukkan kebijakan yang sophisticated: mendukung principle bela negara tapi dengan implementation yang pragmatic dan tidak one-size-fits-all. Differentiated approach memaksimalkan efisiensi dari ресурсов."),

    q("twk3_017", "twk3_017", B,
      "Sebuah perusahaan teknologi asing ingin membangun data center besar di Indonesia untuk menyimpan data warga negara Indonesia. Keuntungan ekonomi signifikan dan ribuan lapangan kerja diciptakan. Namun ada kekhawatiran bahwa data warga akan disimpan di luar kendali regulator Indonesia dan bisa menjadi инструмент espionage oleh negara asal perusahaan tersebut.",
      ["Izinkan dengan persyaratan bahwa semua data harus disimpan di servers di Indonesia dan subject к законодательству Indonesia",
       "Tolak sepenuhnya karena risiko espionage terlalu besar",
       "Izinkan dengan persyaratan data localization dan minta perusahaan berikan source code access untuk audit independen secara berkala",
       "Minta perusahaan menjadi joint venture dengan perusahaan Indonesia sehingga ada representation Indonesia dalam governance",
       "Buat тендер terbuka untuk multiple perusahaan termasuk domestic dan foreign, pilih berdasarkan hasil evaluasi security dan ekonomi"],
      "E",
      "Opsi E menunjukkan bahwa competitive procurement adalah kunci untuk mendapatkan deal terbaik bagi negara. тендер terbuka juga menghindari обвинения в коррупции и протекционизме."),

    q("twk3_018", "twk3_018", B,
      "Beberapa wilayah perbatasan Indonesia mengalami проблема identitas karena warga di perbatasan hidup dalam ekonomi borderless. Mereka melintasi batas setiap hari untuk bekerja, belajar, dan mengakses layanan kesehatan. Beberapa memiliki статус sebagai warga negara Indonesia tapi secara faktual hidup lebih banyak di luar negeri dan loyality mereka dipertanyakan.",
      ["Berlakukan bahwa warga Indonesia di perbatasan harus tinggal di Indonesia untuk mempertahankan hak pilih dan akses layanan publik",
       "Buat kebijakan khusus untuk zona perbatasan yang mengakui realitas ekonomi cross-border sambil mempertahankan статус kewarganegaraan",
       "Larang warga perbatasan bekerja di luar negeri karena mereka adalah warga negara Indonesia",
       "Biarkan saja karena kondisi perbatasan yang kompleks sudah berlangsung generations",
       "Lakukan program возвращение yang memberikan incentives bagi warga perbatasan untuk lebih banyak tinggal di Indonesia"],
      "B",
      "Opsi B menunjukkan humanitarian approach yang juga patriotic: mengakui realitas ekonomi perbatasan yang sudah generations tanpa mengorbankan prinsip kewarganegaraan. Zona perbatasan khusus dengan hak penuh adalah solusi yang pragmatic dan tidak diskriminatif."),

    # PILAR NEGARA
    q("twk3_019", "twk3_019", P,
      "Mahkamah Konstitusi harus memutus apakah undang-undang yang memberikan wewenang membatasi kebebasan bergerak selama keadaan darurat adalah konstitusional. Undang-undang terbukti effective selama pandemi tapi juga berpotensi disalahgunakan untuk membatasi hak демократических граждан di masa depan. Para hakim memiliki pandangan sangat terbagi.",
      ["Nyatakan undang-undang inkonstitusional karena kebebasan bergerak adalah hak dasar yang tidak bisa dibatasi even dengan alasan darurat",
       "Nyatakan undang-undang konstitusional karena pemerintah perlu memiliki инструменты untuk keadaan darurat",
       "Nyatakan undang-undang konstitusional dengan syarat independent oversight mechanism yang ketat dan time limit yang jelas",
       "Tunda putusan sampai keadaan darurat selesai karena tidak etis memutuskan tentang hak during emergency",
       "Serahkan keputusan kepada publik melalui referendum karena masalah ini terlalu fundamental untuk 9 hakim saja"],
      "C",
      "Opsi C menunjukkan constitutional adjudication yang sophisticated: tidak naively striking down maupun upholding tapi menambahkan structural safeguards yang membuat undang-undang work for its legitimate purpose without becoming a tool of abuse."),

    q("twk3_020", "twk3_020", P,
      "Proyek pembangunan ibu kota baru dalam bahaya besar: kontraktor utama telah bangkrut dan tidak mampu melanjutkan pekerjaan, investasi sudah dilakukan sangat besar, waktu terbatas. Kontrak memiliki ketentuan tentang default tapi menerapkan ketentuan tersebut akan означать proyek berhenti total. Beberapa kontraktor lain menyatakan minat mengambil alih dengan kondisi berbeda dari kontrak awal.",
      ["Terapkan ketentuan default secara penuh karena kontrak adalah hukum dan tidak ada exception untuk proyek besar",
       "Renegosiasi kontrak dengan kontraktor bangkrut untuk menemukan solusi yang memungkinkan proyek tetap berjalan",
       "Batalkan proyek total dan gunakan dana yang sudah dikeluarkan sebagai lessons learned",
       "Lakukan тендер cepat untuk kontraktor pengganti dengan conditions yang revised namun tetap competitive dan transparan",
       "Minta kontraktor pengganti mengambil alih dengan subsidi negara karena melindungi pekerja lebih penting dari prinsip"],
      "D",
      "Opsi D menunjukkan balanced approach: mengakui bahwa default punya konsekuensi sistemik yang serius, tapi tidak memaksa solusi yang mungkin corrupted pada situasi krisis. тендер cepat yang tetap transparan adalah middle ground."),

    q("twk3_021", "twk3_021", P,
      "Kehutanan Indonesia dalam krisis: deforestation mencapai angka mengkhawatirkan despite regulasi yang ada. Sebagian besar deforestation dilakukan oleh perusahaan besar dengan izin resmi dari pemerintah daerah dengan persetujuan pusat. Beberapa telah diskualifikasi pusat tapi izin daerah tetap berlaku karena ambiguitas antara tingkat pemerintahan.",
      ["Berikan wewenang penuh ke pusat untuk membatalkan semua izin yang bertentangan tanpa persetujuan daerah",
       "Strengthen kapasitas daerah untuk enforcement tapi dengan monitoring system dari pusat",
       "Buat commission independen yang memiliki wewenang untuk menyelidiki dan membatalkan izin yang bermasalah tanpa memandang tingkat pemerintahan",
       "Tingkatkan punishment untuk deforestation menjadi sangat berat termasuk pidana penjara panjang",
       "Serahkan seluruh hutan kepada masyarakat adat karena merekalah yang paling memiliki insentif untuk melestarikan"],
      "C",
      "Opsi C menunjukkan structural solution terhadap masalah sistemik: menciptakan mekanisme independen yang bisa跨立 уровни pemerintahan untuk menangani masalah yang jelas-jelas sistemный."),

    q("twk3_022", "twk3_022", P,
      "UNESCO memberikan tantangan kepada Indonesia: develop program pelestarian budaya untuk dinilai secara internasional sebagai syarat mendapatkan статус warisan dunia untuk beberapa situs budaya Indonesia. Program memerlukan resources besar dan berpotensi mengubah cara masyarakat adat hidup di situs tersebut. Beberapa sangat bergantung pada praktik tradisional yang mungkin tidakсовместим dengan modernisasi untuk standar UNESCO.",
      ["Terima tantangan UNESCO dengan penuh dan alokasikan resources yang diperlukan tanpa compromise",
       "Tolak participate dalam program UNESCO karena standar internasional tidak selalu sesuai dengan realitas budaya Indonesia",
       "Participate tapi negosiasikan exception untuk praktik budaya tertentu yang tidak bisa dimodernisasi",
       "Lakukan dialog dengan masyarakat adat dan kembangkan program yang menggabungkan international standards dengan vision mereka sendiri",
       "Accept program UNESCO tapi dengan reservasi bahwa beberapa aspek akan implemented secara gradual dalam timeline yang tidak mengorbankan kesejahteraan"],
      "D",
      "Opsi D menunjukkan participatory approach yang paling sesuai: masyarakat adat sebagai experts tentang budaya mereka sendiri dan siapapun harus menjadi keputusan akhir tentang bagaimana warisan mereka dilestarikan."),

    q("twk3_023", "twk3_023", P,
      "Pengadilan agama dan pengadilan umum memiliki dispute yurisdiksi yang sudah lama. Pasangan campuran agama yang bercerai harus menghadapi persidangan di kedua pengadilan untuk berbagai aspek perceraian mereka. Hasilnya tidak konsisten dan seringkali tidak adil bagi salah satu pihak karena each court memiliki pendekatan berbeda.",
      ["Buat satu unified court system yang menangani semua perkara termasuk agama untuk menghindari inconsistensi",
       "Pertahankan dual system tapi dengan mekanisme koordinasi yang kuat untuk menghindari conflicting rulings",
       "Pindahkan semua perkara perceraian ke pengadilan umum dengan hakim yang memiliki pelatihan agama",
       "Biarkan saja karena perbedaan yurisdiksi adalah cerminan dari pengakuan terhadap pluralitas Indonesia",
       "Buat specialized court untuk perkara yang melibatkan berbagai yurisdiksi dengan hakim dari berbagai latar belakang"],
      "E",
      "Opsi E menunjukkan innovative approach: menciptakan mekanisme yang recognize complexity dari Indonesia's legal landscape. Specialized court dengan diverse judges adalah solusi yang respects pluralism sambil mengatasi jurisdictional conflict."),

    q("twk3_024", "twk3_024", P,
      "Undang-undang desentralisasi memberikan lebih banyak wewenang kepada daerah tapi banyak daerah tidak memiliki kapasitas untuk menggunakan wewenang baru secara efektif. Beberapa daerah besar sudah siap tapi banyak daerah kecil justru merasa overwhelmed. Beberapa都开始 melakukan penyimpangan karena lack of capacity untuk menjalankan fungsi baru.",
      ["Peroleh wewenang kembali ke pusat karena desentralisasi tidak работает dan banyak daerah tidak могут handle tanggung jawab",
       "Pertahankan desentralisasi tapi dengan massive capacity building yang membantu daerah yang tertinggal",
       "Diferensiasikan tingkat desentralisasi berdasarkan kapasitas daerah: daerah lebih mampu mendapat wewenang lebih besar",
       "Buat mekanisme sharing resources antara daerah yang lebih mampu dan yang kurang mampu",
       "Tunda implementasi sampai semua daerah bisa menunjukkan kapasitas melalui independent assessment"],
      "C",
      "Opsi C menunjukkan nuanced understanding dari federalism yang berbeda: tidak all-or-nothing antara централизация dan desentralisasi penuh. Diferensiasi berdasarkan kapasitas adalah evidence-based approach."),

    # BAHASA INDONESIA
    q("twk3_025", "twk3_025", L,
      "Ministry ingin mengeluarkan pedoman penulisan resmi yang mewajibkan penggunaan bahasa Indonesia baku dalam semua dokumen resmi pemerintah. Kritikus berpendapat bahwa требование ini akan menghambat komunikasi terutama dalam konteks teknis dan ilmiah di mana banyak istilah tidak ada padanan dalam bahasa Indonesia. Sebagian warga lebih nyaman menggunakan bahasa daerah atau bahasa Inggris dalam konteks profesional.",
      ["Terapkan mandatory penggunaan bahasa Indonesia baku dalam semua dokumen resmi karena ini kewajiban konstitusional",
       "Izinkan penggunaan bahasa Inggris atau bahasa daerah dalam dokumen resmi untuk konteks teknis dengan terjemahan sebagai lampiran",
       "Buat daftar istilah teknis yang sudah memiliki padanan bahasa Indonesia baku, untuk istilah yang belum ada izin penggunaan bahasa asing",
       "Lakukan kongres bahasa terlebih dahulu untuk menetapkan padanan istilah sebelum menerapkan mandatory rule",
       "Serahkan keputusan kepada Akademi Bahasa Indonesia karena merekalah yang paling kompeten"],
      "C",
      "Opsi C menunjukkan pragmatisme linguistik: tidak blindly insisting on bahasa Indonesia tanpa recognition bahwa banyak istilah teknis tidak memiliki padanan, tapi juga tidak abandoning effort untuk mengembangkan bahasa baku."),

    q("twk3_026", "twk3_026", L,
      "Peraturan baru melarang penggunaan bahasa gaul dan slang dalam dokumen resmi pemerintahan dan media massa. Pendukung berpendapat bahasa Indonesia sedang terancam oleh terlalu banyak bahasa gaul yang tidak baku. Kritikus berpendapat bahasa adalah entitas organik yang terus berevolusi dan tidak bisa diatur melalui regulasi.",
      ["Dukung peraturan tersebut karena pelestarian bahasa Indonesia baku adalah keharusan dan без enforcement bahasa akan corrupted",
       "Tolak peraturan tersebut karena bahasa tidak bisa diatur melalui hukum dan upaya-upayaan sebelumnya selalu gagal",
       "Buat program yang mendorong penggunaan bahasa Indonesia baku melalui incentive dan awards bukan melalui pelarangan",
       "Buat diferensiasi: dalam dokumen resmi terapkan standar bahasa baku, untuk konteks tidak-formal biarkan bahasa berkembang",
       "Lakukan riset terlebih dahulu untuk menentukan apakah bahasa Indonesia benar-benar terancam atau ini overreaction"],
      "D",
      "Opsi D menunjukkan realistic approach: membedakan antara konteks formal dan informal adalah hal yang wajar. Bahasa baku perlu di-maintain dalam konteks resmi tapi bahasa organik harus bisa berkembang dalam konteks tidak resmi."),

    q("twk3_027", "twk3_027", L,
      "Surat resmi dari government agency harus disampaikan kepada publik. Draft sudah ditulis dengan bahasa Indonesia yang benar secara tata bahasa namun sulit dipahami karena terlalu formal dengan banyak kalimat pasif yang berbelit-belit. Versi lebih sederhana akan lebih mudah dipahami tapi mungkin dianggap kurang formal.",
      ["Gunakan versi formal dan sulit dipahami karena dokumen resmi harus mengikuti standar bahasa Indonesia baku",
       "Gunakan versi sederhana yang mudah dipahami karena tujuan komunikasi publik adalah transfer informasi yang efektif",
       "Buat dua versi: satu untuk arsip resmi dan satu untuk publik, keduanya sampaikan informasi yang sama",
       "Buat versi hybrid yang mempertahankan bahasa baku tapi dalam kalimat aktif dan langsung sehingga accessible",
       "Minta feedback dari target audience sebelum memutuskan"],
      "D",
      "Opsi D menunjukkan bahwa formalitas dan aksesibilitas tidak harus saling исключать: bahasa baku bisa ditulis dalam kalimat aktif yang langsung tanpa mengorbankan tata bahasa yang benar."),

    q("twk3_028", "twk3_028", L,
      "Karya sastra Indonesia harus diterjemahkan ke bahasa Inggris untuk dipublikasikan secara internasional. Pendekatan literal faithfully reproduces teks Indonesia termasuk struktur tata bahasa dengan catatan kaki. Pendekatan adaptif mengadaptasi teks untuk beresonansi dengan pembaca berbahasa Inggris meskipun menyimpang dari teks asli.",
      ["Prioritaskan terjemahan literal karena karya sastra Indonesia harus представлен apa adanya dalam bahasa aslinya",
       "Prioritaskan terjemahan adaptif karena tujuannya adalah sampaikan pengalaman Indonesia kepada pembaca internasional",
       "Pilih pendekatan middle ground yang melakukan adaptasi untuk элементы yang untranslatable tapi pertahankan как bisa banyak struktur Indonesia",
       "Serahkan kepada penulis karya tersebut untuk memutuskan karena merekalah yang paling memahami nuansa karya mereka",
       "Buat dua terjemahan: satu untuk academic audience yang menghargai literalness, satu untuk general audience"],
      "C",
      "Opsi C menunjukkan pendekatan balanced: neither pure literalism nor complete adaptation is optimal. A nuanced approach that prioritizes emotional and cultural authenticity while maintaining as much of the original structure as possible serves both fidelity and impact."),

    q("twk3_029", "twk3_029", L,
      "Penggunaan bahasa Inggris sebagai lingua franca dalam akademia dan bisnis internasional sudah menjadi standar. Banyak universities Indonesia mengajarkan matakuliah dalam bahasa Inggris untuk meningkatkan global competitiveness. Kritikus berpendapat ini berkontribusi pada erosi bahasa Indonesia sebagai bahasa ilmu pengetahuan karena rekaman sejarah menunjukkan bahwa bahasa bisa развиваться hanya melalui penggunaan aktif dalam ranah intelektual.",
      ["Taati penuh aturan penggunaan bahasa Indonesia karena ini implementasi dari kebijakan yang sudah disepakati",
       "Gunakan bahasa Inggris karena efektivitas komunikasi dalam konteks technical training adalah prioritas utama",
       "Gunakan bahasa Indonesia dengan istilah teknis dalam bahasa Inggris sebagai bridge sampai terminology Indonesia berkembang, dengan penjelasan bahwa penggunaan Inggris bersifat временны",
       "Предложите руководству agar melakukan evaluasi dengan membandingkan performancepeserta dalam kedua bahasa",
       "Jangan mengambil tindakan apapun karena masalah ini terlalu kompleks untuk dipecahkan secara individual"],
      "C",
      "Opsi C menunjukkan pragmatic approach yang linguistically sensitive: tidak menolak penggunaan bahasa Inggris yang masih diperlukan, tidak abandon bahasa Indonesia, tapi menggunakannya sebagai bridge dengan acknowledgment bahwa solusi bersifat временны."),

    q("twk3_030", "twk3_030", L,
      "Bahasa daerah semakin jarang digunakan oleh generasi muda dan beberapa sudah начинают классифицировать sebagai endangered languages. Beberapa pihak menyerukan intervensi pemerintah untuk melestarikan bahasa daerah melalui программы pendidikan formal. Pihak lain menganggap bahasa daerah adalah heritage yang should be preserved voluntarily oleh community speakers bukan melalui program top-down.",
      ["Implementasikan программа pelestarian bahasa daerah melalui kurikulum pendidikan formal karena intervention diperlukan sebelum terlambat",
       "Hormati pilihan masyarakat untuk tidak menggunakan bahasa daerah dan biarkan proses natural terjadi",
       "Buat программа pelestarian yang berkolaborasi dengan masyarakat adat sebagai partners bukan subjects, dengan content dan approach ditentukan oleh masyarakat sendiri",
       "Fokuskan resources pada dokumentasi dan архивирование bahasa daerah yang sudah hampir punah tanpa mencoba menghidupkan kembali penggunaan aktif",
       "Integrasikan bahasa daerah sebagai mata pelajaran optional di sekolah daerah dengan guru dari komunitas lokal"],
      "C",
      "Opsi C menunjukkan decolonized approach: masyarakat adat sebagai partners dengan agency penuh. Pendekatan ini lebih berkelanjutan karena ownership atas program ada pada masyarakat sendiri. Funding dari pemerintah menyediakan resources tanpa menciptakan dependency atau imposing внешний agenda."),
]

# Validate
bad = 0
for i, q in enumerate(questions):
    for key in ['questionText', 'answer', 'explanation']:
        if key in q:
            if re.search(r'[^\x00-\x7F]', str(q[key])):
                print(f"Q{i+1} {key}: NON-ASCII")
                bad += 1
    for j, opt in enumerate(q.get('options', [])):
        if re.search(r'[^\x00-\x7F]', str(opt)):
            print(f"Q{i+1} opt[{j}]: NON-ASCII")
            bad += 1

hard = sum(1 for q in questions if q['difficulty'] == 'hard')
print(f"Total: {len(questions)}, Hard: {hard}, Non-ASCII: {bad}")

with open('assets/questions/twk_3.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Written successfully")