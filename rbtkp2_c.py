import json

with open('assets/questions/tkp_2.json', encoding='utf-8') as f:
    data = json.load(f)

tik = [
    {
        "id": "tkp2_023", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengelola sistem informasi pelayanan publik yang menangani data sensitif warga: NIK, alamat, status ekonomi. Sistem terhubung dengan berbagai platform digital dan digunakan ratusan petugas. Audit security menemukan vulnerability serius: beberapa akun petugas memiliki password sangat lemah dan tidak ada two-factor authentication. Implementasi upgrade memerlukan budget yang tidak ada di pos anggaran tahun ini dan waktu minimal 6 bulan. Beberapa attempted breach oleh pihak tidak dikenal sudah terjadi. Position Anda adalah...",
        "options": [
            "Lakukan upgrade security secepatnya dengan mencari budget dari pos lain atau meminta tambahan budget khusus ke atasan, karena data sensitif warga tidak bisa ditunggu 6 bulan untuk diamankan",
            "Tunda implementasi upgrade sampai anggaran tersedia karena proses procurement mengikuti aturan yang tidak bisa dilanggar, dan untuk sementara terapkan security measures tambahan secara manual",
            "Segera nonaktifkan semua akun dengan password lemah dan minta reset dengan requirement lebih kuat, lakukan bertahap dalam 2 minggu, namun biarkan sistem tetap berjalan",
            "Pindahkan semua sistem ke cloud service provider yang sudah memiliki security compliance lengkap karena akan lebih murah dan lebih cepat",
            "Buat kebijakan baru yang mewajibkan password kuat, namun implementasinya rely pada sukarela petugas karena memaksa reset masif akan mengganggu pelayanan"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan sense of urgency terhadap risiko keamanan data sensitif. Dengan mencari budget dari pos lain atau meminta budget khusus, tidak ada alasan untuk tidak mengambil langkah konkret. Bukan B yang pasif menunggu, bukan C yang terlalu reaktif tanpa rencana sistemik, bukan D yang migrasi tanpa assessment menyeluruh, bukan E yang kebijakan tanpa enforcement.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_024", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengelola sistem e-government yang sudah beroperasi 3 tahun. Sistem mulai mengalami degrade performance signifikan dan sering down. Vendor yang membuat sistem tidak responsif terhadap maintenance request karena kontrak sudah berakhir dan mereka menolak memperbarui karena negosiasi harga tidak mencapai kesepakatan. Pengguna mulai mengeluh dan produktivitas menurun drastis. Anda perlu keputusan cepat.",
        "options": [
            "Minta budget untuk hire new vendor dan migrasi sistem ke platform baru karena vendor lama tidak bisa dipercaya dan sistem sudah obsolete",
            "Coba negosiasi ulang dengan vendor lama dengan menawarkan harga lebih tinggi agar mereka mau melanjutkan maintenance",
            "Audit internally untuk menentukan akar masalah performance, lalu sampaikan findings ke vendor lama dengan ultimatum: perbaikan dalam 30 hari atau kontrak diakhiri dan dilakukan tender terbuka untuk vendor baru",
            "Patch sistem sendiri dengan tim internal karena upgrade minor mungkin cukup dan tidak perlu melibatkan vendor eksternal",
            "Biarkan sistem berjalan seperti sekarang karena semua sistem eventually down dan ini normal"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme dalam management vendor: tidak langsung memutuskan hubungan tanpa dasar yang jelas, memberikan kesempatan perbaikan dengan ultimatum yang jelas, dan memiliki exit strategy terencana. Pendekatan ini melindungi kepentingan institusional sambil memberikan fair chance pada vendor lama.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_025", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengimplementasikan sistem digital baru untuk pelayanan publik. Sistem berjalan 3 bulan dan secara teknis berfungsi dengan baik. Namun sebagian warga terutama yang lebih tua sangat kesulitan menggunakan sistem dan mulai mengeluh bahwa pelayanan publik sekarang lebih sulit dijangkau. Beberapa petugas lapangan juga tidak nyaman dengan sistem baru karena sudah terbiasa dengan cara lama dan merasa sistem baru memperlambat kerja mereka. Anda tahu sistem digital adalah arah kebijakan pemerintah pusat, tapi kenyataan di lapangan menunjukkan segment masyarakat justru semakin tertinggal.",
        "options": [
            "Lakukan evaluasi menyeluruh terhadap sistem digital, identifikasi pain points pengguna, kembangkan jalur alternatif yang tetap bisa diakses sambil secara gradual meningkatkan literasi digital pengguna, dan sampaikan findings ke pusat sebagai rekomendasi kebijakan",
            "Kembali ke sistem manual sepenuhnya karena sistem digital ternyata tidak cocok untuk semua kalangan",
            "Paksa semua warga dan petugas menggunakan sistem digital sepenuhnya karena transisi digital irreversibel dan siapa tidak adapt akan tertinggal",
            "Serahkan tanggung jawab literasi digital kepada warga sendiri karena pemerintah tidak bisa mengajarkan semua orang menggunakan teknologi",
            "Pilih warga yang bisa menggunakan sistem dan hanya layani mereka secara digital, untuk yang tidak bisa serahkan ke organisasi sosial"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan pendekatan human-centered yang nuanced: tidak menolak digitalisasi tapi juga tidak memaksakan sistem yang tidak accessible secara universal. Dual-track approach memastikan nobody left behind sambil mengarah ke digitalisasi. Evaluasi berbasis data dan rekomendasi ke pusat memastikan kebijakan future lebih inklusif.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_026", "category": "TKP", "subcategory": "TIK",
        "question": "Anda diminta menjadi panelis dalam forum tentang implementasi teknologi AI dalam pelayanan publik. Dalam persiapan, Anda menemukan bahwa sebagian besar implementasi AI di pemerintahan globally masih bersifat eksperimental dan banyak yang gagal memberikan hasil yang diharapkan, bahkan beberapa menimbulkan bias terhadap kelompok minoritas karena training data tidak representative. Namun di sisi lain, AI memiliki potensi besar untuk meningkatkan efisiensi dan akurasi pelayanan. Beberapa vendor teknologi mendorong implementasi AI di institusi Anda. Position Anda dalam forum adalah...",
        "options": [
            "Sampaikan bahwa implementasi AI harus dilakukan secara bertahap dengan pilot projects yang ketat, evaluasi bias secara berkala, melibatkan komunitas yang terdampak dalam design process, dan tidak boleh menggantikan keputusan manusia yang bersifat krusial, sambil mengakui potensi AI namun juga tantangan nyata",
            "Sampaikan bahwa AI dalam pelayanan publik pada dasarnya bermasalah karena pemerintah tidak memiliki keahlian dan infrastruktur untuk mengelola sistem AI yang kompleks",
            "Sampaikan bahwa AI adalah masa depan dan harus diadopsi segera karena institusi yang tidak mengadopsi AI akan tertinggal",
            "Sampaikan bahwa keputusan implementasi AI bukan domain Anda sebagai panelis dan serahkan kepada decision makers",
            "Sampaikan bahwa AI hanya boleh digunakan untuk tugas repetitif dan low-stakes, untuk keputusan yang berdampak pada kehidupan warga harus tetap menggunakan human judgment"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan pemahaman balanced tentang AI implementation: mengakui potensi, tidak naif tentang risiko, dan menekankan human-in-the-loop principle. Pendekatan pilot-based dengan evaluasi berkala adalah responsible innovation.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_027", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengelola database critical infrastruktur daerah. Dalam audit security, Anda menemukan bahwa salah satu staff IT dengan akses level tertinggi ke database tersebut adalah saudara kandung dari kontraktor besar yang secara rutin memenangkan tender dari instansi Anda. Staff tersebut memiliki akses ke data procurement, perencanaan proyek, dan informasi sensitif lainnya. Tidak ada bukti bahwa dia menyalahgunakan akses tersebut, tapi ada konflik kepentingan yang jelas.",
        "options": [
            "Segera nonaktifkan akses staff tersebut dan reassign ke posisi tanpa akses ke data sensitif, karena konflik kepentingan sudah cukup grounds untuk tidak memberikan akses kritis",
            "Investigasi lebih lanjut untuk memastikan apakah ada penyalahgunaan akses yang terjadi, dan selama investigation, kurangi level akses staff tersebut ke tingkat minimal yang diperlukan untuk tugas sehari-hari",
            "Panggil staff tersebut dan sampaikan bahwa Anda mengetahui hubungan familinya dengan kontraktor dan minta dia membuat signed declaration bahwa dia tidak akan menggunakan aksesnya untuk kepentingan kontraktor, dengan konsekuensi pemecatan jika terbukti pelanggaran",
            "Tidak mengambil tindakan apapun karena tidak ada bukti penyalahgunaan dan berdasarkan hukum ketenagakerjaan Anda tidak bisa melakukan diskriminasi terhadap staff berdasarkan hubungan keluarga",
            "Lapor ke inspektorat dan minta guidance karena situasi ini kompleks dan Anda tidak ingin mengambil keputusan yang bisa digunakan sebagai dasar untuk menggugat Anda"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan pendekatan berbasis bukti yang adil: tidak langsung menghukum tanpa bukti tapi juga tidak diam saja. Pengurangan akses sementara adalah langkah prudent yang melindungi institusi sambil menghormati hak staff yang belum terbukti bersalah. Investigasi akan memberikan clarity.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_028", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengelola sistem informasi terintegrasi dengan sistem nasional. Anda menemukan vulnerability yang bisa membahayakan data warga nasional jika dieksploitasi oleh pihak tidak berwenang. Anda sudah memperbaiki secara internal tapi ingin melaporkan ke BSSN untuk koordinasi nasional. Namun Anda tahu bahwa melaporkan berarti expose vulnerability yang ada di sistem Anda, dan ini bisa digunakan oleh pihak internal tertentu untuk menilai kinerja Anda secara negatif. Di sisi lain, tidak melaporkan berarti tidak berkontribusi pada keamanan siber nasional.",
        "options": [
            "Laporkan vulnerability ke BSSN beserta steps yang sudah diambil untuk perbaikan, karena keamanan siber nasional lebih penting dari concern personal tentang kinerja Anda",
            "Tidak perlu melaporkan karena Anda sudah fixing internally dan tidak ada eksploitasi yang terjadi, laporan ke BSSN hanya akan menimbulkan masalah bagi Anda sendiri tanpa manfaat nyata",
            "Laporkan ke BSSN tapi sembunyikan identity dari sistem Anda karena Anda tetap berkontribusi pada keamanan nasional tanpa mengorbankan posisi Anda sendiri",
            "Konsultasi dulu dengan atasan langsung sebelum membuat keputusan apapun karena ini keputusan strategik yang harus melibatkan leadership",
            "Buat anonymous report ke BSSN tanpa mencantumkan identity organisasi Anda"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas terhadap tanggung jawab keamanan nasional. Vulnerability yang sudah difix bukan kelemahan yang perlu disembunyikan tapi demonstrasi respons yang baik. Laporan ke BSSN justru menunjukkan profesionalisme karena berkontribusi pada threat intelligence nasional.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_029", "category": "TKP", "subcategory": "TIK",
        "question": "Anda diminta menyusun SOP baru untuk pengelolaan data dan informasi digital di instansi. SOP harus mengatur classification data, access control, data retention, dan disposal procedure. Anda tahu SOP terlalu rigid akan menyulitkan workflow dan tidak akan dipatuhi. Tapi SOP terlalu loose akan meningkatkan risiko keamanan data. Ada pressure dari berbagai unit untuk membuat SOP sesuai kebutuhan masing-masing.",
        "options": [
            "Buat SOP yang adaptif dengan principle-based framework yang menetapkan minimum standards yang harus dipenuhi semua unit, namun berikan fleksibilitas kepada masing-masing unit untuk menambahkan controls tambahan sesuai kebutuhan spesifik, dengan review berkala untuk memastikan kepatuhan",
            "Buat SOP yang uniform dan strict berlaku sama untuk semua unit karena consistency adalah kunci keamanan",
            "Serahkan ke masing-masing unit untuk membuat SOP mereka sendiri karena mereka paling tahu kebutuhan masing-masing",
            "Adopsi saja SOP dari instansi lain yang sudah terbukti berhasil karena tidak perlu reinvent the wheel",
            "Buat SOP yang sangat detail dan lengthy yang mencakup setiap possible scenario agar tidak ada celah yang tidak terlindungi"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan pemahaman sophisticated tentang governance: minimum standards memastikan consistency dan protection baseline, sementara flexibility mengakomodasi variasi legitimate workflow. Principle-based approach lebih robust karena tidak bisa di-game. Review berkala memastikan SOP tetap relevant dan dipatuhi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_030", "category": "TKP", "subcategory": "TIK",
        "question": "Anda mengelola divisi IT dan sedang mengevaluasi apakah perlu migrates seluruh sistem operasional ke cloud computing. Vendor cloud menawarkan kontrak 5 tahun dengan harga menarik. Namun audit internal menemukan bahwa sebagian data operasional instansi mengandung informasi sensitif yang belum pernah di-audit untuk kepatuhan terhadap standar keamanan tertentu. Migrasi cloud akan memindahkan data ke servers di luar kendali langsung instansi. Di waktu bersamaan, infrastruktur IT internal Anda sudah mulai uzur dan maintenance cost meningkat signifikan setiap tahun.",
        "options": [
            "Migrate ke cloud sesuai kontrak vendor karena efisiensi biaya jangka panjang lebih penting dan vendor cloud sudah memiliki security standards yang lebih baik dari infrastruktur internal yang uzur",
            "Tunda migrasi cloud sampai audit menyeluruh selesai dan semua compliance requirements terpenuhi, namun mulai planning untuk upgrade infrastruktur internal sebagai interim solution",
            "Migrasi hanya data non-sensitif ke cloud dan pertahankan sistem kritis secara on-premise dengan security upgrade",
            "Batalkan rencana migrasi cloud sepenuhnya karena kendali atas data sensitif tidak bisa dialihkan ke pihak ketiga tanpa risk yang tidak bisa diterima",
            "Minta tender terbuka untuk multiple cloud providers dan pilih berdasarkan hasil evaluasi keamanan dan kepatuhan mereka terhadap standar yang berlaku"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pendekatan balanced: memanfaatkan efisiensi cloud untuk data non-sensitif sambil mempertahankan kontrol penuh atas sistem kritis. Pendekatan ini pragmatic tapi tetap prudent terhadap risiko keamanan data sensitif. Bukan A yang terlalu trust-based pada vendor, bukan B yang menunda tanpa interim plan, bukan D yang menolak terlalu kaku, bukan E yang meliberalisasi decision terlalu banyak.",
        "difficulty": "hard"
    },
]

profesionalisme = [
    {
        "id": "tkp2_031", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda auditor internal yang sedang melakukan audit terhadap kegiatan pengadaan barang dan jasa. Dalam proses audit, Anda menemukan irregularities signifikan: beberapa proyek memiliki dokumentasi tidak lengkap tapi dana sudah dicairkan, dan ada indikasi bahwa salah satu pejabat tinggi yang Anda hormati mungkin terlibat. Pejabat tersebut merupakan salah satu mentor Anda dalam karier. Dokumentasi tidak lengkap tidak bisa langsung membuktikan KKN, tapi ada pola yang mengkhawatirkan.",
        "options": [
            "Selesaikan audit dengan tidak menyebutkan temuan irregularities karena tidak ada bukti kuat dan Anda tidak ingin menuduh seseorang yang Anda hormati tanpa dasar yang jelas",
            "Sampaikan temuan irregularities kepada atasan auditor dengan language yang faktual, tanpa spekulasi tentang keterlibatan pejabat tinggi, namun sarankan investigation lebih lanjut oleh pihak berwenang karena pola dokumentasi tidak bisa diabaikan begitu saja",
            "Langsung hubungi pejabat tersebut dan sampaikan temuan secara pribadi, minta klarifikasi sebelum audit report dibuat resmi",
            "Eskalasi temuan ke APH karena indikasi irregularities yang melibatkan pejabat tinggi harus segera ditindaklanjuti oleh lembaga berwenang",
            "Buat audit report yang soft-pedal temuan irregularities karena tidak ingin menjadi penyebab masalah bagi organisasi dan pejabat yang Anda hormati"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan integritas auditor yang matur: tidak menyembunyikan temuan, tidak langsung menuduh, tidak mem-bully tapi juga tidak membiarkan pola mengkhawatirkan begitu saja. Penyampaian faktual dengan rekomendasi eskalasi melindungi both auditor dan organisasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_032", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda pejabat yang ditugaskan mengevaluasi kinerja proyek yang didanai dana conjugate cukup besar. Proyek berjalan sesuai timeline, namun Anda menemukan proyek secara kualitas questionable: material tidak sesuai spesifikasi tapi still within acceptable range, workmanship tidak mengikuti best practices tapi tidak ada failure immediate visible, dan progress report melebih-lebihkan pencapaian. Semua ini technically legal tapi kualitas jangka panjang dipertanyakan.",
        "options": [
            "Setujui proyek karena secara legal tidak ada pelanggaran dan semua metric formal terpenuhi",
            "Tuliskan evaluation yang jujur bahwa proyek secara teknis comply tapi kualitas tidak optimal, dan sarankan perbaikan untuk tahap selanjutnya, tanpa menahan pembayaran karena legal obligation harus dipenuhi",
            "Tolak pembayaran karena kualitas tidak sesuai best practice tidak layak mendapat approval dari pejabat yang memiliki tanggung jawab atas penggunaan dana conjugate",
            "Minta inspection oleh pihak ketiga independen untuk validate kualitas proyek sebelum memberikan approval",
            "Serahkan keputusan kepada atasan karena keputusan kompleks dan menyangkut banyak pihak"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan integritas yang pragmatis: tidak menyembunyikan kualitas suboptimal, tidak menahan pembayaran yang secara legal sudah seharusnya dibayarkan, tapi tetap menyampaikan truth dalam bentuk rekomendasi perbaikan. Menghormati both legal obligation dan tanggung jawab atas kualitas spending publik.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_033", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda diminta menjadi narasumber dalam rapat yang membahas rencana pengurangan personil. Secara personal Anda tidak setuju karena akan mengganggu pelayanan publik. Namun secara data, beban kerja unit kerja Anda tidak proporsional dengan jumlah staf dan ada unit lain yang justru overstaffed. Beberapa staf di unit Anda sudah bekerja 20+ tahun dengan loyalitas tinggi. Pengurangan staff akan berdampak langsung pada kehidupan mereka dan keluarga.",
        "options": [
            "Dukung pengurangan personil karena data menunjukkan there is overstaffing di beberapa unit dan efisiensi adalah kepentingan organisasi yang lebih besar",
            "Melawan pengurangan personil dengan alasan bahwa pengurangan akan menurunkan kualitas pelayanan publik dan mengorbankan staf senior yang sudah mengabdi lama",
            "Sampaikan analisis data secara objektif, akui disparitas staffing, namun sarankan alternative approach: redistribusi personil dari unit overstaffed ke unit membutuhkan, dengan program reskilling untuk memastikan staf bisa berkontribusi di unit baru",
            "Minta waktu untuk melakukan workload analysis lebih detail sebelum memberikan recommendation",
            "Serahkan keputusan kepada HRD karena mereka paling memahami organizational needs"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan profesionalisme yang kompleks: tidak memilih antara data-driven efficiency dan human-centered approach tapi mencari solusi yang keduanya dipenuhi. Redistribusi dan reskilling adalah win-win yang mempertahankan tenaga kerja sambil meningkatkan efisiensi organisasi.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_034", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda pejabat eselon II yang sedang menghadapi periode transisi kepemimpinan: atasan akan pensiun dalam 3 bulan dan pejabat baru akan mengambil alih. Pejabat baru memiliki gaya kepemimpinan berbeda dan mungkin prioritas berbeda. Beberapa staff mulai melakukan manuver untuk memposisikan diri bagi pemimpin baru, termasuk beberapa staff menunjukkan tidak loyal kepada Anda dan mulai bypass komunikasi hierarki. Kondisi ini mengganggu stabilitas tim secara signifikan.",
        "options": [
            "Biarkan saja karena transisi kepemimpinan adalah proses alami dan Anda tidak bisa mengontrol bagaimana staff merespons situasi",
            "Adakan meeting tim dan sampaikan bahwa selama masa transisi semua staff harus tetap berkomunikasi melalui hierarki yang berlaku dan tidak ada yang boleh bypass Anda dalam reporting",
            "Proaktif sampaikan kepada staff bahwa Anda mendukung mereka dan akan memberikan rekomendasi yang baik kepada pemimpin baru",
            "Bicara secara personal dengan staff yang paling visible dalam melakukan manuver, pahami motivasi mereka dan sampaikan dampak dari perilaku mereka terhadap stabilitas tim dan professional reputation mereka",
            "Lapor kepada siapapun yang datang sebagai pejabat baru bahwa Anda memiliki tim solid dan siap bekerja"
        ],
        "answer": "D",
        "explanation": "Opsi D menunjukkan kepemimpinan yang mature dan empatik: tidak menggunakan authority secara top-down, tidak pasif, tidak transaksional. Pendekatan personal conversation mengakui bahwa staff mungkin memiliki concerns legitimate tentang masa depan mereka tapi mengkomunikasikan impact dari perilaku tidak profesional. Membangun trust dan respect.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_035", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda ditugaskan mengevaluasi kinerja pejabat yang kemungkinan akan dipromosikan ke posisi lebih tinggi. Kinerja pejabat tersebut pada metrics formal sangat bagus, namun ada issue mengkhawatirkan: hubungan terlalu dekat dengan vendor yang berpotensi konflik kepentingan, sering membuat keputusan penting tanpa konsultasi timnya, dan mengambil credit untuk pekerjaan tim yang bukan dia yang mengerjakan. Semua ini tidak melanggar hukum secara explicit tapi mengindikasikan character issues yang bisa berbahaya di posisi lebih tinggi.",
        "options": [
            "Berikan evaluasi positif karena semua formal metrics terpenuhi dan tidak ada bukti pelanggaran yang bisa digunakan untuk menahan promosi tersebut",
            "Berikan evaluasi yang balanced: akui performance metrics positif tapi tambahkan catatan tentang character concerns, sampaikan bahwa dalam konteks promosi ke posisi lebih tinggi, character dan integrity sama pentingnya dengan performance, dan sarankan mentoring sebelum promosi",
            "Jangan berikan rekomendasi apapun karena tidak ingin mempengaruhi karier seseorang berdasarkan impressions yang mungkin salah",
            "Buat evaluasi negatif karena character issues lebih penting daripada performance metrics dalam menentukan siapa yang layak promosi ke posisi leadership",
            "Bicara langsung dengan pejabat tersebut tentang concerns dan minta klarifikasi sebelum menuliskan evaluasi apapun"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan integritas evaluator yang responsible: tidak menyembunyikan concerns, tidak memblokir promosi dengan alasan soft, tapi memberikan picture lengkap yang memungkinkan decision-makers membuat informed decision. Menyampaikan bahwa character penting dalam leadership adalah truth yang penting dikomunikasikan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_036", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda pejabat yang diminta memberikan konsultasi kepada organisasi pemerintah daerah yang mengalami masalah kinerja parah: layanan publik buruk, waktu kerja tidak dipatuhi, banyak keluhan warga. Organisasi tidak memiliki masalah budget tapi mengelola dana besar secara tidak optimal. Masalahnya adalah budaya organisasi yang buruk memerlukan perubahan mendasar. Untuk membuat perubahan, Anda perlu cooperation dari pejabat lokal yang mungkin merasa terancam oleh kedatangan Anda sebagai konsultan eksternal.",
        "options": [
            "Segera identifikasi masalah utama dan sampaikan rekomendasi perubahan secara komprehensif dalam laporan tertulis karena itu tugas Anda",
            "Mulai dengan pendekatan kolaboratif: listening sessions dengan berbagai stakeholder, identifikasi pain points dari dalam organisasi, bangun trust dan ownership terhadap perubahan dari dalam, baru ajukan interventions berbasis temuan lapangan",
            "Batasi konsultasi pada technical aspects karena budaya organisasi bukan domain yang bisa diubah oleh konsultan eksternal",
            "Minta tambahan fee karena organisasi ini memerlukan intervensi berat yang akan memakan waktu dan usaha jauh lebih besar dari konsultasi standard",
            "Tolak konsultasi karena organisasi ini memerlukan perubahan yang bukan bisa dicapai melalui konsultasi biasa"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan consulting approach yang sophisticated: tidak langsung membenturkan recommendations tanpa memahami konteks, tidak underestimate kekuasaan resistensi, tapi membangun foundation perubahan melalui trust-building dan collaborative ownership. Perubahan yang di-own oleh organisasi sendiri lebih sustainable.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_037", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda pejabat yang harus memutuskan apakah akan whistleblower tentang pelanggaran yang ditemukan di instansi Anda. Pelanggaran nyata dan serius, melibatkan beberapa pejabat senior termasuk seseorang yang merupakan mentor karier Anda. Jika whistleblower, Anda merusak hubungan dengan mentor dan kemungkinan menghadapi retaliation dari jaringan pejabat senior tersebut. Jika tidak whistleblower, Anda tidak menjalankan tanggung jawab integritas sebagai pejabat negara dan pelanggaran berlanjut.",
        "options": [
            "Whistleblower melalui channel resmi karena tanggung jawab integritas sebagai pejabat negara lebih penting dari hubungan personal atau fear of retaliation",
            "Tidak whistleblower karena tidak ingin merusak hubungan dengan mentor dan menghadapi retaliation dari pejabat senior",
            "Bicara langsung dengan mentor dan sampaikan bahwa Anda mengetahui pelanggaran dan akan melakukan whistleblowing, beri kesempatan mentor memperbaiki situasi sendiri sebelum eskalasi",
            "Whistleblower secara anonim untuk melindungi diri sendiri sambil tetap menjalankan tanggung jawab integritas",
            "Minta perlindungan hukum terlebih dahulu sebelum whistleblower karena retaliation akan terjadi dan Anda butuh perlindungan sebelum bertindak"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan integritas tertinggi: tidak menggunakan alasan-alasan yang plausible untuk menghindari tanggung jawab. Whistleblowing melalui channel resmi adalah mekanisme yang sudah ada untuk melindungi whistleblower sekaligus memastikan pelanggaran ditindaklanjuti. Mengorbankan mentor tidak enak tapi integritas tidak bisa dikompromikan.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_038", "category": "TKP", "subcategory": "Profesionalisme",
        "question": "Anda pejabat eselon I yang diminta mengevaluasi apakah instansi perlu melakukan organizational restructure. Data menunjukkan struktur saat ini tidak efisien: overlap responsibilities, duplikasi fungsi, dan communication bottleneck karena hierarki terlalu panjang. Namun restructure berarti beberapa posisi eselon II occupied by people yang sudah mengabdi lama akan dihapus atau diubah, termasuk sosok senior yang sangat respected. Mereka sudah memberikan kontribusi besar tapi posisi mereka sudah tidak efisien secara struktural.",
        "options": [
            "Rekomendasikan restructure sesuai data karena efisiensi organisasi lebih penting dari sentiment terhadap individu",
            "Tunda restructure karena mereorganisasi birokrasi dengan menghapus posisi pejabat senior yang sudah loyal adalah political minefield yang terlalu risky",
            "Rekomendasikan restructure namun dengan compassion: pastikan ada positions comparable atau early retirement package yang generous untuk pejabat senior terdampak, dengan timeline transisi manusiawi dan proses komunikasi transparan",
            "Lakukan restructure secara keseluruhan dan lihat saja apa yang terjadi karena organisasi perlu fresh start",
            "Tidak ambil keputusan karena ini keputusan level politik yang harus dibuat oleh elected officials atau political appointees"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan keseimbangan antara efisiensi organisasi dan penghormatan terhadap kontribusi pejabat senior. Compassionate restructuring dengan package yang layak menunjukkan bahwa organisasi menghargai mereka yang sudah mengabdi. Ini juga mengurangi resistance terhadap perubahan dan modeled integrity organisasi.",
        "difficulty": "hard"
    },
]

data.extend(tik)
data.extend(profesionalisme)
with open('assets/questions/tkp_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Total now: {len(data)}")

import re
bad = sum(1 for q in data for key in ['question','answer','explanation'] if key in q and re.search(r'[^\x00-\x7F]', q[key]))
bad += sum(1 for q in data for opt in q.get('options',[]) if re.search(r'[^\x00-\x7F]', opt))
print(f"Non-ASCII issues: {bad}")