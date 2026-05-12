import json, re

questions = [
    # === NASIONALISME (6) ===
    {
        "id": "twk3_001", "questionId": "twk3_001", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Seorang diplomat senior Indonesia ditugaskan di negara yang sedang mengalami krisis politik dalam negeri. Pemerintah negara tersebut resmi mengakui eksistensi Taiwan dan membuka hubungan diplomatik formal. Secara bersamaan Taiwan menawarkan investasi besar untuk proyek infrastruktur yang akan menciptakan puluhan ribu lapangan kerja bagi warga lokal. China sebagai sekutu diplomatik Indonesia bersikeras bahwa hubungan dengan Taiwan adalah garis merah. Keputusan Anda akan menentukan hubungan bilateral dengan China dan reputasi Indonesia di kawasan.",
        "options": [
            "Terima investasi dari Taiwan karena kepentingan ekonomi warga lokal lebih prioritas dan Indonesia tidak memiliki kewajiban untuk mengikuti kehendak China dalam hal ini",
            "Tolak investasi dari Taiwan dan jaga hubungan baik dengan China karena kepentingan strategis regional lebih penting dari satu proyek investasi",
            "Negosiasikan investasi dari Taiwan dengan syarat hubungan tidak disebut sebagai pengakuan diplomatik tetapi sebagai kerja sama ekonomi, dan sampaikan kondisi ini kepada China sebagai goodwill gesture",
            "Serahkan keputusan kepada pemerintah pusat karena masalah ini bersifat strategis dan berada di luar wewenang diplomat di lapangan",
            "Tunda keputusan sampai krisis politik di negara tersebut selesai karena tidak etis membuat komitmen jangka panjang dengan pemerintah yang mungkin tidak berumur panjang"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan prinsip-prinsip dasar kebijakan luar negeri Indonesia: tidak memihak salah satu superpower, menjaga hubungan dengan semua pihak, dan mencari solusi kreatif yang menghormati semua kepentingan. Menerima kerja sama ekonomi tanpa pengakuan diplomatik adalah posisi yang konsisten dengan prinsip Satu China.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_002", "questionId": "twk3_002", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Media sosial di Indonesia mengalami polarisasi tajam terkait isu pengelolaan sumber daya alam. Satu kelompok menginginkan nasionalisasi penuh seluruh sektor pertambangan dan energi dengan menghapus semua investasi asing. Kelompok lain menuntut liberalisasi penuh untuk menarik investasi asing sebesar-besarnya. Kedua kelompok memiliki argumentasi kuat dan masing-masing memiliki pendukung dari berbagai kalangan termasuk akademisi dan politisi.",
        "options": [
            "Dukung sepenuhnya nasionalisasi karena kekayaan alam adalah milik rakyat Indonesia dan tidak boleh dikuasai asing",
            "Dukung sepenuhnya liberalisasi karena investasi asing adalah satu-satunya cara Indonesia bisa berkembang di era globalisasi",
            "Publikasikan analisis mendalam yang menunjukkan bahwa kedua posisi memiliki kelemahan dan kekuatan masing-masing dan bahwa solusi yang pragmatis adalah kombinasi regulated nationalization yang memastikan kontrol negara tanpa mengorbankan investasi yang dibutuhkan untuk pengembangan",
            "Netralkan diri dengan tidak memberitakan isu ini secara mendalam karena terlalu sensitif secara politik",
            "Selenggarakan debat terbuka antar kedua kubu dan biarkan pembaca yang menentukan tanpa memberikan editorial opinion"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan peran media yang bertanggung jawab: tidak memihak secara buta tapi memberikan analisis yang membantu publik memahami kompleksitas isu. Responsible journalism bukan about having no opinion but about presenting facts and analysis that help audiences form their own views.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_003", "questionId": "twk3_003", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Indonesia mengajukan diri menjadi tuan rumah sebuah organisasi internasional yang berpengaruh. Dalam negosiasi, negara-negara pesaing menempelkan persyaratan agar Indonesia memilih sisi secara tegas dalam konflik geopolitik tertentu. Tanpa komitmen ini, kandidat negara pesaing yang lebih besar akan memenangkan hak hosting. Keikutsertaan Indonesia dipandang strategis untuk pengaruh regional dan akses terhadap teknologi dan pasar baru.",
        "options": [
            "Terima persyaratan dan dukung sisi yang diminta karena manfaat menjadi tuan rumah organisasi internasional lebih besar dari risiko berkompromi pada posisi politik tertentu",
            "Tolak persyaratan dan mundur dari proses bidding karena menjual posisi diplomatik demi keuntungan ekonomi adalah pengkhianatan terhadap prinsip politik luar negeri bebas aktif",
            "Ajukan kontra-proposal yang mempertahankan posisi netral Indonesia tapi menawarkan kontribusi lebih besar dalam bentuk SDM dan resources untuk organisasi",
            "Serahkan keputusan kepada rakyat melalui referendum karena isu geopolitik ini terlalu besar untuk diputuskan oleh pemerintah saja",
            "Negosiasikan persyaratan dengan negara-negara yang menempelkan sambil mengancam mundur jika tidak ada kompromi yang bisa diterima"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan kemampuan diplomasi tingkat tinggi: tidak menerima ultimatum tapi juga tidak langsung menolak, mencari solusi yang memenuhi kebutuhan organisasi tanpa mengorbankan prinsip. Kontribusi dalam bentuk SDM dan resources adalah cara untuk influence tanpa kompromi pada posisi politik.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_004", "questionId": "twk3_004", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Di tengah meningkatnya sentimen anti-asing di beberapa negara tetangga, Indonesia menerima gelombang besar tenaga kerja asing yang kompeten dari negara-negara tersebut. Mereka mengisi posisi-posisi teknis yang dibutuhkan industri lokal tapi tidak bisa diisi oleh tenaga kerja dalam negeri. Perusahaan-perusahaan lokal mulai mengeluh bahwa tenaga kerja asing menduduki posisi strategis dan menekan agar pemerintah membatasi masuknya tenaga kerja asing secara ketat.",
        "options": [
            "Batasi masuknya tenaga kerja asing sesuai permintaan perusahaan lokal karena lapangan kerja warga negara harus menjadi prioritas utama pemerintah",
            "Tetap buka pintu untuk tenaga kerja asing yang kompeten karena kebutuhan industri tidak bisa ditunda dan tenaga kerja lokal belum siap untuk semua posisi",
            "Buat kebijakan yang membedakan antara tenaga kerja asing untuk posisi yang tidak bisa diisi tenaga lokal versus posisi yang bisa diisi tenaga lokal dengan pelatihan, dengan kebijakan yang transparan dan berbasis data",
            "Hapus semua pembatasan dan biarkan mekanisme pasar yang menentukan siapa yang bekerja di Indonesia",
            "Larang semua tenaga kerja asing karena sentimen anti-asing di negara tetangga bisa digunakan sebagai justifikasi untuk membatasi tenaga kerja Indonesia di sana"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan kebijakan yang berprinsip dan berbasis evidence: tidak memihak proteksionisme buta atau pasar bebas buta, tapi membuat differentiated policy berdasarkan data konkret tentang apa yang bisa dan tidak bisa dilakukan oleh tenaga kerja lokal. Transparansi dan berbasis data adalah kunci good governance.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_005", "questionId": "twk3_005", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Dalam negosiasi perjanjian perdagangan bebas bilateral, mitra Indonesia menuntut agar Indonesia menghapus subsidi di sektor pertanian yang mereka klaim sebagai praktik tidak fair. Subsidi tersebut melindungi jutaan petani kecil yang hidup di bawah garis kemiskinan. Tanpa subsidi harga pangan lokal akan naik dan ketahanan pangan nasional terancam. Dengan subsidi, Indonesia dianggap tidak fair oleh mitra dagang yang memiliki subsidy agriculture jauh lebih besar di negaranya sendiri.",
        "options": [
            "Hapus subsidi pertanian karena perjanjian perdagangan bebas akan membuka pasar lain yang lebih besar bagi produk Indonesia dan kesejahteraan petani bisa ditangani melalui program social assistance lain",
            "Pertahankan semua subsidi pertanian karena ketahanan pangan adalah kedaulatan yang tidak bisa dikompromikan untuk kepentingan perdagangan",
            "Negosiasikan phase-out subsidi secara gradual dengan timeline yang memungkinkan petani beradaptasi, sambil mencari alternative support mechanisms yang tidak melanggar perjanjian perdagangan",
            "Gugat perjanjian perdagangan bilateral di forum internasional karena mitra dagang sendiri memberikan subsidi agriculture jauh lebih besar",
            "Batalkan seluruh perjanjian perdagangan bebas karena tidak ada bukti bahwa perjanjian tersebut memberikan manfaat neto bagi rakyat Indonesia"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan sophisticated approach: tidak naively accepting maupun rejecting, tapi mencari middle ground yang pragmatis. Phase-out gradual dengan alternative support mechanisms mengakui realitas ekonomi sambil tetap memenuhi prinsip fair trade. Bukan A yang terlalu trade-focused tanpa regard untuk food security, bukan B yang proteksionis tanpa recognition dari international obligations.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_006", "questionId": "twk3_006", "category": "TWK",
        "subcategory": "Nasionalisme",
        "questionText": "Sekelompok aktivis muda Indonesia ingin membentuk gerakan politik baru berbasis semangat nasionalisme yang kuat dengan agenda utama mengurangi ketergantungan pada asing dalam semua aspek kehidupan nasional. Gerakan ini mendapat dukungan massa yang sangat besar dan mulai mempengaruhi kebijakan pemerintah. Namun dalam gerakan tersebut ada unsur-unsur yang mulai mengeksklusikan warga negara Indonesia yang memiliki pandangan berbeda atau berasal dari latar belakang tertentu.",
        "options": [
            "Dukung gerakan tersebut karena semangat nasionalisme adalah hal yang positif dan pemerintah harus mendengarkan suara rakyat",
            "Kritik gerakan tersebut karena eksklusivitas yang mereka praktikkan bertentangan dengan semangat bhinneka tunggal ika dan merusak kohesi nasional",
            "Pantau gerakan tersebut dan jika mereka mulai melanggar hukum atau mendorong kekerasan, ambil tindakan hukum yang tegas, namun jika mereka beroperasi dalam koridor hukum, hormati hak mereka untuk menyampaikan pandangan politik",
            "Dekati gerakan tersebut dan tawarkan kolaborasi untuk agenda positif mereka sambil secara private menyampaikan concerns tentang unsur eksklusivitas",
            "Biarkan gerakan tersebut berkembang karena setiap gerakan politik memiliki dinamika internal dan pemerintah tidak perlu campur tangan dalam politik non-resmi"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan keseimbangan antara menghormati hak sipil dan mempertahankan prinsip negara hukum: tidak mendukung atau menolak berdasarkan ideologi, tapi berdasarkan perilaku. Jika beroperasi dalam hukum, gerakan memiliki hak yang harus dihormati. Jika melanggar, action yang tegas diperlukan regardless dari ideologi gerakan.",
        "difficulty": "hard"
    },
    # === INTEGRITAS (6) ===
    {
        "id": "twk3_007", "questionId": "twk3_007", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah anggota DPR yang menerima informasi bahwa salah satu vendor besar yang memenangkan tender proyek infrastruktur di daerah pemilihan Anda memiliki hubungan keluarga dengan seorang menteri yang membawahi ministry terkait. Tender secara teknis sudah comply dengan prosedur namun ada beberapa irregularities yang jika diinvestigasi lebih lanjut bisa membuka pertanyaan tentang fairness process. Vendors lain yang kalah sudah mulai bertanya-tanya dan beberapa dari mereka adalah konstituen Anda.",
        "options": [
            "Lakukan investigation independen di komisi budget dan minta klarifikasi dari minister terkait tentang hubungan keluarga vendor dengan dirinya, sampaikan hasilnya secara transparan kepada publik",
            "Diam karena semua proses tender sudah comply secara teknis dan hubungan keluarga tidak bisa dijadikan dasar untuk membatalkan proses yang sudah selesai",
            "Hubungi minister terkait secara pribadi dan sampaikan bahwa Anda mengetahui hubungan tersebut dan minta dia memastikan prosesnya fair, tanpa ada written record dari conversation ini",
            "Publikasikan informasi tentang hubungan keluarga tersebut di media sosial agar publik bisa menilai sendiri",
            "Sampaikan ke konstituen Anda bahwa tender sudah comply secara hukum dan jika mereka tidak puas mereka bisa menempuh jalur hukum"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas legislatif yang tepat: tidak menutup mata terhadap potential conflict of interest tapi tidak juga langsung mempublikasikan tanpa investigation. Channel komisi budget adalah mekanisme checks and balances yang tepat. Transparansi terhadap publik adalah prinsip dasar akuntabilitas legislatif.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_008", "questionId": "twk3_008", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah kepala daerah yang menerima laporan bahwa realisasi anggaran pembangunan di daerah Anda memiliki selisih sangat signifikan antara perencanaan dan implementasi: banyak proyek dianggarkan tidak terealisasi tapi dananya sudah dicairkan. Audit internal awal menunjukkan dokumen-dokumen pendukung tampaknya telah dimanipulasi untuk tampak sesuai prosedur. Beberapa pejabat tinggi di daerah Anda mungkin terlibat dan mereka memiliki hubungan politik yang erat dengan pimpinan pusat.",
        "options": [
            "Eskalasi temuan ke BPKP dan inspektorat jenderal dengan semua bukti yang ada karena korupsi anggaran pembangunan adalah kejahatan terhadap rakyat",
            "Lakukan audit internal menyeluruh terlebih dahulu sebelum eskalasi agar memiliki bukti yang lebih kuat dan comprehensive",
            "Konfrontasi pejabat yang dicurigai dan minta mereka memperbaiki situasi secara sukarela tanpa eskalasi karena membawa kasus ini ke luar akan merusak nama baik daerah",
            "Buat laporan audit yang soft-pedal temuan dan sampaikan bahwa semuanya adalah kesalahan teknis administrasi bukan korupsi",
            "Serahkan temuan kepada media agar publik mengetahui dan bisa menekan system untuk bertindak"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas leadership yang tidak bisa dikompromikan: korupsi anggaran pembangunan adalah pengkhianatan terhadap trust masyarakat. Channel eskalasi ke BPKP dan inspektorat jenderal adalah mekanisme yang tepat karena mereka memiliki wewenang dan independensi untuk menangani kasus seperti ini.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_009", "questionId": "twk3_009", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah inspektur daerah yang menerima anonymous laporan tentang praktik gratifikasi yang meluas di beberapa OPD. Laporan menyebutkan bahwa penerimaan gratifikasi sudah menjadi budaya yang dinormalisasi dan hampir semua pejabat menerima dalam berbagai bentuk. Jika semua ditindaklanjuti, hampir seluruh leadership OPD akan terjerat kasus dan pelayanan publik akan lumpuh total.",
        "options": [
            "Tindaklanjuti semua laporan secara penuh karena tidak ada forgivenes untuk korupsi dan tidak ada ukuran kecilnya korupsi: korupsi tetap korupsi",
            "Buat program amnesty terbatas untuk gratifikasi masa lalu dengan syarat pengungkapan penuh dan komitmen untuk tidak mengulang, dan terapkan zero tolerance untuk gratifikasi di masa depan mulai besok",
            "Investigasi lebih lanjut untuk membedakan antara gratifikasi yang sudah menjadi praktik sistemik yang sulit dihindari pejabat junior versus gratifikasi yang dilakukan secara intentional oleh pejabat senior dengan power",
            "Tunda semua tindakan sampai ada руководство jelas dari tingkat nasional karena masalah ini terlalu sistemik untuk ditangani sendiri",
            "Abaikan laporan anonymous tersebut karena tidak bisa diverifikasi dan investigation berdasarkan laporan anonymous adalah tidak adil bagi yang disebut"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pragmatic approach terhadap masalah sistemik: tidak amnesty untuk korupsi tapi mengakui bahwa normalisasi gratifikasi menciptakan situasi di mana pejabat tertentu tidak punya pilihan realistis selain berpartisipasi. Program amnesty dengan pengungkapan dan zero tolerance ke depan adalah kompromi yang recognize both principle dan realitas.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_010", "questionId": "twk3_010", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah pejabat yang mengelola sistem e-procurement yang digunakan seluruh pemerintah daerah. Anda menemukan vulnerability yang memungkinkan vendor tertentu mendapatkan informasi tentang bid kompetitor sebelum batas waktu submission. Anda sudah memastikan vulnerability sudah diperbaiki tapi tidak memiliki bukti bahwa ada vendor yang sebenarnya telah mengeksploitasi vulnerability ini untuk memenangkan kontrak secara tidak fair.",
        "options": [
            "Lakukan audit forensik untuk mencari bukti apakah vulnerability benar-benar dieksploitasi, dan jika ditemukan bukti proses semua kontrak yang affected sesuai hukum yang berlaku",
            "Amankan vulnerability dan pertimbangkan selesai karena tidak ada bukti eksploitasi dan audit forensik akan memakan biaya dan waktu besar",
            "Publikasikan vulnerability yang sudah ditemukan dan diperbaiki sebagai transparansi kepada publik tentang security sistem yang digunakan pemerintah",
            "Laporkan ke police karena eksploitasi vulnerability dalam e-procurement adalah tindak pidana meskipun tidak ada bukti bahwa hal tersebut benar-benar terjadi",
            "Ceritakan kepada vendor-vendor tentang vulnerability yang sudah diperbaiki agar mereka tenang bahwa proses procurement sekarang sudah aman"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan pendekatan yang bertanggung jawab: tidak mengabaikan risiko bahwa vulnerability mungkin telah dieksploitasi tapi juga tidak langsung menuduh tanpa bukti. Audit forensik memberikan basis untuk action yang proportionate terhadap apa yang ditemukan.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_011", "questionId": "twk3_011", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah pemimpin partai politik yang sedang proses rekonsiliasi dengan elit-elit dari era Orde Baru yang sebelumnya dikritik karena berbagai penyimpangan. Menerima mereka kembali akan memberikan dukungan finansial dan infrastruktur politik yang sangat dibutuhkan untuk memenangkan pemilu. Namun bases supporter partai Anda yang sebagian adalah korban atau keturunan korban dari penyimpangan era tersebut dengan keras menolak rekonsiliasi ini.",
        "options": [
            "Terima rekonsiliasi karena politik adalah tentang coalition building dan masa lalu tidak bisa diubah: yang penting adalah masa depan",
            "Tolak rekonsiliasi karena nilai-nilai partai tidak bisa dikompromikan untuk alasan elektoral dan supporter yang setia harus dihargai dengan tidak berkompromi pada prinsip",
            "Terima rekonsiliasi tapi dengan persyaratan yang jelas: transparansi tentang penyimpangan masa lalu, pemulihan nama baik korban, dan komitmen bahwa penyimpangan tidak akan terulang, dengan monitoring system yang kuat",
            "Serahkan keputusan kepada seluruh members partai melalui voting karena ini adalah keputusan fundamental tentang identitas partai yang harus melibatkan semua stakeholders",
            "Tunda rekonsiliasi sampai setelah pemilu karena membuka luka lama sekarang akan mengganggu fokus partai pada victory elektoral"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan sophisticated political judgment: tidak blindly accepting maupun rejecting tapi menggunakan posisi leverage untuk добиться justice. Persyaratan transparansi, pemulihan korban, dan monitoring adalah cara untuk melakukan rekonsiliasi yang tidak mengorbankan prinsip.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_012", "questionId": "twk3_012", "category": "TWK",
        "subcategory": "Integritas",
        "questionText": "Anda adalah hakim yang preside dalam sidang korupsi besar. Terdakwa adalah pengusaha kaya yang jelas-jelas bersalah berdasarkan semua bukti. Namun jika menghukum penuh sesuai undang-undang, perusahaan milik terdakwa yang merupakan employer terbesar di daerah Anda akan bangkrut dan ribuan warga akan kehilangan pekerjaan. Jika membebaskan Terdakwa, Anda merusak integritas sistem hukum dan memberikan message bahwa korupsi bisa dibebaskan dengan konsekuensi ekonomi.",
        "options": [
            "Hukum Terdakwa sesuai undang-undang karena rule of law tidak bisa dikompromikan dengan pertimbangan ekonomi dan ribuan pekerjaan bukan tanggung jawab seorang hakim",
            "Bebaskan Terdakwa karena menghukum pengusaha yang salah bukan решение yang bijaksana jika konsekuensinya adalah ribuan pengangguran",
            "Hukum Terdakwa dengan hukuman percobaan dan denda yang besar, dengan kondisi bahwa operasi perusahaan tetap berjalan dan jobs dipertahankan, sebagai bentuk restorative justice",
            "Minta penundaan persidangan dan kirimkan rekomendasi kepada eksekutif untuk menyelamatkan perusahaan melalui bailout atau restructuring sebelum memutus",
            "Lakukan putus sesuai hukum tapi sampaikan secara terbuka bahwa konsekuensi ekonomi adalah tanggung jawab bersama yang harus diaddress oleh pemerintah dan masyarakat, bukan hanya akibat dari putusan суд"
        ],
        "answer": "E",
        "explanation": "Opsi E menunjukkan judicial integrity yang highest: menghukum sesuai hukum tanpa compromise, namun secara jujur acknowledge dan articulate konsekuensi sistemik dari putusan. Ini bukan menghindari tanggung jawab tapi mendelegasikan konsekuensi ekonomi kepada branch yang tepat - eksekutif dan legislativo - sambil mempertahankan prinsip bahwa keadilan tidak bisa diukur dengan uang.",
        "difficulty": "hard"
    },
    # === BELA NEGARA (6) ===
    {
        "id": "twk3_013", "questionId": "twk3_013", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Negara tetangga mempermasalahkan batas wilayah laut di kawasan yang rich dengan sumber daya ikan dan possible hydrocarbon deposits. Negara tetangga mengklaim berdasarkan interpretasi historis yang berbeda sementara Indonesia klaim berdasarkan UNCLOS 1982 yang sudah diratifikasi kedua negara. Masyarakatnelayan dari kedua negara sudah puluhan tahun menangkap ikan di waters tersebut dan memiliki traditional fishing rights yang diakui secara adat.",
        "options": [
            "Kompromikan klaim berdasarkan UNCLOS demi perdamaian dan stability regional dengan membagi zona berdasarkan historical fishing patterns yang sudah berlangsung puluhan tahun",
            "Gunakan full military force untuk mempertahankan klaim karena UNCLOS sudah jelas dan compromise adalah pengkhianatan terhadap kedaulatan",
            "Ajak negara tetangga ke meja negosiasi dengan mediator internasional, sampaikan posisi berdasarkan UNCLOS tapi tetap terbuka untuk решения yang mengakomodasi traditional fishing rights masyarakatnelayan kedua negara",
            "Serahkan решение kepada international court karena semua klaim berdasarkan hukum internasional dan kedua negara harus patuh pada keputusan court",
            "Lakukan joint development zone di mana kedua negara berbagi sumber daya tanpa menyelesaikan sengketa klaim terlebih dahulu, sambil tetap mempertahankan posisi klaim masing-masing secara resmi"
        ],
        "answer": "E",
        "explanation": "Opsi E menunjukkan pragmatic maritime diplomacy: tidak menyelesaikan sengketa yang bisa memakan decade tapi mulai menghasilkan manfaat bersama bagi masyarakat yang sudah bergantung pada waters tersebut selama generations. Joint development adalah langkah yang recognize both kedaulatan dan realitas pragmatis.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_014", "questionId": "twk3_014", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Sebuah grup teroris internasional menyatakan niat untuk menyerang fasilitas strategis Indonesia. Inteligensia Anda menunjukkan mereka memiliki kapasitas untuk executes attack tapi belum tentu memiliki motivasi yang kuat unless mereka bisa mendapat publicity yang besar dari serangan tersebut. Di saat bersamaan media sedang menunggu untuk mengeksposiberita tentang kelemahan keamanan infrastruktur kritis Indonesia sebagai bagian dari investigasi journalism yang legitimate.",
        "options": [
            "Batasi sementara semua reporting tentang infrastruktur kritis di media karena tidak ada keamanan yang bisa dijamin jika informasi tentang kelemahan terus dipublikasikan secara terbuka",
            "Koordinasikan dengan media untuk menunda publikasi tertentu sampai situasi keamanan membaik, namun sampaikan dasar reasoning-nya tanpa memaksa media untuk服从",
            "Tidak mengambil tindakan apapun terhadap media karena kebebasan pers adalah prinsip yang tidak bisa dikompromikan bahkan dalam situasi ancaman terror",
            "Bagikan semua informasi tentang ancaman terror kepada publik secara lengkap agar masyarakat bisa vigilance dan ikut membantu menjaga keamanan",
            "Tingkatkan security di semua fasilitas kritis berdasarkan threat intelligence yang ada tanpa mengubah kebijakan media sama sekali"
        ],
        "answer": "E",
        "explanation": "Opsi E menunjukkan bahwa langkah keamanan yang responsible tidak harus mengorbankan kebebasan pers. Inteligensia tentang ancaman digunakan untuk security upgrade, sementara pers memiliki kebebasan untuk memberitakan apa yang menjadi interesse publik. Keduanya tidak harus saling konflik.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_015", "questionId": "twk3_015", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Indonesia ditawari bergabung dalam aliansi keamanan baru yang предложила protection kuat terhadap ancaman external. Keikutsertaan означает bahwa Indonesia harus mengurangi konsultasi dan koordinasi dengan beberapa negara lain yang saat ini menjadi mitra strategis. Beberapa mitra ini adalah negara yang memiliki hubungan baik dengan China maupun AS sekaligus dan posisinya sebagai mediator telah memberikan Indonesia leverage diplomatik yang signifikan.",
        "options": [
            "Terima keikutsertaan dalam aliansi karena perlindungan terhadap ancaman eksternal adalah prioritas utama dan investasi dalam keamanan adalah keharusan",
            "Tolak keikutsertaan karena posisi mediator dan koneksi dengan semua блоки adalah aset strategis yang tidak bisa dikompromikan untuk perlindungan yang mungkin tidak diperlukan",
            "Negosiasikan статус asosiasi而非keanggotaan penuh dalam aliansi sehingga可以获得 beberapa manfaat perlindungan tanpa harus memilih сторона secara tegas",
            "Lakukan national security review terlebih dahulu dengan melibatkan semua stakeholders sebelum mengambil keputusan karena implicaasi dari keputusan ini terlalu besar untuk diambil sendiri oleh siapapun",
            "Ajukan referendum kepada rakyat karena bergabung dalam aliansi militer adalah keputusan yang mengubah posisi strategis Indonesia secara fundamental dan harus melibatkan suara rakyat"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan sophisticated strategic thinking: tidak menerima atau menolak secara binary tapi mencari posisi yang memberikan manfaat maksimal dengan biaya minimal. Associated status adalah middle ground yang pragmatic dan sering digunakan oleh negara yang tidak ingin dipaksa memilih sides dalam конфликт superpower.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_016", "questionId": "twk3_016", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Rencana wajib militer untuk semua warga negara dipertimbangkan kembali. Pihak militer mendukung karena dianggap penting untuk membangun semangat bela negara dan pertahanan nasional. Pihak sosial dan ekonomi mengeritik karena akan mengeluarkan young people dari sistem pendidikan dan ekonomi selama 1-2 tahun. Budget yang diperlukan juga sangat besar.",
        "options": [
            "Implementasikan wajib militer penuh sesuai permintaan militer karena bela negara adalah tanggung jawab setiap warga negara dan manfaat jangka panjang lebih besar dari biaya jangka pendek",
            "Tolak wajib militer karena biaya dan dampak sosial ekonomi terlalu besar dan军队 bisa direkrut melalui jalur voluntary yang sudah memadai",
            "Buat program wajib militer yang terdiferensiasi: untuk yang sudah memiliki keahlian tertentu bisa melakukan pengabdian dalam bentuk lain seperti disaster response atau community service, sementara untuk others bisa dilakukan dalam bentuk lebih pendek",
            "Lakukan пилотный проект wajib militer di beberapa daerah terlebih dahulu untuk mengevaluasi efektivitas dan dampak sebelum implementasi nasional",
            "Serahkan keputusan kepada generasi muda melalui survei nasional karena merekalah yang paling affected oleh kebijakan ini"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan kebijakan yang sophisticated: mendukung principle bela negara tapi dengan implementation yang pragmatic dan tidak one-size-fits-all. Differentiated approach mengakui bahwa bela negara bisa expressed dalam banyak bentuk beyond military service. Ini tidak mengurangi semangat pertahanan tapi memaksimalkan efisiensi dari ресурсов.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_017", "questionId": "twk3_017", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Sebuah perusahaan teknologi asing ingin membangun data center besar di Indonesia untuk menyimpan data warga negara Indonesia. Keuntungan ekonomi signifikan dan ribuan lapangan kerja diciptakan. Namun ada kekhawatiran bahwa data warga Indonesia akan disimpan di luar kendali penuh regulator Indonesia dan bisa menjadi инструмент espionage oleh negara asal perusahaan tersebut.",
        "options": [
            "Izinkan dengan persyaratan bahwa semua data harus disimpan di servers located di Indonesia dan subject к законодательству Indonesia dengan enforcement yang kuat",
            "Tolak sepenuhnya karena risiko espionage terlalu besar dan tidak ada amount экономической выгоды yang bisa justify pengkhianatan data warga negara",
            "Izinkan dengan persyaratan data localization tapi juga minta perusahaan memberikan source code access kepada regulator Indonesia untuk audit independen secara berkala",
            "Minta perusahaan menjadi joint venture dengan perusahaan Indonesia sehingga ada representation Indonesia dalam governance of data center",
            "Buat тендер terbuka untuk multiple perusahaan termasuk иностранные и domestic untuk data center, dan pilih berdasarkan hasil evaluasi security dan ekonomi"
        ],
        "answer": "E",
        "explanation": "Opsi E menunjukkan bahwa competitive procurement adalah kunci untuk mendapatkan deal yang terbaik bagi negara: не выбирая automatically domestic atau foreign tapi membandingkan всех претендентов berdasarkan objective criteria. тендер terbuka juga menghindari обвинения в коррупции и протекционизме.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_018", "questionId": "twk3_018", "category": "TWK",
        "subcategory": "Bela Negara",
        "questionText": "Beberapa wilayah perbatasan Indonesia mengalami проблема identitas karena warga di perbatasan hidup dalam ekonomi borderless di mana mereka melintasi batas setiap hari untuk bekerja, belajar, dan mengakses layanan kesehatan. Beberapa dari mereka memiliki status sebagai warga negara Indonesia tapi secara faktual hidup lebih banyak di luar negeri. Kondisi ini menciptakan tantangan untuk bela negara karena loyality mereka dipertanyakan oleh beberapa kelompok di masyarakat.",
        "options": [
            "Berlakukan secara tegas bahwa warga negara Indonesia di perbatasan harus tinggal di Indonesia untuk mempertahankan hak pilih dan akses layanan publik mereka",
            "Buat kebijakan khusus untuk zona perbatasan yang mengakui realitas ekonomi cross-border sambil tetap mempertahankan статус kewarganegaraan Indonesia dan hak-haknya",
            "Larang warga perbatasan bekerja di luar negeri karena mereka adalah warga negara Indonesia dan seharusnya mengabdi kepada bangsa mereka sendiri",
            "Biarkan saja karena kondisi perbatasan yang kompleks sudah berlangsung generations dan tidak perlu diubah dengan kebijakan baru",
            "Lakukan program возвращение yang memberikan incentives bagi warga perbatasan untuk lebih banyak tinggal dan berkontribusi di Indonesia"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan humanitarian approach yang juga patriotic: mengakui realitas ekonomi perbatasan yang sudah berlangsung generations tanpa mengorbankan prinsip kewarganegaraan. Zona perbatasan khusus dengan hak penuh sebagai warga negara tapi pengakuan praktik cross-border ekonomi adalah solusi yang pragmatic dan tidak diskriminatif.",
        "difficulty": "hard"
    },
    # === PILAR NEGARA (6) ===
    {
        "id": "twk3_019", "questionId": "twk3_019", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "Mahkamah Konstitusi harus memutus perkara yang sangat krusial: apakah undang-undang yang memberikan wewenang kepada pemerintah untuk membatasi kebebasan bergerak selama keadaan darurat adalah konstitusional atau tidak. Undang-undang ini diterapkan selama pandemi dan terbukti effective dalam membatasi penyebaran penyakit tapi juga berpotensi disalahgunakan untuk membatasi hak демократических граждан di masa depan. Para hakim memiliki pandangan sangat terbagi tentang masalah ini.",
        "options": [
            "Nyatakan undang-undang inkonstitusional karena kebebasan bergerak adalah hak dasar yang tidak bisa dibatasi даже dengan alasan darurat sekalipun",
            "Nyatakan undang-undang konstitusional karena pemerintah perlu memiliki инструменты untuk menangani keadaan darurat dan demokrasi harus memiliki checks and balances terhadap kekuasaan darurat",
            "Nyatakan undang-undang konstitusional dengan условие bahwa harus ada independent oversight mechanism yang ketat dan time limit yang jelas untuk применения, sebagai judicial legislation yang dibutuhkan untuk make undang-undang workable without becoming инструмент abuse",
            "Tunda putusan sampai keadaan darurat selesai karena tidak etis memutuskan tentang hak during emergency ketika kita sendiri berada dalam keadaan darurat",
            "Serahkan keputusan kepada publik melalui referendum karena masalah ini terlalu fundamental untuk diputuskan oleh 9 orang hakim saja"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan constitutional adjudication yang sophisticated: tidak naively striking down maupun upholding tapi menggunakan judicial review power untuk menambahkan structural safeguards yang membuat undang-undang work for its legitimate purpose without becoming a tool of abuse. Это adalah judicial statesmanship yang sesuai dengan peran MK sebagai penjaga конституции.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_020", "questionId": "twk3_020", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "Sebuah proyek besar pembangunan ibu kota baru berada dalam bahaya besar: kontraktor utama telah bangkrut dan tidak mampu melanjutkan pekerjaan, sementara investasi sudah dilakukan sangat besar dan waktu sangat terbatas. Kontrak initial sudah memiliki ketentuan tentang default namun menerapkan ketentuan tersebut akan означать proyek berhenti total dan kerugian besar bagi negara. Beberapa kontraktor lain sudah menyatakan minat untuk mengambil alih tapi dengan kondisi yang berbeda secara signifikan dari kontrak awal.",
        "options": [
            "Terapkan ketentuan default secara penuh karena kontrak adalah hukum dan tidak ada exception untuk proyek besar: jika tidak ada consequences untuk default, maka seluruh system procurement akan rusak",
            "Renegosiasi kontrak dengan kontraktor bangkrut untuk menemukan solusi yang memungkinkan proyek tetap berjalan dengan terms yang revised",
            "Batalkan proyek total dan gunakan dana yang sudah dikeluarkan sebagai lessons learned karena melanjutkan proyek dalam kondisi tidak sehat adalah recipe untuk bencana",
            "Lakukan тендер cepat untuk kontraktor pengganti dengan conditions yang sudah revised namun tetap competitive dan transparan",
            "Minta kontraktor pengganti mengambil alih dengan subsidi negara karena melindungi pekerja dan melanjutkan pembangunan adalah lebih penting dari prinsip контрактный"
        ],
        "answer": "D",
        "explanation": "Opsi D menunjukkan balanced approach: mengakui bahwa default dalam kontrak besar punya konsekuensi sistemik yang serius, tapi tidak mau memaksa solusi yang mungkin коррумпированный pada situasi krisis. тендер cepat yang tetap transparan dan competitive adalah middle ground yang recognize both principle и pragmatism.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_021", "questionId": "twk3_021", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "Kehutanan Indonesia sedang dalam krisis: deforestation mencapai angka yang mengkhawatirkan despite regulasi yang sudah ada. Riset menunjukkan bahwa sebagian besar deforestation dilakukan oleh perusahaan-perusahaan besar yang memiliki izin resmi dari pemerintah daerah dengan persetujuan dari pemerintah pusat. Beberapa из них bahkan telah дисквалифицирован oleh central government tapi izin daerah mereka tetap berlaku karena ambiguitas antara tingkat pemerintahan.",
        "options": [
            "Berikan wewenang penuh kepada центральное правительство untuk membatalkan semua izin yang bertentangan, tanpa perlu persetujuan daerah, karena krisis iklim adalah isu nasional",
            "Strengthen kapasitas daerah untuk melakukan enforcement tapi dengan monitoring system dari pusat",
            "Buat commission независимый yang memiliki wewenang untuk menyelidiki dan membatalkan izin yang bermasalah tanpa memandang tingkat pemerintahan yang mengeluarkan",
            "Tingkatkan punishment untuk deforestation menjadi sangat berat termasuk pidana penjara panjang dan denda yang sangat besar untuk perusahaan yang terlibat",
            "Serahkan seluruh hutan kepada masyarakat adat karena merekalah yang paling memiliki insentif untuk melestarikan hutan tempat mereka hidup selama generations"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan structural solution terhadap masalah sistemik: tidak menyalahkan satu tingkat pemerintahan atau yang lain tapi menciptakan mekanisme independen yang bisa跨立 уровни pemerintahan untuk menangani masalah yang jelas-jelas sistemный. Институциональный решение yang tidak bisa дискредитирован oleh political interests.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_022", "questionId": "twk3_022", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "UNESCO memberikan tantangan kepada Indonesia: mengembangkan program pelestarian budaya yang akan dinilai secara internasional sebagai kondisi untuk memberikan статус warisan dunia kepada beberapa situs budaya Indonesia. Program tersebut memerlukan resources besar dan berpotensi mengubah cara masyarakat adat hidup dalam situs tersebut. Beberapa из них sangat bergantung pada praktik tradisional yang mungkin tidakсовместим dengan modernisasi yang diperlukan untuk memenuhi standar UNESCO.",
        "options": [
            "Terima tantangan UNESCO dengan penuh dan alokasikan resources yang diperlukan untuk memenuhi semua standar internasional tanpa compromise",
            "Tolak untuk participate dalam program UNESCO karena standar internasional tidak selalu sesuai dengan realitas budaya Indonesia dan tidak ada who are we untuk judge how Indonesians should preserve their own budaya",
            "Participate tapi dengan negosiasi untuk mendapatkan exception untuk praktik budaya tertentu yang tidak bisa dimodernisasi tanpa kehilangan esensinya",
            "Lakukan dialog dengan masyarakat adat yang affected dan kembangkan program pelestarian yang menggabungkan international standards dengan vision mereka sendiri tentang bagaimana budaya mereka harus dilestarikan",
            "Accept program UNESCO tapi dengan reservasi bahwa beberapa aspek dari program akan diimplementasikan secara gradual dalam timeline yang tidak mengorbankan kesejahteraan masyarakat adat"
        ],
        "answer": "D",
        "explanation": "Opsi D menunjukkan participatory approach yang paling sesuai dengan semangat pelestarian budaya: masyarakat adat adalah experts tentang budaya mereka sendiri dan siapapun harus menjadi keputusan akhir tentang bagaimana warisan mereka harus dilestarikan. Kombinasi international standards dengan local vision adalah collaborative preservation yang paling efektif dan berkelanjutan.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_023", "questionId": "twk3_023", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "Pengadilan agama dan pengadilan umum memiliki dispute yurisdiksi yang sudah berlangsung lama. Pasangan campuran agama yang bercerai harus menghadapi persidangan di kedua pengadilan untuk menyelesaikan berbagai aspek dari perceraian mereka. Hasilnya tidak konsisten dan seringkali tidak adil bagi salah satu pihak karena each court memiliki pendekatan yang berbeda dan tidak saling terkait.",
        "options": [
            "Buat satu unified court system yang menangani semua perkara termasuk agama untuk menghindari inconsistensi dan memastikan keseragaman keadilan",
            "Pertahankan dual system tapi dengan mekanisme koordinasi yang kuat antara pengadilan agama dan umum untuk menghindari conflicting rulings",
            "Pindahkan semua perkara perceraian ke pengadilan umum dengan hakim yang memiliki pelatihan agama untuk memastikan perspektif agama tetap hadir",
            "Biarkan saja karena perbedaan yurisdiksi antara pengadilan agama dan umum adalah cerminan dari pengakuan terhadap pluralitas Indonesia dan seharusnya tidak diubah",
            "Buat specialized court untuk perkara yang melibatkan berbagai yurisdiksi dengan hakim dari berbagai latar belakang yang diperlukan"
        ],
        "answer": "E",
        "explanation": "Opsi E menunjukkan innovative approach: tidak menerima dualism atau unified system sebagai only options tapi menciptakan mekanisme yang recognize complexity dari legal landscape Indonesia. Specialized court dengan diverse judges adalah solusi yang respects pluralism sambil mengatasi конфликт yurisdiksi yang menyebabkan ketidakadilan.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_024", "questionId": "twk3_024", "category": "TWK",
        "subcategory": "Pilar Negara",
        "questionText": "Undang-undang baru tentang desentralisasi memberikan lebih banyak wewenang kepada daerah tapi pada saat yang sama banyak daerah tidak memiliki kapasitas untuk menggunakan wewenang baru tersebut secara efektif. Beberapa daerah besar sudah siap tapi banyak daerah kecil justru merasa overwhelmed dengan tanggung jawab baru. Beberapa都开始 melakukan penyimpangan karena lack of capacity untuk menjalankan fungsi baru.",
        "options": [
            "Peroleh wewenang kembali ke pusat karena desentralisasi tidak bekerja dan banyak daerah tidak могут handle tanggung jawab yang diberikan",
            "Pertahankan desentralisasi tapi dengan massive capacity building program yang membantu daerah yang tertinggal tanpa mengurangi wewenang yang sudah diberikan",
            "Diferensiasikan tingkat desentralisasi berdasarkan kapasitas daerah: daerah yang lebih mampu mendapat wewenang lebih besar, yang belum mampu mendapat more support dan mentoring",
            "Buat mekanisme sharing resources antara daerah yang lebih mampu dan yang kurang mampu sehingga semua bisa benefit dari desentralisasi",
            "Tunda implementasi sampai semua daerah bisa menunjukkan kapasitas yang memadai melalui independent assessment"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan nuanced understanding dari federalism yang berbeda: tidak all-or-nothing antara централизация dan desentralisasi penuh. Diferensiasi berdasarkan kapasitas daerah adalah evidence-based approach yang mengakui realitas berbeda di seluruh wilayah Indonesia tanpa mengurangi prinsip desentralisasi.",
        "difficulty": "hard"
    },
    # === BAHASA INDONESIA (6) ===
    {
        "id": "twk3_025", "questionId": "twk3_025", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Sebuah ministry ingin издать pedoman penulisan resmi yang mewajibkan penggunaan bahasa Indonesia baku dalam semua dokumen resmi pemerintah. Kritikus berpendapat bahwa требование ini akan menghambat komunikasi terutama dalam konteks teknis dan ilmiah di mana banyak istilah tidak ada padanan dalam bahasa Indonesia. Sebagian warga negara Indonesia lebih nyaman berkomunikasi dalam bahasa daerah atau bahasa Inggris dalam konteks profesional tertentu.",
        "options": [
            "Terapkan mandatory penggunaan bahasa Indonesia baku dalam semua dokumen resmi karena ini adalah kewajiban konstitusional yang harus ditegakkan tanpa pengecualian",
            "Izinkan penggunaan bahasa Inggris atau bahasa daerah dalam dokumen resmi untuk konteks teknis dan ilmiah dengan terjemahan bahasa Indonesia yang acompañan sebagai lampiran",
            "Buat daftar istilah teknis yang sudah memiliki padanan bahasa Indonesia baku dan wajib gunakan padanan tersebut, namun untuk istilah yang belum ada padanan, izin penggunaan bahasa asing dengan italicisasi",
            "Lakukan kongres bahasa terlebih dahulu untuk menetapkan padanan istilah teknis dalam bahasa Indonesia sebelum menerapkan mandatory rule",
            "Serahkan keputusan kepada Akademi Bahasa Indonesia karena merekalah yang paling kompeten untuk menentukan kebijakan bahasa yang tepat"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pragmatisme linguistik: tidak blindly insisting on bahasa Indonesia tanpa recognition untuk realitas bahwa banyak istilah teknis tidak memiliki padanan yang established, tapi juga tidak abandoning effort untuk mengembangkan bahasa Indonesia baku. Pendekatan bertahap berbasis daftar istilah spesifik lebih workable dan efektif.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_026", "questionId": "twk3_026", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Peraturan baru melarang penggunaan bahasa gaul dan slang dalam dokumen resmi pemerintahan dan media massa. Pendukung peraturan ini berpendapat bahwa bahasa Indonesia sedang terancam oleh terlalu banyak masuknya bahasa gaul yang tidak baku. Kritikus berpendapat bahwa bahasa adalah entitas organik yang terus berevolusi dan tidak bisa diatur melalui regulasi.",
        "options": [
            "Dukung peraturan tersebut karena pelestarian bahasa Indonesia baku adalah keharusan dan tanpa enforcement melalui regulasi, bahasa akan corrupted beyond repair",
            "Tolak peraturan tersebut karena bahasa tidak bisa diatur melalui hukum dan upaya-upayaan sebelumnya untuk mengatur bahasa everywhere selalu gagal",
            "Buat program yang mendorong penggunaan bahasa Indonesia baku melalui incentive dan awards, bukan melalui pelarangan",
            "Buat diferensiasi: dalam dokumen resmi dan media massa terapkan standar bahasa baku, namun untuk konteks tidak-formal biarkan bahasa berkembang secara alami",
            "Lakukan riset terlebih dahulu untuk menentukan apakah bahasa Indonesia benar-benar terancam oleh bahasa gaul atau ini adalah overreaction belaka"
        ],
        "answer": "D",
        "explanation": "Opsi D menunjukkan realistic approach towards language policy: membedakan antara konteks formal dan informal adalah hal yang wajar. Bahasa baku perlu di-maintain dalam konteks resmi tapi bahasa organik harus bisa berkembang dalam konteks tidak resmi. One-size-fits-all prohibition tidak pernah efektif dalam kebijakan bahasa.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_027", "questionId": "twk3_027", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Sebuah surat resmi dari government agency harus disampaikan kepada publik. Draft sudah ditulis dengan bahasa Indonesia yang benar secara tata bahasa namun sulit dipahami oleh masyarakat umum karena terlalu formal dan menggunakan banyak kalimat pasif yang berbelit-belit. Versi yang lebih sederhana dan langsung akan lebih mudah dipahami tapi mungkin dianggap kurang formal.",
        "options": [
            "Gunakan versi formal dan sulit dipahami karena dokumen resmi harus mengikuti standar bahasa Indonesia baku dan tidak boleh mengorbankan formalitas demi aksesibilitas",
            "Gunakan versi sederhana yang mudah dipahami karena tujuan utama komunikasi publik adalah transfer informasi yang efektif dan tidak ada gunanya dokumen yang formally correct tapi tidak bisa dipahami",
            "Buat dua versi: satu versi formal untuk arsip resmi dan satu versi sederhana untuk publik, dengan catatan bahwa keduanya menyampaikan informasi yang sama",
            "Buat versi hybrid yang mempertahankan bahasa baku tapi menulis dalam kalimat yang lebih aktif dan langsung sehingga accessible namun tetap mengikuti standar bahasa Indonesia yang baik",
            "Minta feedback dari target audience tentang versi mana yang mereka preferensikan sebelum memutuskan"
        ],
        "answer": "D",
        "explanation": "Opsi D menunjukkan bahwa formalitas dan aksesibilitas tidak harus saling исключать: bahasa baku bisa ditulis dalam kalimat aktif yang langsung tanpa mengorbankan tata bahasa yang benar. Versi hybrid memungkinkan pemerintah untuk tetap menjaga standards sambil memastikan komunikasi efektif dengan masyarakat.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_028", "questionId": "twk3_028", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Karya sastra Indonesia harus diterjemahkan ke bahasa Inggris untuk dipublikasikan secara internasional. Dua pendekatan sedang diperdebatkan: pertama memprioritaskan terjemahan literal yang faithfully reproduces teks Indonesia termasuk struktur tata bahasanya dan referensi budaya dengan catatan kaki. Kedua memprioritaskan dampak emosional dan budaya, mengadaptasi teks untuk beresonansi dengan pembaca berbahasa Inggris meskipun ini berarti menyimpang dari teks asli Indonesia.",
        "options": [
            "Prioritaskan terjemahan literal karena karya sastra Indonesia harus dipresented apa adanya dalam bahasa aslinya, dan pembaca internasional harus menghargai karya tersebut apa adanya",
            "Prioritaskan terjemahan adaptif karena tujuannya adalah menyampaikan pengalaman dan emosi Indonesia kepada pembaca internasional, dan jika terjemahan literal gagal melakukan ini maka terjemahan gagal dalam tujuannya",
            "Pilih pendekatan middle ground yang melakukan adaptasi untuk элементы yang clearly untranslatable secara literal namun tetap mempertahankan как bisa lebih banyak dari struktur dan gaya bahasa Indonesia",
            "Serahkan kepada penulis karya tersebut untuk memutuskan karena merekalah yang paling memahami nuansa dari karya mereka sendiri",
            "Buat dua terjemahan terpisah: satu untuk academic audience yang menghargai literalness, satu untuk general audience yang menghargai aksesibilitas"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pendekatan balanced dalam terjemahan sastra: acknowledge bahwa some aspects of language are untranslatable and require adaptation, while others should be preserved. Neither pure literalism nor complete adaptation is optimal. A nuanced approach that prioritizes emotional and cultural authenticity while maintaining as much of the original structure as possible serves both fidelity and impact.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_029", "questionId": "twk3_029", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Dalam dunia yang globalized, penggunaan bahasa Inggris sebagai lingua franca dalam akademia dan bisnis internasional sudah menjadi standar. Banyak universities Indonesia yang mengajarkan matakuliah dalam bahasa Inggris untuk meningkatkan global competitiveness. Kritikus berpendapat bahwa ini berkontribusi pada erosi bahasa Indonesia sebagai bahasa ilmu pengetahuan karena rekaman sejarah menunjukkan bahwa bahasa bisa berkembang hanya melalui penggunaan aktif dalam ranah intelektual.",
        "options": [
            "Taati penuh aturan penggunaan bahasa Indonesia karena ini adalah implementasi dari kebijakan yang sudah disepakati dan tidak ada ruang untuk discretion pribadi dalam这种事情",
            "Gunakan bahasa Inggris karena efektivitas komunikasi dalam konteks technical training adalah prioritas utama dan bahasa Indonesia yang belum memiliki terminology yang developed bisa menghambat pembelajaran",
            "Gunakan bahasa Indonesia dengan menyisipkan istilah teknis dalam bahasa Inggris sebagai bridge sampai terminology Indonesia berkembang, namun jelaskan bahwa penggunaan Inggris bersifat временны dan akan digantikan ketika padanan Indonesia sudah tersedia",
            "Предложите руководству agar melakukan evaluasi terhadap efektivitas kebijakan ini dengan membandingkan performancepeserta dalam kedua bahasa sebelum memutuskan pendekatan mana yang lebih baik",
            "Jangan mengambil tindakan apapun dan ikuti arus karena masalah ini terlalu kecil untuk perhatian Anda dan terlalu kompleks untuk dipecahkan secara individual"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pragmatic approach yang linguistically sensitive: tidak menolak penggunaan bahasa Inggris yang masih diperlukan, tidak juga abandon bahasa Indonesia, tapi menggunakannya sebagai bridge dengan acknowledgment bahwa solusi bersifat временны. Pendekatan ini memungkinkan pembelajaran efektif sambil tetap membangun kapasitas bahasa Indonesia.",
        "difficulty": "hard"
    },
    {
        "id": "twk3_030", "questionId": "twk3_030", "category": "TWK",
        "subcategory": "Bahasa Indonesia",
        "questionText": "Bahasa daerah semakin jarang digunakan oleh generasi muda dan beberapa sudah mulai классифицировать sebagai endangered languages. Beberapa pihak menyerukan intervensi pemerintah untuk melestarikan bahasa daerah melalui программы pendidikan formal. Pihak lain menganggap bahwa bahasa daerah adalah heritage yang should be preserved voluntarily oleh community speakers, bukan melalui program top-down dari pemerintah.",
        "options": [
            "Implementasikan программа pelestarian bahasa daerah melalui kurikulum pendidikan formal karena language death adalah kehilangan budaya yang tidak bisa diabaikan dan intervensi diperlukan sebelum terlambat",
            "Hormati pilihan masyarakat untuk tidak menggunakan bahasa daerah dan biarkan proses natural terjadi: jika masyarakat tidak mau menggunakan bahasa mereka sendiri, tidak ada yang bisa memaksa",
            "Buat программа pelestarian yang berkolaborasi dengan masyarakat adat sebagai partners bukan sebagai subjects, dengan funding dan resources dari pemerintah namun content dan approach ditentukan oleh masyarakat sendiri",
            "Fokuskan resources pada dokumentasi dan архивирование bahasa daerah yang sudah hampir punah melalui linguists dan teknologis, tanpa mencoba untuk menghidupkan kembali penggunaan aktif yang masyarakatnya sendiri sudah tidak berminat",
            "Integrasikan bahasa daerah sebagai mata pelajaran optional di sekolah daerah tersebut dengan guru dari komunitas lokal yang dibayar oleh pemerintah"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan decolonized approach towards language preservation: masyarakat adat sebagai partners dengan agency penuh, bukan sebagai subjects dari program government. Pendekatan ini lebih berkelanjutan karena ownership atas program ada pada masyarakat sendiri. Funding dari pemerintah menyediakan resources tanpa menciptakan dependency atau imposing внешний agenda.",
        "difficulty": "hard"
    },
]

# Validate ASCII
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

print(f"Total: {len(questions)}, Non-ASCII: {bad}")

with open('assets/questions/twk_3.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Written successfully")