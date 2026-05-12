import json, os

# ============================================================
# TWK PAKET 3 - 30 soal
# ============================================================
twk3 = [
  # NASIONALISME (6)
  {
    "id": "twk3_001", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Peristiwa Pertempuran 10 November 1945 di Surabaya merupakan perlawanan heroik rakyat Indonesia terhadap pasukan Inggris yang telah mendarat di kota tersebut setelah Jepang menyerah. Peristiwa ini melibatkan tokoh utama bernama...",
    "options": ["Soekarno", "Mohammad Hatta", "Jenderal Soedirman", "Bung Tomo", "Sutan Sjahrir"],
    "answer": "D",
    "explanation": "Pertempuran 10 November 1945 di Surabaya melibatkan tokoh utama Bung Tomo yang号召 rakyat untuk melawan pasukan Inggris. Peristiwa ini menjadi simbol keberanian rakyat Indonesia dalam mempertahankan kemerdekaan.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_002", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Sumpah Pemuda 28 Oktober 1928 menjadi tonggak sejarah pergerakan nasional Indonesia karena pada peristiwa tersebut para pemuda dari berbagai suku dan budaya...",
    "options": ["Mendeklarasikan kemerdekaan Indonesia secara resmi kepada dunia", "Menetapkan satu bahasa daerah sebagai bahasa pemersatu", "Mengikrarkan satu tanah air, satu bangsa, dan satu bahasa", "Membentuk organisasi kepemudaan bernama Pacto Sanguinis", "Menandatangani perjanjian dengan pemerintah kolonial Belanda"],
    "answer": "C",
    "explanation": "Sumpah Pemuda mengikrarkan satu tanah air Indonesia, satu bangsa Indonesia, dan satu bahasa Indonesia. Ikrar ini menjadi fondasi persatuan bangsa Indonesia dari Sabang sampai Merauke.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_003", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Politik luar negeri Indonesia yang bebas dan aktif berarti Indonesia...",
    "options": ["Bergabung dalam bloc kekuatan tertentu dan memihak salah satu negara adidaya", "Tidak memihak bloc kekuatan dunia mana pun dan aktif Foster kerja sama dengan semua negara", "Menolak seluruh bentuk kerja sama dengan negara asing", "Hanya bekerja sama dengan negara-negara bertetangga di Asia Tenggara", "Mengikuti sepenuhnya kebijakan luar negeri negara adidaya yang paling kuat"],
    "answer": "B",
    "explanation": "Politik luar negeri bebas dan aktif berarti Indonesia tidak memihak bloc kekuatan dunia mana pun, tetapi secara aktif Foster kerja sama dengan semua negara atas dasar penghormatan dan kesetaraan.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_004", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Perhatikan tabel berikut! (1) Mengutamakan kepentingan bangsa di atas kepentingan pribadi. (2) Menolak budaya asing secara total tanpa pengecualian. (3) Ikut serta dalam peringatan hari kemerdekaan. (4) Mempersatukan diri dengan semangat gotong royong. Sikap yang mencerminkan nasionalisme Indonesia yang sejati terdapat pada nomor...",
    "options": ["(1) dan (2)", "(1) dan (3)", "(1) dan (4)", "(2) dan (3)", "(3) dan (4)"],
    "answer": "C",
    "explanation": "Mengutamakan kepentingan bangsa di atas kepentingan pribadi (1) dan bersatu dengan semangat gotong royong (4) merupakan pengamalan nasionalisme sejati. Menolak budaya asing secara total (2) bukan sikap nasionalisme yang bijak.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_005", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Bangsa Indonesia memiliki pengalaman panjang dalam melawan penjajahan oleh bangsa asing. Pengalaman tersebut seharusnya menjadikan bangsa Indonesia...",
    "options": ["Menutup diri dari kerja sama internasional mana pun", "Semangat dalam membangun negara agar tidak pernah terjajah kembali", "Memusatkan seluruh sumber daya pada bidang militer saja", "Menghindari seluruh bentuk investasi asing", "Bersikap permusuhan terhadap seluruh orang asing"],
    "answer": "B",
    "explanation": "Pengalaman penjajahan yang panjang harus menjadi motivasi untuk terus membangun negara dengan semangat kebangsaan. Semangat nasionalisme sejati adalah keinginan kuat untuk kemajuan bangsa agar tidak pernah terjajah kembali.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_006", "category": "TWK", "subcategory": "Nasionalisme",
    "question": "Perhatikan tabel berikut! (1) Ikut serta dalam pembangunan sesuai kemampuan. (2) Menyebarkan kebencian terhadap kelompok tertentu. (3) Mengutamakan kepentingan daerah di atas kepentingan nasional. (4) Menjaga kerukunan dengan menghormati perbedaan. Yang bukan termasuk pengamalan semangat kebangsaan terdapat pada nomor...",
    "options": ["(1)", "(2)", "(3)", "(4)", "(1) dan (4)"],
    "answer": "B",
    "explanation": "Menyebarkan kebencian terhadap kelompok tertentu (2) bukan pengamalan semangat kebangsaan, melainkan tindakan yang memecah belah bangsa. Similarly, mengutamakan kepentingan daerah di atas nasional (3) juga bertentangan dengan semangat persatuan.",
    "difficulty": "easy"
  },
  # INTEGRITAS (6)
  {
    "id": "twk3_007", "category": "TWK", "subcategory": "Integritas",
    "question": "Penerapan integritas dalam kehidupan bernegara bermakna setiap warga negara...",
    "options": ["Wajib memberikan kesaksian di pengadilan meskipun tidak sesuai kenyataan", "Memberikan informasi yang benar kepada institusi negara dan tidak melakukan kecurangan dalam setiap urusan dengan pemerintah", "Bebas menyebarkan informasi tanpa memerdulikan kebenarannya", "Tidak perlu membayar pajak karena merupakan pilihannya", "Hanya jujur kepada keluarga dekat dan teman"],
    "answer": "B",
    "explanation": "Integritas dalam kehidupan bernegara berarti memberikan informasi yang benar kepada institusi negara dan tidak melakukan kecurangan, seperti membayar pajak dengan jujur dan menyampaikan data yang akurat.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_008", "category": "TWK", "subcategory": "Integritas",
    "question": "Pasal 27 ayat (1) UUD 1945 mengatur tentang...",
    "options": ["Hak setiap warga negara untuk berpendapat di muka umum", "Kewajiban setiap warga negara untuk mengikuti pendidikan dasar", "Setiap warga negara memiliki kedudukan yang sama di hadapan hukum dan pemerintahan", "Hak warga negara untuk mendapatkan jaminan sosial dari negara", "Kewajiban warga negara untuk membayar pajak dan retribusi"],
    "answer": "C",
    "explanation": "Pasal 27 ayat (1) UUD 1945 menyatakan bahwa setiap warga negara bersamaan kedudukannya di dalam hukum dan pemerintahan dan wajib menjunjung hukum dan pemerintahan itu dengan tidak ada kecualinya.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_009", "category": "TWK", "subcategory": "Integritas",
    "question": "Penyalahgunaan wewenang oleh pejabat publik yang memanfaatkan jabatannya untuk kepentingan pribadi merupakan pelanggaran terhadap...",
    "options": ["Hak asasi manusia warga negara", "Tanggung jawab moral dan hukum yang melekat pada jabatannya", "Kewajiban untuk selalu menghadiri acara resmi kedinasan", "Peraturan tentang jam kerja aparatur negara", "Etika profesi di luar bidang pemerintah"],
    "answer": "B",
    "explanation": "Penyalahgunaan wewenang merupakan pelanggaran terhadap tanggung jawab moral dan hukum yang melekat pada jabatan. Pejabat publik seharusnya menggunakan wewenangnya untuk kepentingan masyarakat, bukan untuk kepentingan pribadi.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_010", "category": "TWK", "subcategory": "Integritas",
    "question": "Budaya integritas dalam organisasi pemerintahan akan terbentuk apabila...",
    "options": ["Semua aturan dibuat secara ketat tanpa memberi kelonggaran sedikit pun", "Keteladanan pemimpin dan konsistensi penerapan aturan berjalan beriringan secara sinergis", "Sanksi diterapkan hanya pada level bawahan tanpa menyentuh manajemen puncak", "Pengawasan dilakukan secara rahasia tanpa melibatkan partisipasi masyarakat luas", "Gaji pejabat dinaikkan drastis tanpa diimbangi evaluasi kinerja yang ketat"],
    "answer": "B",
    "explanation": "Budaya integritas terbentuk melalui keteladanan pemimpin yang memberi contoh baik dan konsistensi penerapan aturan tanpa pilih kasih. Tanpa keduanya, budaya integritas tidak akan terbentuk secara berkelanjutan.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_011", "category": "TWK", "subcategory": "Integritas",
    "question": "Seorang ASN yang berintegritas akan menolak segala bentuk gratifikasi karena...",
    "options": ["Gratifikasi hanya diperbolehkan bagi pejabat tinggi eselon I", "Gratifikasi dapat memengaruhi objektivitas dalam pengambilan keputusan dan menimbulkan konflik kepentingan", "ASN tidak diperbolehkan menerima hadiah dalam bentuk apa pun", "Gratifikasi melanggar aturan jam kerja yang berlaku", "ASN tidak memiliki waktu luang untuk menerima gratifikasi"],
    "answer": "B",
    "explanation": "Gratifikasi dapat memengaruhi objektivitas dan independensi seorang ASN dalam mengambil keputusan. Penerimaan gratifikasi menimbulkan konflik kepentingan yang melanggar integritas dan kode etik ASN.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_012", "category": "TWK", "subcategory": "Integritas",
    "question": "Perhatikan tabel berikut! (1) Menolak penyuapan dalam transaksi bisnis. (2) Menyatakan pendapat kritis terhadap kebijakan pemerintah yang tidak berpihak. (3) Memalsukan informasi laporan keuangan untuk menghindari pajak. (4) Menyimpan rahasia jabatan demi keuntungan pribadi. Informasi yang menunjukkan sikap berintegritas terdapat pada nomor...",
    "options": ["(1) dan (2)", "(1) dan (3)", "(2) dan (3)", "(2) dan (4)", "(3) dan (4)"],
    "answer": "A",
    "explanation": "Menolak penyuapan dalam transaksi bisnis (1) dan menyatakan pendapat kritis terhadap kebijakan pemerintah yang tidak berpihak (2) merupakan pengamalan integritas. Memalsukan informasi (3) dan menyimpan rahasia jabatan demi keuntungan pribadi (4) jelas tidak berintegritas.",
    "difficulty": "easy"
  },
  # BELA NEGARA (6)
  {
    "id": "twk3_013", "category": "TWK", "subcategory": "Bela Negara",
    "question": "TNI sebagai komponen utama pertahanan negara RI memiliki tiga matra, yaitu...",
    "options": ["TNI Angkatan Darat, TNI Angkatan Laut, dan TNI Angkatan Udara", "TNI, POLRI, dan Civil Defense", "Militer reguler, marinir, dan militer cadangan nasional", "Angkatan darat, angkatan laut, dan angkatan bersenjata gabungan", "Pasukan perdamaian, pasukan elit, dan pasukan cadangan"],
    "answer": "A",
    "explanation": "TNI terdiri dari tiga matra yaitu TNI Angkatan Darat, TNI Angkatan Laut, dan TNI Angkatan Udara. Ketiga matra ini bekerja sama di bawah koordinasi Presiden untuk menjaga kedaulatan dan pertahanan negara.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_014", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Bela negara bagi seluruh warga negara Indonesia diatur dalam UUD 1945 Pasal...",
    "options": ["27 Ayat 1", "27 Ayat 2", "30 Ayat 1", "30 Ayat 2", "31 Ayat 1"],
    "answer": "C",
    "explanation": "Pasal 30 Ayat 1 UUD 1945 berbunyi: Setiap warga negara berhak dan wajib ikut serta dalam usaha pertahanan dan keamanan negara. Ketentuan ini mewajibkan seluruh warga negara untuk bela negara sesuai kemampuan masing-masing.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_015", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Peradilan militer di Indonesia berwenang mengadili...",
    "options": ["Seluruh warga negara Indonesia yang melakukan tindak pidana apapun", "Tentara Nasional Indonesia yang melakukan tindak pidana militer", "Seluruh penegak hukum di Indonesia tanpa terkecuali", "Pejabat negara yang melakukan tindak pidana korupsi", "Warga sipil yang bekerja sama dengan militer dalam keadaan darurat"],
    "answer": "B",
    "explanation": "Peradilan militer berwenang mengadili perkara pidana militer yang dilakukan oleh anggota TNI sesuai dengan hukum militer yang berlaku. Peradilan ini berbeda dari peradilan umum yang mengadili warga sipil.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_016", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Ancaman terhadap pertahanan negara RI dapat berasal dari ancaman militer dan ancaman nonmiliter. Contoh ancaman nonmiliter adalah...",
    "options": ["Serangan udara oleh negara lain yang melanggar wilayah udara nasional", "Invasi militer asing yang mendarat di wilayah perbatasan", "Penyebaran hoaks yang dapat mengancam stabilitas dan persatuan nasional", "Pendaratan pasukan khusus asing di wilayah teritorial Indonesia", "Penyerangan kapal perang Indonesia di jalur laut internasional"],
    "answer": "C",
    "explanation": "Ancaman nonmiliter meliputi berbagai bentuk yang dapat mengancam kedaulatan negara secara tidak langsung, seperti penyalahgunaan teknologi informasi, separaisme, bencana alam, dan penyebaran hoaks yang dapat memecah belah bangsa.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_017", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Peran serta masyarakat dalam sistem pertahanan dan keamanan negara yang dikenal dengan istilah Sishankamrata berarti...",
    "options": ["Sistem pertahanan yang hanya dikelola oleh militer profesional", "Sistem pertahanan dan keamanan rakyat semesta yang melibatkan seluruh potensi bangsa", "Sistem pertahanan berbasis intelijen militer yang didukung teknologi tinggi", "Sistem pertahanan bilateral dengan negara-negara sahabat", "Sistem pertahanan yang digerakkan oleh anggaran negara saja"],
    "answer": "B",
    "explanation": "Sistem Pertahanan dan Keamanan Rakyat Semesta (Sishankamrata) merupakan konsep pertahanan Indonesia yang melibatkan seluruh rakyat sebagai komponen pertahanan. Ini sesuai dengan semangat persatuan dan gotong royong bangsa Indonesia.",
    "difficulty": "hard"
  },
  {
    "id": "twk3_018", "category": "TWK", "subcategory": "Bela Negara",
    "question": "Perhatikan tabel berikut! (1) Ikut serta dalam pertahanan wilayah perbatasan. (2) Mengikuti wajib militer sesuai ketentuan yang berlaku. (3) Menyebarkan berita bohong yang dapat memecah belah. (4) Menjaga kelestarian lingkungan hidup untuk generasi mendatang. Dari informasi tersebut, yang merupakan implementasi bela negara adalah...",
    "options": ["(1), (2), dan (4)", "(1), (3), dan (4)", "(2), (3), dan (4)", "(1) dan (2)", "(3) dan (4)"],
    "answer": "A",
    "explanation": "Ikut serta dalam pertahanan wilayah perbatasan (1), mengikuti wajib militer (2), dan menjaga lingkungan hidup untuk generasi mendatang (4) merupakan bentuk bela negara. Menyebarkan berita bohong (3) jelas bukan bela negara karena justru merusak persatuan.",
    "difficulty": "easy"
  },
  # PILAR NEGARA (6)
  {
    "id": "twk3_019", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Pancasila sebagai dasar negara mengandung nilai-nilai yang harus diamalkan dalam kehidupan sehari-hari. Nilai tersebut meliputi...",
    "options": ["Hanya nilai-nilai religious tanpa nilai-nilai sosial kemasyarakatan", "Nilai-nilai luhur yang menjadi pedoman dalam kehidupan bermasyarakat, berbangsa, dan bernegara", "Hanya nilai-nilai politik internasional yang relevan", "Nilai-nilai ekonomi liberal yang menjadi pedoman utama", "Nilai-nilai yang hanya berlaku bagi pejabat negara"],
    "answer": "B",
    "explanation": "Pancasila mengandung nilai-nilai luhur yang menjadi pedoman hidup seluruh rakyat Indonesia dalam segenap aspek kehidupan bermasyarakat, berbangsa, dan bernegara. Nilai-nilai ini harus diamalkan, bukan sekadar diucapkan.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_020", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Kedudukan pembukaan UUD 1945 sebagai bagian yang tidak dapat diubah (tetap) menunjukkan bahwa...",
    "options": ["Pembukaan UUD 1945 hanya berlaku bagi militer dan pertahanan negara", "Nilai-nilai dasar dalam Pembukaan tidak dapat diubah oleh siapapun dalam kondisi apapun juga", "Pembukaan UUD 1945 harus diamandemen setiap 5 tahun sekali", "Pembukaan UUD 1945 hanya berlaku pada masa awal kemerdekaan Indonesia", "Pembukaan UUD 1945 merupakan lampiran yang tidak memiliki kekuatan hukum"],
    "answer": "B",
    "explanation": "Pasal 37 Ayat 5 UUD 1945 menyatakan bahwa Pembukaan tidak dapat diubah. Hal ini menunjukkan bahwa nilai-nilai dasar dalam Pembukaan, yaitu proklamasi kemerdekaan dan Pancasila, merupakan fondasi negara yang kekal.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_021", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Pasal 33 UUD 1945 mengatur tentang perekonomian nasional yang didasarkan atas...",
    "options": ["Sistem ekonomi kapitalis free market secara penuh", "Usaha bersama berdasar atas asas kekeluargaan", "Penghapusan seluruh kepemilikan私有 secara menyeluruh", "Dominasi pengusaha asing dalam pengelolaan ekonomi negara", "Sistem ekonomi komando yang diatur sepenuhnya oleh pemerintah pusat"],
    "answer": "B",
    "explanation": "Pasal 33 Ayat 1 UUD 1945 berbunyi: Perekonomian nasional disusun sebagai usaha bersama berdasar atas asas kekeluargaan. Prinsip kebersamaan dan kekeluargaan menjadi ciri khas perekonomian Indonesia.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_022", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Mahkamah Konstitusi (MK) memiliki wewenang untuk menguji undang-undang terhadap UUD 1945. Pengujian ini dalam ilmu hukum dikenal sebagai...",
    "options": ["Legislative review", "Judicial review", "Executive review", "Constitutional amendment", "Administrative appeal"],
    "answer": "B",
    "explanation": "Pengujian undang-undang terhadap UUD 1945 oleh MK disebut judicial review. MK berhak menilai apakah suatu undang-undang sesuai atau bertentangan dengan konstitusi sebagai penjaga ketatanegaraan.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_023", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Dewan Perwakilan Daerah (DPD) menurut UUD 1945 Pasal 22D berwenang untuk...",
    "options": ["Membuat undang-undang tanpa memerlukan persetujuan dari DPR", "Mengajukan rancangan undang-undang tentang otonomi daerah, pier stab dan creation, pranata alam, serta pengelolaan SDA", "Memilih Presiden dan Wakil Presiden secara langsung", "Mengubah isi pembukaan UUD 1945 sesuai kebutuhan zaman", "Mengangkat dan memberhentikan pejabat tinggi negara"],
    "answer": "B",
    "explanation": "Pasal 22D UUD 1945 menegaskan bahwa DPD berhak mengajukan rancangan undang-undang tentang otonomi daerah, pier stab dan creation, pranata alam, serta pengelolaan SDA. DPD tidak memiliki kekuatan legislatif seperti DPR.",
    "difficulty": "hard"
  },
  {
    "id": "twk3_024", "category": "TWK", "subcategory": "Pilar Negara",
    "question": "Pasal 29 UUD 1945 mengatur tentang...",
    "options": ["Hak asasi manusia dalam kehidupan beragama dan berkeyakinan", "Negara berdasarkan atas Ketuhanan Yang Maha Esa", "Sistem pertahanan dan keamanan negara yang terpadu", "Kedaulatan rakyat dalam sistem pemerintahan", "Pembagian kekuasaan antara Executivo dan legislatif"],
    "answer": "B",
    "explanation": "Pasal 29 UUD 1945 mengatur tentang dasar negara Indonesia yang berdasarkan Ketuhanan Yang Maha Esa. Ketentuan ini menjamin kemerdekaan segala agama dan kepercayaan terhadap Tuhan Yang Maha Esa bagi seluruh rakyat Indonesia.",
    "difficulty": "medium"
  },
  # BAHASA INDONESIA (6)
  {
    "id": "twk3_025", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Perhatikan kalimat berikut! Laporan tersebut kurang lebih five thousand lembar. Kalimat tersebut tidak sesuai dengan kaidah PUEBI karena...",
    "options": ["Penggunaan istilah bahasa Inggris dalam kalimat formal resmi yang mengabaikan kaidah bahasa Indonesia baku", "Penggunaan kata penghubung yang tidak tepat dalam struktur kalimat", "Penggunaan angka alih-alih lambang bilangan sesuai kaidah yang berlaku", "Penggunaan tanda baca yang salah di akhir kalimat", "Tidak adanya subjek yang jelas dalam kalimat tersebut"],
    "answer": "A",
    "explanation": "Penggunaan istilah bahasa Inggris five thousand dalam kalimat formal resmi bertentangan dengan kaidah PUEBI yang mengharuskan penggunaan bahasa Indonesia baku. Seharusnya menggunakan lima ribu lembar atau 5.000 lembar.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_026", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Perhatikan koreksi penulisan berikut! (1) Kami akan mengadakan rapat pada hari Jumat, 17 Agustus 2024, pukul 09.00 WIB. (2) Pertandingan akan dimulai pada tanggal 17-agustus-2024. (3) Puncak acara diper tanggal 17 Agustus 2024. Yang sesuai dengan kaidah penulisan bahasa Indonesia baku terdapat pada nomor...",
    "options": ["(1) saja", "(2) saja", "(3) saja", "(1) dan (3)", "(2) dan (3)"],
    "answer": "A",
    "explanation": "Kalimat (1) sesuai kaidah: angka pada tanggal ditulis dengan lambang bilangan, nama hari dan bulan ditulis kapital, dan singkatan WIB sesuai ketentuan PUEBI. Kalimat (2) tidak baku karena menggunakan tanda hubung pada tanggal. Kalimat (3) tidak baku karena kata diper bukan bentuk baku.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_027", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Penulisan judul buku yang benar menurut PUEBI adalah...",
    "options": ['Buku ini berjudul "panduan lengkap bahasa Indonesia"', 'Buku ini berjudul "Panduan Lengkap Bahasa Indonesia"', 'Buku ini berjudul "PANDUAN LENGKAP BAHASA INDONESIA"', 'Buku ini berjudul "panduan lengkap Bahasa Indonesia"', 'Buku ini berjudul "Panduan lengkap bahasa Indonesia"'],
    "answer": "B",
    "explanation": "Menurut PUEBI, judul buku atau karya ilmiah ditulis dengan huruf kapital pada setiap kata pertamanya. Jadi penulisan yang benar adalah Panduan Lengkap Bahasa Indonesia.",
    "difficulty": "easy"
  },
  {
    "id": "twk3_028", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Perhatikan penggunaan huruf kapital berikut! (1) Saya membaca buku Bahasa Indonesia. (2) Mereka berasal dari Daerah Istimewa Yogyakarta. (3) Kami merayakan kemerdekaan pada bulan Agustus. (4) Gunung Merapi terletak di provinsi Jawa Tengah. Penggunaan huruf kapital yang sesuai PUEBI terdapat pada nomor...",
    "options": ["(1) dan (2)", "(2) dan (3)", "(3) dan (4)", "(1), (2), dan (4)", "(1), (3), dan (4)"],
    "answer": "E",
    "explanation": "Huruf kapital digunakan untuk: nama mata pelajaran (Bahasa Indonesia), bulan (Agustus), dan nama tempat (Yogyakarta, Jawa Tengah). Semua pilihan (1), (2), (3), dan (4) menggunakan huruf kapital dengan tepat sesuai PUEBI.",
    "difficulty": "medium"
  },
  {
    "id": "twk3_029", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": 'Perhatikan kalimat berikut dengan seksama! "Jadi, dapat kami simpulkan bahwa tujuan daripada kegiatan ini adalah untuk meningkatkan kualitas SDM dan meninggkatkan kesejahteraan rakyat." Kesalahan dalam kalimat tersebut meliputi...',
    "options": ["Kata Simpulkan salah eja, kata daripada tidak baku, kata meninggkatkan salah eja", "Kata Jadi seharusnya huruf kapital saja, kata Simpulkan salah eja, kata daripada tidak baku", "Penggunaan tanda koma yang berlebihan, kata Simpulkan salah eja, singkatan SDM tidak baku", "Hanya penggunaan singkatan SDM yang tidak baku dalam konteks kalimat formal", "Tidak ada kesalahan sama sekali dalam kalimat tersebut"],
    "answer": "A",
    "explanation": "Kalimat tersebut mengandung tiga kesalahan: kata Simpulkan seharusnya huruf kecil karena bukan nama diri; kata daripada bukan bentuk baku; kata meninggkatkan seharusnya meningkatkan sesuai kaidah ejaan baku.",
    "difficulty": "hard"
  },
  {
    "id": "twk3_030", "category": "TWK", "subcategory": "Bahasa Indonesia",
    "question": "Menurut PUEBI, penulisan singkatan yang benar adalah...",
    "options": ["Yth", "yt", "A.n", "an", "sdh"],
    "answer": "A",
    "explanation": "Menurut PUEBI, singkatan Yth. (untukyth) merupakan bentuk singkatan yang baku. Penulisan yt, A.n, an, atau sdh tidak sesuai dengan kaidah PUEBI karena tidak mengikuti pola singkatan resmi yang ditetapkan.",
    "difficulty": "medium"
  }
]

# ============================================================
# TIU PAKET 3 - 35 soal
# ============================================================
tiu3 = [
  # ANALOGI (5)
  {
    "id": "tiu3_001", "category": "TIU", "subcategory": "Analogi",
    "question": "ARSITEK : BANGUNAN :: PELUKIS : ...",
    "options": ["Editor", "Lukisan", "Kanvas", "Galeri", "Studio"],
    "answer": "B",
    "explanation": "Hubungan analogi: pencipta dengan karyanya. ARSITEK menciptakan BANGUNAN. PELUKIS menciptakan LUKISAN. Jadi jawaban yang tepat adalah LUKISAN.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_002", "category": "TIU", "subcategory": "Analogi",
    "question": "KONVEKSI : PAKAIAN :: PERCETAKAN : ...",
    "options": ["Tinta", "Buku", "Penulis", "Kertas", "Meja"],
    "answer": "B",
    "explanation": "Hubungan analogi: penghasil produk jadi. KONVEKSI menghasilkan PAKAIAN jadi untuk dijual. PERCETAKAN menghasilkan BUKU. Jadi jawaban yang tepat adalah BUKU.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_003", "category": "TIU", "subcategory": "Analogi",
    "question": "PENJAHIT : JARUM :: KOKI : ...",
    "options": ["Kompor", "Wajan", "Pisau", "Piring", "Sendok"],
    "answer": "C",
    "explanation": "Hubungan analogi: alat dengan profesinya. PENJAHIT menggunakan JARUM untuk menjahit. KOKI menggunakan PISAU untuk memotong bahan makanan. Jadi jawaban yang tepat adalah PISAU.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_004", "category": "TIU", "subcategory": "Analogi",
    "question": "PENDIDIKAN : ILMU :: EKONOMI : ...",
    "options": ["Perdagangan", "Uang", "Kesejahteraan", "Pasar", "Industri"],
    "answer": "C",
    "explanation": "Hubungan analogi: bidang dengan tujuannya. PENDIDIKAN bertujuan menghasilkan ILMU pengetahuan. EKONOMI bertujuan mencapai KESEJAHTERAAN masyarakat. Jadi jawaban yang tepat adalah KESEJAHTERAAN.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_005", "category": "TIU", "subcategory": "Analogi",
    "question": "GENDANG : ORKESTRA :: BUKU : ...",
    "options": ["Penulis", "Perpustakaan", "Judul", "Fiksi", "Ilmu"],
    "answer": "B",
    "explanation": "Hubungan analogi: koleksi utama dalam suatu tempat. GENDANG adalah alat musik utama dalam ORKESTRA. BUKU adalah koleksi utama dalam PERPUSTAKAAN. Jadi jawaban yang tepat adalah PERPUSTAKAAN.",
    "difficulty": "medium"
  },
  # SILOGISME (5)
  {
    "id": "tiu3_006", "category": "TIU", "subcategory": "Silogisme",
    "question": "Jika hujan turun, maka jalanan basah. Jika jalanan basah, maka kecepatan kendaraan melambat. Jika kecepatan kendaraan melambat, maka kemacetan terjadi. Simpulan yang paling logis adalah...",
    "options": ["Hujan turun selalu menyebabkan kemacetan di semua jalan", "Kemacetan hanya terjadi saat hujan turun", "Jika hujan turun, maka kemacetan terjadi", "Kemacetan terjadi jika dan hanya jika hujan turun", "Kemacetan tidak terjadi saat jalanan tidak basah"],
    "answer": "C",
    "explanation": "Dari serangkaian implikasi: hujan turun -> jalanan basah -> kecepatan melambat -> kemacetan. Melalui transitivitas implikasi logika, dapat disimpulkan langsung bahwa jika hujan turun, maka kemacetan terjadi.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_007", "category": "TIU", "subcategory": "Silogisme",
    "question": "Semua mahasiswa yang rajin belajar akan lulus ujian. Sebagian mahasiswa mengambil program bimbingan tambahan. Simpulan yang sah adalah...",
    "options": ["Semua mahasiswa yang mengikuti bimbingan tambahan akan lulus ujian", "Semua mahasiswa yang lulus mengikuti ujian", "Semua yang mengikuti ujian mengambil bimbingan tambahan", "Tidak dapat ditarik kesimpulan yang pasti", "Sebagian yang mengikuti bimbingan tambahan tidak mengikuti ujian"],
    "answer": "D",
    "explanation": "Dari premis mayor Semua mahasiswa yang rajin belajar akan lulus ujian dan premis minor Sebagian mahasiswa mengambil program bimbingan tambahan, tidak ada informasi yang menghubungkan kedua kelompok secara pasti. Jadi tidak dapat ditarik kesimpulan yang pasti.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_008", "category": "TIU", "subcategory": "Silogisme",
    "question": "Premis 1: Tidak ada mahasiswa yang tidak membutuhkan waktu untuk belajar. Premis 2: Beberapa mahasiswa mengambil program multitasking. Simpulan yang tepat adalah...",
    "options": ["Semua mahasiswa membutuhkan waktu untuk belajar", "Sebagian mahasiswa tidak mengambil program multitasking", "Semua mahasiswa mengambil program multitasking", "Tidak ada mahasiswa yang mengambil program multitasking", "Kesimpulan tidak dapat ditentukan"],
    "answer": "A",
    "explanation": "Premis 1 menyatakan tidak ada mahasiswa yang tidak membutuhkan waktu untuk belajar, berarti semua mahasiswa membutuhkan waktu untuk belajar. Premis 2 tidak mengubah kesimpulan. Jadi kesimpulan yang pasti adalah semua mahasiswa membutuhkan waktu untuk belajar.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_009", "category": "TIU", "subcategory": "Silogisme",
    "question": "Semua jenis buah yang berwarna merah mengandung antioksidan tinggi. Mangga berwarna hijau dan tidak mengandung antioksidan tinggi. Simpulan yang tepat adalah...",
    "options": ["Mangga bukan jenis buah yang berwarna merah", "Semua buah berwarna hijau tidak mengandung antioksidan tinggi", "Mangga mengandung antioksidan tinggi", "Semua buah yang tidak berwarna merah tidak mengandung antioksidan tinggi", "Tidak dapat disimpulkan apa-apa"],
    "answer": "A",
    "explanation": "Dari premis: semua buah berwarna merah mengandung antioksidan tinggi. Mangga berwarna hijau dan tidak mengandung antioksidan tinggi. Karena mangga tidak mengandung antioksidan tinggi, maka sesuai premis, mangga bukan buah berwarna merah.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_010", "category": "TIU", "subcategory": "Silogisme",
    "question": "Semua mahasiswa yang rajin belajar akan lulus ujian. Beberapa mahasiswa tidak mengikuti kelas secara teratur. Simpulan yang dapat ditarik adalah...",
    "options": ["Semua mahasiswa yang rajin belajar mengikuti kelas secara teratur", "Semua mahasiswa yang tidak mengikuti kelas secara teratur tidak lulus ujian", "Beberapa mahasiswa yang rajin belajar tidak lulus ujian", "Tidak dapat ditarik kesimpulan yang pasti", "Semua mahasiswa yang lulus ujian rajin belajar"],
    "answer": "E",
    "explanation": "Dari premis: semua mahasiswa yang rajin belajar akan lulus ujian. Beberapa mahasiswa tidak mengikuti kelas secara teratur. Karena rajin belajar menjamin kelulusan, maka semua yang lulus ujian adalah rajin belajar. Jadi simpulan yang dapat ditarik adalah Semua mahasiswa yang lulus ujian rajin belajar.",
    "difficulty": "hard"
  },
  # ANALITIS (5)
  {
    "id": "tiu3_011", "category": "TIU", "subcategory": "Analitis",
    "question": "Empat siswa (W, X, Y, Z) memiliki tinggi berbeda. W lebih tinggi dari X. Y lebih tinggi dari W. Z tidak lebih tinggi dari X. Pernyataan yang PALING TEPAT adalah...",
    "options": ["Y adalah siswa tertinggi", "Z adalah siswa terendah", "W lebih tinggi dari Z", "X lebih tinggi dari Z", "Tidak ada informasi cukup untuk menentukan siapa tertinggi"],
    "answer": "A",
    "explanation": "Dari informasi: Y > W > X dan Z tidak lebih tinggi dari X, berarti Z <= X. Dengan Y > W > X dan Z <= X, maka urutan: Y > W > X >= Z. Jadi Y adalah siswa tertinggi.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_012", "category": "TIU", "subcategory": "Analitis",
    "question": "Sebuah perusahaan memiliki karyawan A, B, C, D, dan E. Gaji A lebih besar dari B. Gaji C lebih kecil dari D. Gaji D lebih kecil dari A. Gaji E sama dengan gaji B. Pernyataan yang BENAR adalah...",
    "options": ["Gaji C paling rendah", "Gaji E lebih besar dari D", "Gaji A paling tinggi", "Gaji B lebih kecil dari D", "Gaji D lebih besar dari B"],
    "answer": "C",
    "explanation": "Dari informasi: A > B, C < D, D < A, E = B. Urutan: A > D > C dan A > B = E. Jadi A memiliki gaji paling tinggi.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_013", "category": "TIU", "subcategory": "Analitis",
    "question": "Dalam perlombaan lari, Andi finish lebih cepat dari Budi. Chris finish lebih cepat dari Andi. Dodi finish lebih cepat dari Chris. Edo finish lebih lambat dari Dodi. Yang finish paling lambat adalah...",
    "options": ["Andi", "Budi", "Chris", "Dodi", "Edo"],
    "answer": "B",
    "explanation": "Urutan finish tercepat: Dodi > Chris > Andi > Budi. Edo finish lebih lambat dari Dodi, artinya waktu Edo > waktu Dodi. Urutan waktu dari terlambat: Budi > Andi > Chris > Dodi > Edo. Jadi Budi finish paling lambat.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_014", "category": "TIU", "subcategory": "Analitis",
    "question": "Diketahui: semua X adalah Y. Sebagian Y adalah Z. Simpulan yang sah adalah...",
    "options": ["Semua X adalah Z", "Sebagian X adalah Z", "Tidak ada X yang Z", "Semua Z adalah X", "Tidak dapat disimpulkan"],
    "answer": "B",
    "explanation": "Semua X adalah Y dan sebagian Y adalah Z. X termasuk dalam Y, dan sebagian dari Y adalah Z. Jadi sebagian X mungkin termasuk dalam Z. Simpulan yang sah adalah sebagian X adalah Z.",
    "difficulty": "hard"
  },
  {
    "id": "tiu3_015", "category": "TIU", "subcategory": "Analitis",
    "question": "Tiga anak A, B, dan C memiliki tinggi badan berbeda. A lebih tinggi dari B. B lebih tinggi dari C. Jika D lebih tinggi dari A, siapa yang paling rendah?",
    "options": ["A", "B", "C", "D", "Tidak dapat ditentukan"],
    "answer": "C",
    "explanation": "Diketahui: C < B < A (A lebih tinggi dari B, B lebih tinggi dari C) dan D > A. Urutan tinggi: D > A > B > C. Jadi yang paling rendah adalah C.",
    "difficulty": "easy"
  },
  # DERET (5)
  {
    "id": "tiu3_016", "category": "TIU", "subcategory": "Deret",
    "question": "3, 8, 15, 24, 35, ..., 63. Nilai yang tepat untuk titik-titik adalah...",
    "options": ["44", "46", "48", "50", "52"],
    "answer": "C",
    "explanation": "Pola: 3+5=8, 8+7=15, 15+9=24, 24+11=35, 35+13=48, 48+15=63. Selisihnya adalah bilangan ganjil: 5, 7, 9, 11, 13, 15. Setelah 35+13=48, lalu 48+15=63.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_017", "category": "TIU", "subcategory": "Deret",
    "question": "100, 95, 85, 70, 50, ..., 5. Nilai yang tepat untuk titik-titik adalah...",
    "options": ["25", "30", "35", "40", "45"],
    "answer": "A",
    "explanation": "Pola pengurangan: 100-5=95, 95-10=85, 85-15=70, 70-20=50. Pengurang naik 5 setiap langkah: 5, 10, 15, 20, 25. Jadi 50-25=25. Lalu 25-20=5. Pola pengurang berubah arah setelah titik tengah.",
    "difficulty": "hard"
  },
  {
    "id": "tiu3_018", "category": "TIU", "subcategory": "Deret",
    "question": "2, 6, 14, 30, 62, ..., 254. Nilai yang tepat untuk titik-titik adalah...",
    "options": ["126", "128", "130", "132", "134"],
    "answer": "A",
    "explanation": "Pola: 2x2+2=6, 6x2+2=14, 14x2+2=30, 30x2+2=62, 62x2+2=126, 126x2+2=254. Setiap langkah dikali 2 lalu ditambah 2.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_019", "category": "TIU", "subcategory": "Deret",
    "question": "5, 11, 23, 47, 95, ... Nilai yang tepat adalah...",
    "options": ["190", "191", "192", "193", "194"],
    "answer": "B",
    "explanation": "Pola: 5+6=11, 11+12=23, 23+24=47, 47+48=95, 95+96=191. Penambahannya dikali 2 setiap langkah: 6, 12, 24, 48, 96.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_020", "category": "TIU", "subcategory": "Deret",
    "question": "1, 4, 9, 16, 25, ..., 49. Nilai yang tepat untuk titik-titik adalah...",
    "options": ["30", "34", "36", "38", "42"],
    "answer": "C",
    "explanation": "Pola kuadrat: 1 kuadrat 1, 2 kuadrat 4, 3 kuadrat 9, 4 kuadrat 16, 5 kuadrat 25, 6 kuadrat 36, 7 kuadrat 49.",
    "difficulty": "easy"
  },
  # ARITMETIKA (5)
  {
    "id": "tiu3_021", "category": "TIU", "subcategory": "Aritmetika",
    "question": "Harga barang setelah diskon 20% adalah Rp480.000,00. Harga barang sebelum diskon adalah...",
    "options": ["Rp560.000,00", "Rp580.000,00", "Rp600.000,00", "Rp620.000,00", "Rp640.000,00"],
    "answer": "C",
    "explanation": "Harga setelah diskon = 80% dari harga awal. Harga awal = 480.000 / 0,8 = 600.000. Jadi harga sebelum diskon adalah Rp600.000,00.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_022", "category": "TIU", "subcategory": "Aritmetika",
    "question": "Sebuah bus membawa 48 penumpang. Di halte pertama turun 12 orang dan naik 8 orang. Di halte kedua turun 15 orang dan naik 5 orang. Jumlah penumpang bus setelah halte kedua adalah...",
    "options": ["30", "32", "34", "36", "38"],
    "answer": "C",
    "explanation": "Mula-mula 48. Halte 1: turun 12 -> 36, naik 8 -> 44. Halte 2: turun 15 -> 29, naik 5 -> 34.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_023", "category": "TIU", "subcategory": "Aritmetika",
    "question": "Jika 3x + 7 = 22, maka nilai dari 5x - 3 adalah...",
    "options": ["18", "20", "22", "24", "26"],
    "answer": "C",
    "explanation": "3x + 7 = 22 -> 3x = 15 -> x = 5. Maka 5x - 3 = 5(5) - 3 = 25 - 3 = 22.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_024", "category": "TIU", "subcategory": "Aritmetika",
    "question": "Perbandingan uang Anton dan Budi adalah 5:3. Jumlah uang mereka adalah Rp400.000,00. Selisih uang Anton dan Budi adalah...",
    "options": ["Rp80.000,00", "Rp100.000,00", "Rp120.000,00", "Rp150.000,00", "Rp200.000,00"],
    "answer": "B",
    "explanation": "Jumlah perbandingan = 5+3 = 8 bagian. Satu bagian = 400.000/8 = 50.000. Selisih = 5-3 = 2 bagian = 2 x 50.000 = 100.000.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_025", "category": "TIU", "subcategory": "Aritmetika",
    "question": "Sebuah proyek dikerjakan oleh 12 orang dalam 20 hari. Jika proyek yang sama harus selesai dalam 15 hari, maka tambahan pekerja yang dibutuhkan adalah...",
    "options": ["4 orang", "6 orang", "8 orang", "10 orang", "12 orang"],
    "answer": "A",
    "explanation": "Total pekerjaan = orang x hari = 12 x 20 = 240 orang-hari. Untuk 15 hari, dibutuhkan = 240/15 = 16 orang. Tambahan = 16 - 12 = 4 orang.",
    "difficulty": "medium"
  },
  # CERITA MATEMATIKA (5)
  {
    "id": "tiu3_026", "category": "TIU", "subcategory": "Cerita Matematika",
    "question": "Pak Hasan mengecat pagar sepanjang 60 meter. Setiap hari ia mengecat 15 meter. Setelah 3 hari, berapa meter pagar yang belum dicat?",
    "options": ["15 meter", "20 meter", "25 meter", "30 meter", "35 meter"],
    "answer": "A",
    "explanation": "Total pagar 60 meter. Sudah dicat 3 x 15 = 45 meter. Belum dicat = 60 - 45 = 15 meter.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_027", "category": "TIU", "subcategory": "Cerita Matematika",
    "question": "Satu liter bensin mampu menempuh 12 km. Dengan bensin 5 liter, seorang sopir menempuh jarak pulang-pergi 40 km. Berapa km jarak rumah ke tempat kerja?",
    "options": ["20 km", "25 km", "30 km", "35 km", "40 km"],
    "answer": "A",
    "explanation": "5 liter x 12 km/liter = 60 km total. Jarak pulang-pergi = 40 km. Sisa bensin menempuh 60 - 40 = 20 km. Jarak rumah ke tempat kerja = 40/2 = 20 km.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_028", "category": "TIU", "subcategory": "Cerita Matematika",
    "question": "Satu kantong beras berharga Rp72.000,00 dan beratnya 6 kg. Jika Ibu membeli 10 kg beras dengan uang Rp200.000,00, berapa kembalian yang diterima?",
    "options": ["Rp60.000,00", "Rp80.000,00", "Rp100.000,00", "Rp120.000,00", "Rp140.000,00"],
    "answer": "B",
    "explanation": "Harga per kg = 72.000/6 = 12.000 per kg. Beli 10 kg = 10 x 12.000 = 120.000. Bayar 200.000, kembalian = 200.000 - 120.000 = 80.000.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_029", "category": "TIU", "subcategory": "Cerita Matematika",
    "question": "Untuk membuat 4 kue dibutuhkan 600 gram tepung. Jika ingin membuat 10 kue, berapa gram tepung yang dibutuhkan?",
    "options": ["1.200 gram", "1.350 gram", "1.500 gram", "1.650 gram", "1.800 gram"],
    "answer": "C",
    "explanation": "4 kue butuh 600 gram tepung. Per kue = 600/4 = 150 gram. 10 kue butuh 10 x 150 = 1.500 gram.",
    "difficulty": "easy"
  },
  {
    "id": "tiu3_030", "category": "TIU", "subcategory": "Cerita Matematika",
    "question": "Jarak kota A ke kota B adalah 240 km. Sebuah mobil berangkat dari A ke B dengan kecepatan 60 km/jam. Setelah 2 jam, mobil istirahat 30 menit. Pukul berapa mobil tiba di B jika berangkat pukul 11.30?",
    "options": ["14.30", "15.00", "15.30", "16.00", "16.30"],
    "answer": "D",
    "explanation": "Waktu tempuh normal tanpa istirahat: 240/60 = 4 jam. Mobil berjalan 2 jam -> menempuh 120 km. Sisa jarak = 120 km. Istirahat 30 menit. Waktu tempuh sisa = 120/60 = 2 jam. Total = 2 jam perjalanan + 0,5 jam istirahat + 2 jam perjalanan = 4,5 jam. Berangkat 11.30, tiba 16.00.",
    "difficulty": "hard"
  },
  # FIGURAL (5)
  {
    "id": "tiu3_031", "category": "TIU", "subcategory": "Figural",
    "isFigural": True,
    "figuralData": '{"type": "deret", "sequence": ["triangle", "square", "circle", "triangle", "?"], "answerShapes": "diamond,square,pentagon,circle,hexagon", "correctIndex": 1}',
    "question": "Perhatikan deret bentuk berikut! Terdapat tiga bentuk: Segitiga, Persegi, Lingkaran, Segitiga. Pola berulang adalah...",
    "options": ["Persegi", "Lingkaran", "Segilima", "Wajik", "Segienam"],
    "answer": "A",
    "explanation": "Pola bentuk: Segitiga, Persegi, Lingkaran, Segitiga. Pola pengulangan: Segitiga - Persegi - Lingkaran. Setelah Segitiga, berikutnya dalam pola adalah Persegi. Jadi jawabannya adalah Persegi.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_032", "category": "TIU", "subcategory": "Figural",
    "isFigural": True,
    "figuralData": '{"type": "matriks", "gridData": [["triangle", "circle", "square"], ["square", "triangle", "circle"], ["circle", "square", "?"]], "answerShapes": "triangle,circle,pentagon,diamond,hexagon", "correctIndex": 0}',
    "question": "Perhatikan matriks 3x3 berikut! Baris 1: Segitiga, Lingkaran, Segiempat. Baris 2: Segiempat, Segitiga, Lingkaran. Baris 3: Lingkaran, Segiempat, ? Elemen yang tepat untuk mengisi tanda tanya adalah...",
    "options": ["Segitiga", "Lingkaran", "Segiempat", "Wajik", "Segilima"],
    "answer": "A",
    "explanation": "Pola matriks mengikuti pergeseran bentuk: Baris 1: Segitiga(1), Lingkaran(2), Segiempat(3). Baris 2: Segiempat(3), Segitiga(1), Lingkaran(2). Baris 3: Lingkaran(2), Segiempat(3), Segitiga(1). Jadi ? = Segitiga.",
    "difficulty": "hard"
  },
  {
    "id": "tiu3_033", "category": "TIU", "subcategory": "Figural",
    "isFigural": True,
    "figuralData": '{"type": "deret", "sequence": ["filled-circle", "empty-square", "filled-triangle", "empty-circle", "?"], "answerShapes": "filled-square,empty-triangle,diamond,filled-diamond,pentagon", "correctIndex": 0}',
    "question": "Perhatikan pola deret figural berikut! Bentuk berisi hitam, bentuk garis, bentuk berisi hitam, bentuk garis, ?. Pola yang tepat untuk menggantikan tanda tanya adalah...",
    "options": ["Bentuk berisi hitam", "Bentuk garis", "Bentuk titik", "Bentuk kosong", "Bentuk campuran"],
    "answer": "A",
    "explanation": "Pola: bentuk berisi hitam, bentuk garis, bentuk berisi hitam, bentuk garis, ?. Pola pengulangan: berisi -> garis -> berisi -> garis -> berisi. Setelah bentuk garis, berikutnya adalah bentuk berisi hitam.",
    "difficulty": "medium"
  },
  {
    "id": "tiu3_034", "category": "TIU", "subcategory": "Figural",
    "isFigural": True,
    "figuralData": '{"type": "matriks", "gridData": [["large-circle", "small-square", "large-triangle"], ["small-square", "large-triangle", "large-circle"], ["large-triangle", "large-circle", "?"]], "answerShapes": "small-circle,small-triangle,large-square,diamond,pentagon", "correctIndex": 0}',
    "question": "Perhatikan matriks figural berikut! Baris 1: Lingkaran besar, Segiempat kecil, Segitiga besar. Baris 2: Segiempat kecil, Segitiga besar, Lingkaran besar. Baris 3: Segitiga besar, Lingkaran besar, ? Elemen yang tepat adalah...",
    "options": ["Lingkaran kecil", "Segiempat besar", "Segitiga kecil", "Wajik", "Segilima"],
    "answer": "A",
    "explanation": "Matriks menunjukkan pola rotasi dan ukuran: Baris 1: besar-kecil-besar. Baris 2: kecil-besar-besar. Baris 3: besar-besar-?. Pola menunjukkan bahwa elemen terakhir harus kecil. Dari pilihan yang tersedia, Lingkaran kecil paling sesuai sebagai kelanjutan pola.",
    "difficulty": "hard"
  },
  {
    "id": "tiu3_035", "category": "TIU", "subcategory": "Figural",
    "isFigural": True,
    "figuralData": '{"type": "deret", "sequence": ["arrow-right", "arrow-down", "arrow-left", "arrow-up", "?"], "answerShapes": "arrow-right,arrow-down,arrow-left,arrow-diagonal,circle", "correctIndex": 0}',
    "question": "Perhatikan deret figural berikut! Arahan panah: kanan, bawah, kiri, atas, ?. Pola yang tepat untuk menggantikan tanda tanya adalah...",
    "options": ["Kanan", "Bawah", "Kiri", "Atas", "Diagonal"],
    "answer": "A",
    "explanation": "Pola deret: panah kanan -> bawah -> kiri -> atas -> ?. Arah berputar berlawanan arah jarum jam: kanan(0), bawah(90), kiri(180), atas(270), kanan(360). Jadi berikutnya adalah arah kanan.",
    "difficulty": "easy"
  }
]

# ============================================================
# TKP PAKET 3 - 45 soal
# ============================================================
tkp3 = [
  # PELAYANAN PUBLIK (8)
  {
    "id": "tkp3_001", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Seorang warga datang ke kantor camat dengan wajah marah dan mengeluh bahwa ia sudah menunggu selama 2 jam untuk sekadar memperpanjang Surat Keterangan Tidak Mampu. Sebagai pimpinan di kantor tersebut, langkah terbaik yang diambil adalah...",
    "options": ["Menyalahkan warga karena seharusnya datang lebih awal", "Menganalisis penyebab antrean panjang dan memperbaiki sistem pelayanan secara sistematis", "Menutup sementara layanan untuk memeriksa prosedur yang ada", "Menyuruh warga pulang dan datang di hari lain", "Memberikan prioritas layanan kepada warga tanpa memperbaiki sistem"],
    "answer": "B",
    "explanation": "Orientasi pelayanan publik yang baik mendorong pimpinan untuk menganalisis akar masalah antrean dan memperbaiki sistem secara terstruktur. Ini menunjukkan tanggung jawab dan orientasi pada peningkatan kualitas layanan.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_002", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Anda diminta menangani permohonan dari warga yang memerlukan dokumen kepindahan segera untuk keperluan sekolah anaknya. Namun prosedur normal memerlukan waktu 3 hari kerja. Sebagai petugas, tindakan yang paling menunjukkan empati sekaligus profesionalisme adalah...",
    "options": ["Menolak karena tidak sesuai prosedur dan tidak ada pengecualian", "Menjelaskan prosedur dan meminta warga sabar mengikuti tahapan normal", "Mencari solusi percepatan proses dengan tetap memperhatikan aturan dan mencatat alasan kecepatan yang urgent", "Mengarahkan warga ke bagian lain tanpa tindak lanjut", "Menunda karena banyak permohonan serupa yang juga urgent"],
    "answer": "C",
    "explanation": "Mencari solusi percepatan proses dengan tetap memperhatikan aturan dan mencatat alasan kecepatan yang urgent menunjukkan keseimbangan antara empati terhadap kebutuhan warga dan profesionalisme dalam menjaga integritas prosedur.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_003", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Anda mengelola loket pelayanan di kantor lurah. Seorang lansia datang untuk mengurus perpanjangan Kartu Keluarga tetapi tidak dapat melengkapi seluruh dokumen karena kondisi kesehatannya. Sebagai petugas, tindakan terbaik adalah...",
    "options": ["Meminta lansia tersebut kembali besok dengan dokumen lengkap", "Membantu lansia melengkapi dokumen yang memungkinkan dan memberikan prioritas layanan", "Menolak layanan karena prosedur tidak dipenuhi secara penuh", "Menghubungi keluarga lansia dan meminta mereka untuk menguruskan", "Memberikan informasi sederhana kemudian meminta lansia pulang"],
    "answer": "B",
    "explanation": "Membantu lansia melengkapi dokumen yang memungkinkan dan memberikan prioritas layanan mencerminkan empati dan profesionalisme dalam pelayanan publik. Warga lanjut usia memerlukan perhatian khusus dan pendekatan yang lebih manusiawi.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_004", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Saat sedang melayani warga, Anda menerima telepon dari atasan tentang pekerjaan yang harus segera diselesaikan. Sementara itu, seorang warga masih menunggu untuk dilayani. Langkah yang paling tepat adalah...",
    "options": ["Abaikan warga dan selesaikan tugas dari atasan terlebih dahulu", "Melayani warga terlebih dahulu dengan baik, lalu selesaikan tugas dari atasan", "Meminta warga menunggu karena tugas dari atasan lebih penting", "Menyerahkan pelayanan kepada rekan kerja tanpa konfirmasi", "Menolak telepon dari atasan dan fokus hanya pada warga"],
    "answer": "B",
    "explanation": "Melayani warga terlebih dahulu dengan baik, lalu menyelesaikan tugas atasan menunjukkan keseimbangan antara tanggung jawab terhadap warga dan atasan. Ini mencerminkan prioritas pelayanan publik yang baik.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_005", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Anda menemukan sebuah dokumen penting milik warga yang sudah tertinggal di meja kerja selama beberapa hari. Warga tersebut memerlukan dokumen itu untuk keperluan segera. Tindakan yang harus Anda lakukan adalah...",
    "options": ["Biarkan karena bukan tanggung jawab Anda dan dokumen sudah di luar prosedur", "Cari tahu siapa penanggung jawab dan segera sampaikan dokumen tersebut untuk segera diproses", "Simpan di lemari arsip sampai ada yang menanyakan", "Buang karena sudah tidak relevan dan melewati batas waktu", "Pindahkan ke bagian lain tanpa memberitahu warga"],
    "answer": "B",
    "explanation": "Mencari penanggung jawab dan menyampaikan dokumen untuk segera diproses adalah tindakan yang menunjukkan tanggung jawab dan dedikasi terhadap pelayanan publik. Ini mengutamakan kebutuhan warga di atas segalanya.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_006", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Anda diminta memimpin sebuah proyek pelayanan publik dengan anggaran yang terbatas. Masyarakat berharap hasil proyek dapat menyelesaikan masalah mereka. Strategi yang paling tepat adalah...",
    "options": ["Menunda proyek sampai ada anggaran yang mencukupi", "Membuat rencana kerja yang menghasilkan dampak maksimal dengan anggaran terbatas yang ada", "Mengurangi ruang lingkup proyek tanpa komunikasi dengan masyarakat", "Menyerahkan tanggung jawab kepada pihak ketiga", "Menggunakan seluruh anggaran untuk bagian yang paling terlihat saja"],
    "answer": "B",
    "explanation": "Membuat rencana kerja yang menghasilkan dampak maksimal dengan anggaran terbatas menunjukkan kemampuan mengelola sumber daya secara efisien dan tetap mengutamakan kebutuhan masyarakat.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_007", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Seorang warga datang pada menit-menit menjelang penutupan layanan dengan permohonan yang cukup kompleks. Anda sedang dalam kondisi lelah dan sebenarnya sudah ingin istirahat. Tindakan yang paling tepat adalah...",
    "options": ["Menutup layanan tepat waktu dan menyuruh warga besok pagi", "Melayani warga tersebut dengan tetap efisien, namun menjelaskan bagian mana yang perlu dilengkapi besok", "Melayani warga tanpa menyelesaikan dengan baik karena sudah lelah", "Menyalahkan warga yang datang terlambat", "Meminta warga datang besok tanpa memberikan informasi tambahan"],
    "answer": "B",
    "explanation": "Melayani warga dengan tetap efisien sambil menjelaskan bagian yang perlu dilengkapi besok menunjukkan profesionalisme yang menjunjung tinggi pelayanan publik meskipun dalam kondisi tidak ideal.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_008", "category": "TKP", "subcategory": "Pelayanan Publik",
    "question": "Seorang warga marah karena permohonannya ditolak karena alasan yang tidak jelas. Warga tersebut mengancam akan menyebarkan informasi negatif tentang kantor Anda di media sosial. Sebagai pimpinan, Anda sebaiknya...",
    "options": ["Melaporkan warga tersebut ke pihak berwajib karena telah mengancam", "Menjelaskan alasan penolakan secara transparan dan bantu warga menemukan solusi alternatif", "Mengabaikan ancaman karena dianggap tidak berdasar", "Langsung mengabulkan permintaan warga agar tidak menjadi masalah", "Menghubungi media terlebih dahulu untuk membela nama baik kantor"],
    "answer": "B",
    "explanation": "Menjelaskan alasan penolakan secara transparan dan membantu warga menemukan solusi alternatif adalah pendekatan terbaik. Ini menunjukkan profesionalisme, transparansi, dan orientasi pada penyelesaian masalah.",
    "difficulty": "medium"
  },
  # JARINGAN KERJA (7)
  {
    "id": "tkp3_009", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda bertugas di sebuah organisasi pemerintah daerah. Dalam rapat koordinasi dengan perangkat daerah lain, terdapat perbedaan pendapat tentang pembagian tugas. Sikap yang paling tepat adalah...",
    "options": ["Memaksakan pendapat sendiri karena merasa paling benar", "Mendengarkan semua pendapat dan mencari solusi yang mengakomodasi semua pihak", "Mendiamkan diri karena bukan tanggung jawab Anda", "Melaporkan perbedaan pendapat ke media agar menjadi perhatian publik", "Menolak berpartisipasi dalam rapat jika tidak sesuai keinginan"],
    "answer": "B",
    "explanation": "Mendengarkan semua pendapat dan mencari solusi yang mengakomodasi semua pihak mencerminkan semangat kebersamaan dan orientasi pelayanan dalam jejaring kerja. Ini membangun koordinasi yang efektif antar perangkat daerah.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_010", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda diminta bekerja sama dengan sebuah organisasi non-pemerintah dalam sebuah proyek pelayanan publik. Sikap yang tepat adalah...",
    "options": ["Menolak bekerja sama karena bukan mitra resmi pemerintah", "Menerima dengan terbuka dan menjelaskan batasan kerja sama yang saling menguntungkan", "Membiarkan pihak NGO menentukan semua rencana kerja", "Melakukan pengawasan ketat tanpa memberikan ruang diskusi", "Mengabaikan masukan dari pihak NGO karena perbedaan kepentingan"],
    "answer": "B",
    "explanation": "Menerima dengan terbuka dan menjelaskan batasan kerja sama yang saling menguntungkan mencerminkan pendekatan kolaboratif yang efektif. Ini membangun kemitraan yang produktif dan saling menghargai.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_011", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Dalam sebuah tim proyek lintas perangkat daerah, Anda merasa kurang dihargai oleh anggota lainnya. Kontribusi Anda sering tidak mendapat pengakuan. Tindakan yang paling tepat adalah...",
    "options": ["Menarik diri dari tim karena merasa tidak dihargai", "Membuat rekam jejak kontribusi untuk menunjukkan hasil kerja secara terstruktur", "Menggunakan media sosial untuk mengekspresikan ketidakpuasan", "Melaporkan masalah ke atasan tanpa konsultasi lebih dulu", "Mengambil alih semua tugas agar diakui kontribusinya"],
    "answer": "B",
    "explanation": "Membuat rekam jejak kontribusi untuk menunjukkan hasil kerja secara terstruktur adalah pendekatan yang konstruktif dan profesional. Ini membantu mengkomunikasikan nilai kontribusi tanpa konfrontasi.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_012", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda ditugaskan membangun jejaring dengan komunitas masyarakat di daerah kerja Anda. Yang paling penting dalam membangun jejaring yang efektif adalah...",
    "options": ["Mengumpulkan sebanyak mungkin kontak tanpa memperhatikan kualitas", "Menjalin hubungan berdasarkan kepercayaan dan manfaat bersama", "Mengidentifikasi siapa saja yang memiliki kepentingan terhadap program Anda", "Memaksa komunitas untuk mendukung program pemerintah", "Melakukan pendekatan dengan memberikan janji yang belum tentu dipenuhi"],
    "answer": "B",
    "explanation": "Menjalin hubungan berdasarkan kepercayaan dan manfaat bersama adalah kunci membangun jejaring kerja yang berkelanjutan. Ini menciptakan kolaborasi yang bermakna dan saling menguntungkan.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_013", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda diminta menjadi fasilitator dalam konflik antara dua perangkat daerah yang memiliki kepentingan bertentangan. Pendekatan yang paling efektif adalah...",
    "options": ["Menentukan pemenang konflik dan mendukung satu pihak", "Memfasilitasi dialog terbuka dan mencari solusi yang saling menguntungkan kedua belah pihak", "Mengambil alih semua keputusan agar tidak ada konflik", "Menyarankan kedua pihak untuk berkompromi tanpa memahami konteks", "Melaporkan ke pimpinan agar pimpinan yang menentukan"],
    "answer": "B",
    "explanation": "Memfasilitasi dialog terbuka dan mencari solusi yang saling menguntungkan adalah pendekatan terbaik dalam resolusi konflik. Ini menunjukkan kemampuan interpersonal dan orientasi pelayanan dalam membangun kolaborasi.",
    "difficulty": "hard"
  },
  {
    "id": "tkp3_014", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda diminta untuk membangun tim kerja yang anggotanya berasal dari berbagai instansi dengan latar belakang berbeda. Tantangan terbesar dalam situasi ini adalah...",
    "options": ["Memaksakan satu cara kerja yang sama untuk semua anggota tim", "Menciptakan lingkungan yang inklusif dan menghargai perbedaan sebagai kekuatan tim", "Membuat hierarki yang jelas agar tidak ada kebingungan", "Menghindari konflik dengan tidak memberikan tugas yang menantang", "Memilih anggota yang memiliki pemikiran serupa untuk efisiensi"],
    "answer": "B",
    "explanation": "Menciptakan lingkungan yang inklusif dan menghargai perbedaan memungkinkan tim memanfaatkan keberagaman untuk meningkatkan kreativitas dan inovasi. Ini adalah kunci keberhasilan tim lintas instansi.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_015", "category": "TKP", "subcategory": "Jejaring Kerja",
    "question": "Anda diminta memberikan pelatihan kepada rekan kerja yang belum lama bergabung di organisasi. Keputusan Anda sebaiknya adalah...",
    "options": ["Menolak karena bukan tugas utama Anda dan tidak ada kompensasi tambahan", "Mempersiapkan materi pelatihan dengan baik, memberikan pelatihan secara sabar, dan bersedia menjawab pertanyaan", "Menyalahkan kinerja rekan kerja baru yang belum maksimal", "Melakukan pelatihan asal-asalan agar cepat selesai", "Meminta bayaran tambahan untuk melakukan pelatihan"],
    "answer": "B",
    "explanation": "Mempersiapkan materi dengan baik, melatih dengan sabar, dan bersedia menjawab pertanyaan menunjukkan profesionalisme dan orientasi pada pengembangan kolektif. Ini membangun jaringan kerja yang solid.",
    "difficulty": "easy"
  },
  # SOSIAL BUDAYA (7)
  {
    "id": "tkp3_016", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda bertugas di sebuah daerah dengan tingkat toleransi antarumat beragama yang masih rendah. Dalam bekerja, Anda perlu menyikapi keberagaman dengan cara...",
    "options": ["Mengabaikan perbedaan dan fokus pada tugas administratif saja", "Menjunjung tinggi keberagaman sebagai kekuatan bangsa, bukan sebagai ancaman", "Menghormati hanya budaya mayoritas yang ada di daerah tersebut", "Menghindari interaksi dengan kelompok minoritas", "Menyamaratakan semua budaya tanpa penghargaan terhadap kekhasan"],
    "answer": "B",
    "explanation": "Menjunjung tinggi keberagaman sebagai kekuatan bangsa mencerminkan semangat Bhinneka Tunggal Ika. Ini penting dalam pelayanan publik untuk membangun masyarakat yang inklusif dan harmonis.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_017", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda bekerja di sebuah daerah dengan budaya lokal yang kuat. Kebijakan pemerintah pusat kadang tidak sepenuhnya sesuai dengan kearifan lokal yang ada. Pendekatan yang tepat adalah...",
    "options": ["Memaksakan program pemerintah pusat tanpa modifikasi apa pun", "Mencari cara mengintegrasikan program dengan kearifan lokal yang ada secara harmonis", "Menolak program yang tidak sesuai dengan kearifan lokal", "Melaporkan kearifan lokal ke pusat sebagai penghambat pembangunan", "Menghentikan semua program sampai ada kebijakan yang sepenuhnya sesuai"],
    "answer": "B",
    "explanation": "Mencari cara mengintegrasikan program dengan kearifan lokal mencerminkan kepekaan terhadap budaya dan kemampuan adaptasi. Ini memungkinkan program pemerintah berjalan efektif tanpa merusak nilai-nilai lokal.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_018", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Saat melakukan outreach ke masyarakat, Anda menghadapi resistensi dari tokoh adat yang merasa program Anda mengancam nilai-nilai mereka. Tindakan yang paling tepat adalah...",
    "options": ["Melaporkannya ke atasan agar tokoh adat tersebut diberikan teguran", "Mendengarkan kekhawatiran tokoh adat dan mencari solusi yang tidak mengancam nilai-nilai mereka", "Mengabaikan resistensi dan melanjutkan program sesuai rencana awal", "Menawarkan hadiah agar tokoh adat mendukung program", "Menghindari daerah tersebut sama sekali"],
    "answer": "B",
    "explanation": "Mendengarkan kekhawatiran dan mencari solusi yang tidak mengancam nilai-nilai mereka mencerminkan kepekaan terhadap budaya dan kemampuan komunikasi yang efektif. Ini memungkinkan kebijakan berjalan dengan dukungan masyarakat.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_019", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda bekerja sama dengan organisasi masyarakat sipil yang memiliki pandangan politik berbeda dari pemerintah. Tindakan terbaik Anda adalah...",
    "options": ["Menolak bekerja sama karena perbedaan pandangan politik", "Bekerja sama sesuai tugas pokok dengan mengesampingkan perbedaan pandangan politik", "Melaporkan organisasi tersebut kepada pihak berwajib", "Menyebarkan informasi negatif tentang organisasi tersebut", "Memaksa organisasi tersebut untuk mengubah pandangannya"],
    "answer": "B",
    "explanation": "Bekerja sama sesuai tugas pokok dengan mengesampingkan perbedaan pandangan politik mencerminkan profesionalisme tinggi. Ini menunjukkan kemampuan bekerja sama dengan berbagai pihak tanpa memedulikan perbedaan politik.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_020", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda diminta menangani proyek yang berkaitan dengan adat istiadat setempat yang tidak Anda kenal. Tindakan terbaik Anda adalah...",
    "options": ["Menolak karena tidak sesuai dengan kompetensi dan keahlian Anda", "Mempelajari adat istiadat setempat, berkonsultasi dengan tokoh masyarakat, dan menyesuaikan pendekatan", "Mengabaikan adat istiadat setempat dan menerapkan prosedur standar", "Meminta agar adat istiadat setempat dihapus dari proses", "Menyebarkan informasi tentang adat istiadat yang dianggap aneh"],
    "answer": "B",
    "explanation": "Mempelajari, berkonsultasi, dan menyesuaikan pendekatan menunjukkan profesionalisme dan kepekaan budaya. Ini penting untuk membangun kepercayaan masyarakat setempat.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_021", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda diminta bekerja dalam tim yang anggotanya berasal dari berbagai latar belakang suku dan agama. Sikap Anda sebaiknya...",
    "options": ["Hanya bekerja dengan anggota tim yang memiliki latar belakang sama", "Menghormati perbedaan setiap anggota tim dan fokus pada pencapaian tujuan bersama", "Memaksakan cara kerja sendiri yang dianggap paling baik", "Menghindari topik yang berkaitan dengan perbedaan latar belakang", "Membandingkan budaya setiap anggota tim secara terbuka di forum resmi"],
    "answer": "B",
    "explanation": "Menghormati perbedaan dan fokus pada tujuan bersama mencerminkan profesionalisme dan kemampuan bekerja dalam tim yang beragam. Ini penting dalam lingkungan kerja pemerintah yang multikultural.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_022", "category": "TKP", "subcategory": "Sosial Budaya",
    "question": "Anda ditugaskan ke daerah terpencil yang memiliki tradisi kerja berbeda dari yang Anda kenal. Kondisi ini memang menyulitkan, tetapi Anda tetap harus bekerja optimal. Sikap Anda sebaiknya...",
    "options": ["Bekerja secukupnya sambil terus memohon pindah ke daerah lain", "Beradaptasi dengan lingkungan baru dan memberikan pelayanan terbaik sesuai kondisi setempat", "Menolak penugasan dan tetap di tempat semula", "Bekerja dengan setengah hati karena tidak ada motivasi dan dukungan", "Meminta intensif tambahan sebelum bersedia bekerja"],
    "answer": "B",
    "explanation": "Beradaptasi dengan lingkungan baru dan memberikan pelayanan terbaik sesuai kondisi setempat menunjukkan kemampuan beradaptasi dan dedikasi profesional. Ini mencerminkan semangat nasionalisme dalam pengabdian.",
    "difficulty": "medium"
  },
  # TIK (8)
  {
    "id": "tkp3_023", "category": "TKP", "subcategory": "TIK",
    "question": "Kebijakan baru dari pemerintah daerah mengharuskan semua layanan dilakukan secara elektronik melalui sistem informasi. Anda yang belum familiar dengan teknologi akan...",
    "options": ["Menolak kebijakan dan tetap menggunakan cara lama", "Mengikuti pelatihan dan mempelajari sistem elektronik secara mandiri dengan tekun", "Meminta rekan kerja untuk mengerjakan layanan Anda", "Melapor ke media bahwa kebijakan ini tidak realistis", "Melakukan layanan elektronik tetapi asal-asalan agar cepat selesai"],
    "answer": "B",
    "explanation": "Mengikuti pelatihan dan belajar secara mandiri menunjukkan keterbukaan dan tanggung jawab profesional. Kemampuan beradaptasi terhadap perubahan kebijakan dan teknologi adalah kunci keberhasilan dalam pelayanan publik.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_024", "category": "TKP", "subcategory": "TIK",
    "question": "Anda menerima surat elektronik dari pengirim yang tidak dikenal dengan lampiran yang mencurigakan. Tindakan yang tepat adalah...",
    "options": ["Membuka lampiran karena mungkin berisi informasi penting", "Memverifikasi pengirim terlebih dahulu sebelum membuka lampiran tersebut", "Meneruskan surat elektronik tersebut ke semua rekan kerja", "Mengabaikan surat elektronik tersebut tanpa membukanya", "Menghapus surat elektronik tanpa memeriksa isinya"],
    "answer": "B",
    "explanation": "Memverifikasi pengirim terlebih dahulu sebelum membuka lampiran adalah praktik keamanan teknologi informasi yang baik. Ini melindungi sistem dari ancaman potensial seperti virus atau phishing.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_025", "category": "TKP", "subcategory": "TIK",
    "question": "Anda diminta memperkenalkan teknologi baru kepada rekan kerja yang belum familiar. Pendekatan terbaik Anda adalah...",
    "options": ["Menyerahkan perangkat dan membiarkan rekan kerja belajar sendiri", "Menyiapkan materi pelatihan yang mudah dipahami dan membimbing secara bertahap", "Menyalahkan rekan kerja karena tidak bisa menggunakan teknologi", "Melaporkan kepada atasan bahwa rekan kerja tidak mampu", "Menggunakan teknologi tersebut sendiri tanpa mengajarkan orang lain"],
    "answer": "B",
    "explanation": "Menyiapkan materi pelatihan yang mudah dipahami dan membimbing secara bertahap menunjukkan kemampuan komunikasi dan kepedulian terhadap pengembangan tim. Ini membantu transisi teknologi yang efektif.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_026", "category": "TKP", "subcategory": "TIK",
    "question": "Anda mengelola sebuah basis informasi yang berisi informasi warga yang sangat sensitif. Standar keamanan yang harus diterapkan adalah...",
    "options": ["Memberikan akses terbuka untuk semua karyawan karena saling membutuhkan dalam tim", "Menerapkan prinsip need-to-know dengan enkripsi data dan audit trail", "Menyimpan informasi tanpa kata sandi karena dianggap aman secara fisik", "Membackup informasi ke penyimpanan berbasis awan publik tanpa enkripsi", "Menghapus semua informasi sensitif untuk menghindari risiko sepenuhnya"],
    "answer": "B",
    "explanation": "Menerapkan prinsip need-to-know dengan enkripsi dan audit trail adalah standar keamanan informasi yang baik. Ini melindungi privasi warga sekaligus memungkinkan akses yang diperlukan untuk tugas resmi.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_027", "category": "TKP", "subcategory": "TIK",
    "question": "Anda ditugaskan membuat presentasi elektronik untuk rapat penting dengan stakeholder. Anda belum pernah membuat presentasi elektronik sebelumnya. Langkah terbaik Anda adalah...",
    "options": ["Menolak karena tidak mampu dan tidak sesuai keahlian", "Mempelajari aplikasi presentasi, berlatih sebelum acara, dan menyampaikannya dengan percaya diri", "Meminta rekan kerja lain untuk menggantikan Anda", "Menyalahkan penyelenggara yang memaksakan presentasi elektronik", "Melakukan presentasi asal-asalan karena bukan keahlian Anda"],
    "answer": "B",
    "explanation": "Mempelajari aplikasi, berlatih sebelum acara, dan menyampaikannya dengan percaya diri menunjukkan profesionalisme dan keberanian untuk berkembang. Literasi teknologi mendorong seseorang untuk menghadapi tantangan baru.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_028", "category": "TKP", "subcategory": "TIK",
    "question": "Anda menemukan sebuah celah sistem yang dapat mengancam informasi sensitif warga. Memperbaikinya memerlukan waktu dan anggaran tambahan. Tindakan yang paling bertanggung jawab adalah...",
    "options": ["Mengabaikan karena belum ada gangguan yang terjadi dan sistem masih berjalan", "Mengamankan sistem sementara sambil menyusun rencana perbaikan secara bertahap", "Menyalahkan pihak IT karena tidak membuat sistem yang sempurna", "Menutup akses sistem sampai diperbaiki sepenuhnya untuk menghindari risiko", "Membiarkan warga tahu tentang kerentanan tanpa perbaikan untuk transparansi"],
    "answer": "B",
    "explanation": "Mengamankan sistem sementara sambil menyusun rencana perbaikan bertahap mencerminkan keseimbangan antara respons terhadap risiko dan kelanjutan layanan. Ini menunjukkan tanggung jawab dan manajemen risiko yang baik.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_029", "category": "TKP", "subcategory": "TIK",
    "question": "Anda diminta untuk mengevaluasi sebuah aplikasi pelayanan publik yang baru dikembangkan. Kriteria terpenting dalam evaluasi adalah...",
    "options": ["Kecanggihan teknologi yang digunakan tanpa memandang kemudahan penggunaan", "Kemudahan penggunaan bagi warga dan keamanan informasi data", "Biaya pengembangan tanpa memperhatikan dampak terhadap masyarakat", "Kecepatan pengembangan tanpa mempertimbangkan kualitas dan keandalan", "Popularitas aplikasi di media sosial dan platform digital"],
    "answer": "B",
    "explanation": "Kemudahan penggunaan bagi warga dan keamanan informasi data adalah kriteria terpenting untuk aplikasi pelayanan publik. Ini memastikan warga dapat menggunakan aplikasi dengan efektif sementara data mereka terlindungi.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_030", "category": "TKP", "subcategory": "TIK",
    "question": "Anda diminta membuat laporan elektronik yang harus dipresentasikan secara virtual kepada seluruh stakeholder. Yang sebaiknya Anda persiapkan adalah...",
    "options": ["Menolak karena tidak familiar dengan presentasi virtual", "Mempelajari sistem presentasi virtual, mempersiapkan materi visual yang jelas, dan melakukan uji coba teknis sebelum sesi", "Hanya membuat slide tanpa mempersiapkan aspek teknis presentasi virtual", "Menyalahkan teknologi yang tidak mendukung presentasi", "Meminta orang lain menggantikan dalam presentasi karena bukan keahlian Anda"],
    "answer": "B",
    "explanation": "Mempersiapkan sistem virtual, materi visual yang jelas, dan uji coba teknis menunjukkan profesionalisme dalam berkomunikasi secara elektronik. Ini memastikan presentasi berjalan lancar dan efektif.",
    "difficulty": "medium"
  },
  # PROFESIONALISME (8)
  {
    "id": "tkp3_031", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda diminta memimpin tim untuk menyelesaikan tugas yang belum pernah Anda kerjakan sebelumnya. Langkah pertama yang paling tepat adalah...",
    "options": ["Menolak karena tidak sesuai kemampuan dan keahlian", "Mempelajari informasi tentang tugas tersebut, mengidentifikasi sumber daya, dan membuat rencana kerja", "Menyerahkan sepenuhnya kepada anggota tim tanpa koordinasi", "Melakukan apa yang dianggap terbaik tanpa perencanaan", "Menunggu sampai ada instruksi lebih lanjut dari atasan"],
    "answer": "B",
    "explanation": "Mempelajari informasi, mengidentifikasi sumber daya, dan menyusun rencana kerja adalah langkah pertama yang tepat dalam memimpin tugas baru. Ini menunjukkan profesionalisme dan kepemimpinan yang terencana.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_032", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda diminta membuat laporan tentang topik yang tidak Anda kuasai. Langkah terbaik Anda adalah...",
    "options": ["Menolak karena tidak menguasai topik tersebut", "Mempelajari topik tersebut, menghimpun informasi dari berbagai sumber, dan menyusun laporan berdasarkan fakta", "Menyalin laporan orang lain yang sudah ada", "Menyampaikan bahwa Anda tidak mampu kepada atasan", "Meminta atasan menunjuk orang lain untuk mengerjakan"],
    "answer": "B",
    "explanation": "Mempelajari topik baru, menghimpun informasi, dan menyusun laporan berdasarkan fakta menunjukkan inisiatif dan kemampuan belajar yang tinggi. Ini mencerminkan profesionalisme sejati.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_033", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda melihat bahwa metode kerja Anda saat ini kurang efisien dan sudah waktunya untuk diperbaiki. Namun tidak ada yang memintanya. Yang sebaiknya Anda lakukan adalah...",
    "options": ["Menunggu sampai ada yang memintanya karena bukan prioritas", "Menganalisis metode baru, menyusun proposal perbaikan, dan menyampaikannya kepada atasan", "Tetap menggunakan metode lama karena sudah terbiasa dan berjalan", "Melaporkan metode lama yang digunakan rekan kerja lain", "Menyalahkan sistem yang tidak mendukung perbaikan"],
    "answer": "B",
    "explanation": "Menganalisis metode baru, menyusun proposal, dan menyampaikannya kepada atasan menunjukkan proaktif dan orientasi pada peningkatan berkelanjutan. Profesionalisme sejati mendorong perbaikan tanpa perlu diminta.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_034", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda diminta menyelesaikan tugas dalam waktu yang menurut Anda tidak realistis. Langkah terbaik adalah...",
    "options": ["Langsung menolak dan mengatakan tidak mungkin bisa diselesaikan", "Menerima tantangan, mengidentifikasi sumber daya yang dibutuhkan, dan bernegosiasi jadwal yang lebih realistis jika diperlukan", "Menyelesaikan asal-asalan agar selesai cepat", "Meminta seseorang lain untuk mengerjakannya", "Mengabaikan tenggat waktu dan menyelesaikan sesuai kenyamanan sendiri"],
    "answer": "B",
    "explanation": "Menerima tantangan, mengidentifikasi sumber daya, dan bernegosiasi secara profesional menunjukkan proaktif dan kemampuan komunikasi. Ini mencari solusi daripada langsung menolak.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_035", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda diminta menilai kinerja rekan kerja yang belum memenuhi standar yang ditetapkan. Tindakan terbaik Anda adalah...",
    "options": ["Memberikan penilaian terbaik agar rekan tidak kecewa dan hubungan baik terjaga", "Memberikan penilaian jujur sesuai fakta dan memberikan masukan konstruktif untuk perbaikan", "Memberikan penilaian buruk agar Anda terlihat lebih baik dalam perbandingan", "Meminta rekan kerja untuk menyuap agar penilaian menjadi baik", "Menolak memberikan penilaian karena terlalu sensitif untuk dilakukan"],
    "answer": "B",
    "explanation": "Memberikan penilaian jujur sesuai fakta dan memberikan masukan konstruktif untuk perbaikan membantu rekan berkembang tanpa mengorbankan kejujuran. Ini menunjukkan profesionalisme dan integritas.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_036", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda ditugaskan membuat proyek pelayanan publik dengan anggaran terbatas. Masyarakat berharap hasil proyek dapat menyelesaikan masalah mereka. Strategi yang paling tepat adalah...",
    "options": ["Menunda proyek sampai ada anggaran yang memadai", "Membuat proyek yang menghasilkan dampak nyata terbesar dengan anggaran yang ada", "Mengurangi ruang lingkup proyek tanpa komunikasi dengan masyarakat", "Menyerahkan tanggung jawab kepada pihak ketiga tanpa koordinasi", "Menggunakan seluruh anggaran untuk bagian yang paling terlihat saja"],
    "answer": "B",
    "explanation": "Membuat proyek yang menghasilkan dampak nyata terbesar dengan anggaran yang ada menunjukkan kemampuan mengelola sumber daya secara efisien dan tetap mengutamakan kebutuhan masyarakat.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_037", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda telah beberapa kali gagal mencapai target kinerja. Sikap terbaik Anda adalah...",
    "options": ["Menyerah karena memang tidak mampu mencapai target", "Menganalisis penyebab kegagalan, mengevaluasi strategi, dan menyusun rencana perbaikan yang lebih realistis", "Menyalahkan kondisi eksternal atas kegagalan yang terjadi", "Meminta target diturunkan agar lebih mudah dicapai", "Berpura-pura telah mencapai target untuk memenuhi ekspektasi"],
    "answer": "B",
    "explanation": "Menganalisis penyebab kegagalan, mengevaluasi strategi, dan menyusun rencana perbaikan menunjukkan ketangguhan dan orientasi pada peningkatan. Ini mencerminkan profesionalisme sejati yang tidak menyerah.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_038", "category": "TKP", "subcategory": "Profesionalisme",
    "question": "Anda diminta memberikan evaluasi terhadap sistem kerja yang telah berjalan selama 5 tahun. Tanggapan terbaik Anda adalah...",
    "options": ["Menyatakan bahwa sistem sudah baik karena sudah berjalan lama dan stabil", "Menganalisis kelebihan dan kekurangan, memberikan rekomendasi perbaikan dengan informasi yang mendukung", "Menyalahkan sistem lama agar sistem baru disahkan tanpa pertimbangan", "Menyatakan bahwa evaluasi bukan tugas dan tanggung jawab Anda", "Menggunakan evaluasi untuk menyerang kompetitor internal"],
    "answer": "B",
    "explanation": "Menganalisis kelebihan dan kekurangan serta memberikan rekomendasi perbaikan dengan informasi yang mendukung menunjukkan orientasi pada peningkatan berkelanjutan. Ini profesionalisme sejati.",
    "difficulty": "medium"
  },
  # INTEGRITAS DIRI (7)
  {
    "id": "tkp3_039", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda ditawari sebuah hadiah oleh vendor sebagai ucapan terima kasih atas layanan yang telah Anda berikan. Hadiah tersebut memiliki nilai yang cukup besar. Tindakan yang paling tepat adalah...",
    "options": ["Menerima karena dianggap sebagai bentuk apresiasi yang wajar dan lumrah", "Menolak dengan sopan dan menjelaskan bahwa menerima hadiah dari vendor tidak diperbolehkan sesuai aturan", "Menerima dan membagikan kepada kolega karena bukan untuk Anda sendiri", "Menerima dan tidak memberitahu siapa pun agar tidak menjadi masalah", "Menolak karena dianggap tidak menghargai vendor sebagai mitra"],
    "answer": "B",
    "explanation": "Menolak dengan sopan dan menjelaskan aturan yang berlaku mencerminkan integritas dan kepatuhan terhadap pemberantasan korupsi. Ini melindungi profesionalisme dan menghindari konflik kepentingan.",
    "difficulty": "easy"
  },
  {
    "id": "tkp3_040", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda mengetahui bahwa seorang atasan langsung Anda meminta Anda untuk membuat informasi palsu dalam laporan kinerja. Tindakan Anda yang paling sesuai adalah...",
    "options": ["Melakukan sesuai permintaan karena itu adalah perintah atasan langsung", "Menolak dan menjelaskan alasan dengan informasi yang mendukung posisi Anda secara tegas", "Melakukan karena Anda juga merasa tertekan untuk menunjukkan hasil", "Melaporkannya ke media karena tidak ada saluran pelaporan internal yang efektif", "Mengabaikan permintaan dan melanjutkan seolah tidak ada permintaan"],
    "answer": "B",
    "explanation": "Menolak dan menjelaskan alasan dengan tegas mencerminkan integritas dan keberanian untuk melakukan hal yang benar. Ini menunjukkan kemampuan komunikasi yang baik dan menjunjung tinggi kebenaran.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_041", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda bekerja dalam sebuah lingkungan di mana banyak terjadi pemborosan anggaran negara. Anda merasa tidak seharusnya ikut tetapi juga takut menjadi sasaran jika sampaikan pendapat. Pendekatan terbaik adalah...",
    "options": ["Ikut serta karena semua orang juga melakukan dan tidak ada salahnya", "Membuat laporan internal tentang pemborosan dan sampaikan ke saluran yang sesuai secara anonim", "Mengabaikan karena bukan tanggung jawab Anda untuk melaporkan", "Berbicara terbuka tanpa bukti di depan umum", "Melakukan pemborosan yang sama agar tidak menjadi target"],
    "answer": "B",
    "explanation": "Membuat laporan internal secara anonim mencerminkan keberanian bermoral dan pendekatan strategis. Ini memungkinkan tindakan perbaikan tanpa mengorbankan keamanan diri sendiri.",
    "difficulty": "hard"
  },
  {
    "id": "tkp3_042", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda mengetahui bahwa terdapat pembengkakan anggaran dalam proposal yang disusun oleh tim Anda. Sebagai penanggung jawab, Anda sebaiknya...",
    "options": ["Mengabaikan karena bukan inisiatif Anda dan bukan tanggung jawab Anda", "Melaporkan temuan tersebut dan mengkoreksi proposal sebelum diajukan", "Ikut memanfaatkan pembengkakan anggaran untuk kepentingan tim", "Menyebarkan informasi tersebut ke publik tanpa melalui jalur resmi", "Menyembunyikan temuan dan mengajukan proposal apa adanya"],
    "answer": "B",
    "explanation": "Melaporkan dan mengkoreksi sebelum diajukan menunjukkan tanggung jawab dan komitmen terhadap penggunaan anggaran yang benar. Ini integritas sejati dalam pengelolaan keuangan negara.",
    "difficulty": "hard"
  },
  {
    "id": "tkp3_043", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda diminta untuk memberikan presentasi tentang pencapaian proyek yang sebenarnya tidak berhasil sesuai target. Presentasi harus tetap menarik untuk menjaga atmosfer yang positif. Pendekatan terbaik adalah...",
    "options": ["Memalsukan informasi untuk menunjukkan hasil yang tidak sesuai kenyataan", "Menyampaikan fakta dengan jujur termasuk hambatan yang dihadapi dan pelajaran yang diambil", "Menghindari membicarakan angka-angka yang tidak tercapai", "Menyalahkan pihak lain untuk ketidakberhasilan proyek", "Tidak memberikan presentasi karena tidak ada yang baik untuk dilaporkan"],
    "answer": "B",
    "explanation": "Menyampaikan fakta dengan jujur termasuk hambatan dan pelajaran yang diambil mencerminkan integritas dalam komunikasi. Ini membangun kepercayaan dan memungkinkan perbaikan berkelanjutan.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_044", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Anda mengetahui bahwa seorang teman kerja memiliki masalah dengan alkohol yang mempengaruhi kinerjanya di kantor. Sebagai teman yang baik, tindakan yang paling tepat adalah...",
    "options": ["Mengabaikan karena itu adalah masalah pribadi teman yang bukan urusan Anda", "Menyarankan teman untuk mencari bantuan profesional dengan penuh empati dan tanpa menghakimi", "Melaporkannya ke atasan agar teman tersebut diberikan sanksi tegas", "Memberitahu semua kolega agar mereka memperingatkan teman tersebut", "Menyindir teman di depan umum agar menyadari masalahnya"],
    "answer": "B",
    "explanation": "Menyarankan teman mencari bantuan profesional dengan empati mencerminkan kepedulian yang tulus dan pendekatan yang konstruktif. Ini membantu teman menyelesaikan masalah tanpa mempermalukan.",
    "difficulty": "medium"
  },
  {
    "id": "tkp3_045", "category": "TKP", "subcategory": "Integritas Diri",
    "question": "Pada saat bersamaan, Anda menerima kritik dari atasan dan keluhan dari warga. Tekanan dari dua arah yang berbeda membuat Anda merasa terjepit. Yang sebaiknya Anda lakukan adalah...",
    "options": ["Melampiaskan emosi kepada salah satu pihak yang paling lemah", "Menenangkan diri, memprioritaskan tugas berdasarkan urgensi, dan menangani satu per satu secara terstruktur", "Mengabaikan semua dan mengambil cuti untuk memulihkan diri", "Menyalahkan pihak ketiga atas situasi yang terjadi", "Menyerah dan menyatakan tidak mampu menangani situasi ini"],
    "answer": "B",
    "explanation": "Menenangkan diri, memprioritaskan berdasarkan urgensi, dan menangani satu per satu menunjukkan kemampuan mengelola tekanan secara terstruktur. Ini integritas diri dalam menghadapi tekanan berganda.",
    "difficulty": "medium"
  }
]

# ============================================================
# WRITE ALL FILES
# ============================================================
base = "C:/Users/muham/tryout_cpns/assets/questions"

with open(f"{base}/twk_3.json", "w", encoding="utf-8") as f:
    json.dump(twk3, f, ensure_ascii=False, indent=2)
print(f"twk_3.json written: {len(twk3)} questions")

with open(f"{base}/tiu_3.json", "w", encoding="utf-8") as f:
    json.dump(tiu3, f, ensure_ascii=False, indent=2)
print(f"tiu_3.json written: {len(tiu3)} questions")

with open(f"{base}/tkp_3.json", "w", encoding="utf-8") as f:
    json.dump(tkp3, f, ensure_ascii=False, indent=2)
print(f"tkp_3.json written: {len(tkp3)} questions")

# Verify counts
print("\nVerification:")
for name, data in [("twk3", twk3), ("tiu3", tiu3), ("tkp3", tkp3)]:
    cats = {}
    for q in data:
        cats[q["category"]] = cats.get(q["category"], 0) + 1
    print(f"  {name}: total={len(data)}, by_category={cats}")

# Print first 2 of each
print("\n=== TWK3 First 2 ===")
for q in twk3[:2]:
    print(f"  [{q['id']}] {q['subcategory']} | {q['question'][:80]}...")
    print(f"  Answer: {q['answer']}")

print("\n=== TIU3 First 2 ===")
for q in tiu3[:2]:
    print(f"  [{q['id']}] {q['subcategory']} | {q['question'][:80]}...")
    print(f"  Answer: {q['answer']}")

print("\n=== TKP3 First 2 ===")
for q in tkp3[:2]:
    print(f"  [{q['id']}] {q['subcategory']} | {q['question'][:80]}...")
    print(f"  Answer: {q['answer']}")
