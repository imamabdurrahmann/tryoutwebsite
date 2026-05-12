import json

with open('assets/questions/tkp_2.json', encoding='utf-8') as f:
    data = json.load(f)

integritas = [
    {
        "id": "tkp2_039", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat yang akan pensiun dalam 6 bulan. Sepanjang karier Anda dikenal sebagai pejabat bersih dan tidak pernah terlibat KKN. Namun dalam bulan-bulan terakhir ini, Anda ditawari pekerjaan consulting oleh perusahaan yang merupakan mitra instansi Anda. Fee sangat besar dan Anda tahu tawaran ini karena perusahaan menghargai hubungan baik Anda dengan instansi dan berharap Anda bisa menggunakan koneksitas setelah pensiun untuk melancarkan proses procurement mereka. Anda tidak diharuskan menggunakan koneksitas secara eksplisit tapi implikasinya jelas.",
        "options": [
            "Terima pekerjaan tersebut karena Anda sudah tidak menjabat lagi dan tidak ada conflict of interest karena tidak menggunakan posisi official untuk kepentingan perusahaan",
            "Terima pekerjaan tersebut tapi dengan tegas sampaikan kepada perusahaan bahwa Anda tidak akan menggunakan koneksitas Anda di instansi untuk kepentingan mereka",
            "Tolak pekerjaan tersebut karena meskipun tidak secara eksplisit menggunakan positional authority, tawaran ini adalah bentuk gratitude lobbying yang exploitative terhadap hubungan institusional, dan sebagai pejabat yang bersih Anda tidak membuka preseden yang merusak integritas sistem",
            "Minta waktu untuk berpikir karena perlu mempertimbangkan secara matang apakah ini kesempatan professional yang legitimate atau cara mendapatkan akses tidak legitimate",
            "Diskusikan dengan atasan tentang tawaran ini karena sebagai pejabat yang akan pensiun Anda butuh guidance tentang batas antara kesempatan professional dan conflict of interest"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan integritas yang konsisten dan vision jangka panjang: tidak melihat pensiun sebagai free pass untuk behavior yang sebelumnya tidak dilakukan, memahami bahwa gratitude lobbying adalah bentuk corruption yang subtle tapi nyata, dan berkomitmen pada prinsip yang sama sebelum dan sesudah pensiun.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_040", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat dengan integritas tinggi di organisasi. Namun Anda memiliki keluarga dengan kebutuhan finansial tidak kecil: anak kuliah, orang tua sakit, rumah masih berutang. Anda ditawarkan pekerjaan sampingan sebagai konsultan dengan fee sangat menggiurkan oleh perusahaan yang berkali-kali memenangkan tender di instansi Anda. Anda tahu secara hukum boleh memiliki pekerjaan sampingan selama tidak mengganggu tugas pokok. Namun Anda juga tahu hubungan Anda dengan perusahaan tidak bisa dilepaskan dari positional authority Anda sebagai pejabat.",
        "options": [
            "Terima pekerjaan tersebut karena secara hukum diizinkan dan kebutuhan finansial keluarga adalah realitas yang tidak bisa diabaikan",
            "Terima pekerjaan tersebut dengan syarat perusahaan adalah perusahaan yang kompeten dan Anda hanya memberikan konsultasi professional based on expertise bukan berdasarkan positional advantage",
            "Tolak pekerjaan tersebut karena meskipun secara hukum diperbolehkan, hubungan Anda dengan perusahaan yang secara rutin memenangkan tender menciptakan conflict of interest yang tidak bisa diabaikan, dan integritas yang dibangun bertahun-tahun tidak boleh dikompromikan oleh kebutuhan finansial yang sementara",
            "Minta izin tertulis kepada atasan sebelum menerima pekerjaan tersebut agar ada transparansi dan formal clearance yang melindungi Anda",
            "Temukan perusahaan lain yang tidak ada hubungannya dengan instansi untuk pekerjaan sampingan agar tidak ada conflict of interest"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan integritas yang tidak situational: tidak membuat exception untuk convenience pribadi, memahami bahwa conflict of interest tidak hanya tentang legalitas tapi juga tentang persepsi dan precedent. Kebutuhan finansial keluarga tidak membenarkan compromise yang merusak credibility yang sudah dibangun bertahun-tahun.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_041", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat yang mengetahui bahwa salah satu rekan kerja memiliki masalah serius dengan alkoholisme yang mulai mempengaruhi kinerjanya. Rekan tersebut dulu pernah membantu Anda saat sedang dalam situasi sulit dan Anda merasa memiliki utang moral. Jika tidak melaporkan, kinerja tim bisa terganggu dan keputusan yang dibuat di bawah pengaruh alkohol bisa berbahaya. Namun reporting akan berarti akhir dari karier rekan Anda. Rekan tersebut memiliki keluarga dan konsekuensi dari reporting akan sangat berat bagi keluarganya juga.",
        "options": [
            "Tidak melaporkan karena tidak ingin menjadi penyebab kehancuran karier dan keluarga rekan kerja, dan masalah mungkin resolve sendiri seiring waktu",
            "Laporkan masalah tersebut kepada atasan dengan informasi akurat dan komprehensif karena keputusan tentang alkoholisme di tempat kerja harus ditindaklanjuti dan Anda tidak bisa menutup mata terhadap risiko terhadap tim dan keputusan organisasi",
            "Bicara langsung dengan rekan kerja terlebih dahulu: sampaikan bahwa Anda mengetahui masalahnya, berikan dia waktu dan kesempatan untuk memperbaiki sendiri, dan sampaikan bahwa jika dalam waktu tertentu tidak ada perbaikan, Anda akan perlu mengambil langkah lebih lanjut karena tidak bisa mengabaikan risiko terhadap tim",
            "Sarankan rekan kerja untuk mengambil cuti dan mencari bantuan professional tanpa melibatkan organisasi karena itu privacy matter yang harus diselesaikan antara dia dan keluarganya",
            "Lapor ke HRD agar mereka menangani masalah ini secara confidential tanpa exposed identitas Anda"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan keseimbangan antara loyalty terhadap teman dan tanggung jawab terhadap tim dan organisasi: tidak langsung reporting yang langsung destroy karier seseorang tanpa memberikan kesempatan, tapi juga tidak diam yang mengabaikan risiko nyata. Pendekatan ini menghormati friendship sambil holding to professional responsibility.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_042", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat yang diminta memberikan presentasi tentang anti-korupsi di acara yang disponai oleh perusahaan yang merupakan vendor utama di instansi Anda. Perusahaan memiliki reputasi tidak bagus: beberapa kali terlibat dalam kasus suap dan memiliki hubungan terlalu dekat dengan beberapa pejabat. Acara adalah program anti-korupsi yang disponai oleh mereka dan Anda diminta sebagai narasumber pemerintah. Hadir berarti memberikan legitimasi pada perusahaan track record korupsi. Tidak hadir berarti melewatkan kesempatan menyampaikan pesan anti-korupsi ke audience luas.",
        "options": [
            "Terima undangan karena pesan anti-korupsi harus disampaikan seluas mungkin dan siapa yang sponsori acara tidak mengubah substance pesan yang disampaikan",
            "Tolak undangan karena menerima sponsor dari perusahaan dengan track record suap untuk acara anti-korupsi adalah hipokrisi yang akan merusak kredibilitas pesan itu sendiri",
            "Terima undangan dengan syarat bahwa Anda akan sampaikan dalam presentasi bahwa Anda hadir sebagai pemerintah yang independen dan tidak memberikan endorsement terhadap sponsor, dan sampaikan kritik terhadap sponsor yang memiliki track record buruk dalam bicara anti-korupsi",
            "Negosiasi dengan perusahaan untuk mengganti sponsor acara dengan entity yang lebih bersih dan netral sebelum accept undangan",
            "Terima undangan dan gunakan kesempatan ini untuk publicly expose track record korupsi perusahaan sponsor sebagai bagian dari presentasi anti-korupsi Anda"
        ],
        "answer": "C",
        "explanation": "Opsi C menunjukkan pendekatan sophisticated: tidak memboikot kesempatan menyampaikan pesan anti-korupsi, tidak juga memberikan legitimasi diam-diam kepada sponsor bermasalah. Dengan menyatakan independence secara eksplisit dan memberikan kritik, pesan anti-korupsi menjadi lebih powerful karena datang dengan contoh nyata dari hypocrisy.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_043", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat eselon I yang selama 10 tahun memiliki track record sangat bersih dan dihormati banyak pihak. Anda mendapati bahwa salah satu staf dengan akses ke sistem informasi telah menyebarkan informasi internal kepada pihak yang tidak berhak. Tidak ada bukti kuat tentang siapa yang menyebarkan dan bagaimana informasi digunakan. Jika tidak mengambil tindakan, insiden bisa berulang dan berbahaya. Jika mengambil tindakan terlalu agresif tanpa bukti kuat, Anda bisa menuduh orang tidak bersalah dan merusak reputasi Anda sendiri.",
        "options": [
            "Lakukan audit forensik terhadap sistem untuk melacak siapa yang mengakses dan menyebarkan informasi, dengan pendekatan confidential dan tidak menuduh siapapun sebelum bukti ditemukan",
            "Segera nonaktifkan semua akses yang berpotensi spread informasi dan minta semua staf reset credentials, karena pendekatan zero trust adalah satu-satunya cara untuk memastikan keamanan",
            "Panggil semua staf yang memiliki akses dan minta mereka jujur karena Anda sudah mengetahui siapa pelakunya, meskipun sebenarnya tidak tahu",
            "Lapor ke BSSN dan pihak berwajib karena penyebarluasan informasi internal adalah tindak pidana yang harus ditangani pihak berwenang",
            "Biarkan saja karena tidak ada bukti kuat dan investigate tanpa bukti hanya akan menciptakan ketidakpercayaan di antara staf"
        ],
        "answer": "A",
        "explanation": "Opsi A menunjukkan profesionalisme dalam menghadapi security incident: tidak panik, tidak menuduh tanpa bukti, tapi juga tidak mengabaikan. Audit forensik berbasis data akan memberikan bukti yang dapat ditindaklanjuti dan melindungi both organisasi dan individu dari false accusation.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_044", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat yang mendapati bahwa kebijakan terbaru dari pemerintah pusat tentang reformasi birokrasi memiliki kelemahan fatal yang bisa menimbulkan unintended consequences besar bagi masyarakat. Anda sudah berpengalaman cukup lama untuk memahami bahwa kebijakan tersebut akan bermasalah jika diterapkan di lapangan. Namun kebijakan sudah disahkan dan semua pejabat diminta untuk implementasi. Jika sampaikan kritik, Anda bisa dianggap pembangkang yang tidak loyal terhadap kebijakan pemerintah. Jika diam, masyarakat akan merasakan dampak negatifnya.",
        "options": [
            "Diam karena Anda bagian dari birokrasi dan sudah menjadi kewajiban untuk implementasi kebijakan yang decided, masalah bisa diperbaiki dalam implementasi di level bawah",
            "Sampaikan kritik melalui channel resmi secara konstruktif dengan bukti empiris tentang potential problems dan solusi untuk perbaikan kebijakan sebelum implementasi dimulai, karena sampaikan melalui channel hierarchy adalah cara tepat dan konstruktif untuk influencing policy",
            "Publikasikan kritik di media dan media sosial agar masyarakat tahu ada masalah dalam kebijakan ini dan pressure publik bisa mendorong perbaikan",
            "Ikut implementasi sambil sabotase secara diam-diam agar kebijakan gagal dan Anda bisa membuktikan kebijakan tidak bisa berhasil",
            "Minta penugasan ke daerah lain saja sehingga tidak perlu bertanggung jawab atas implementasi kebijakan yang tidak Anda setuju"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan patriotism yang konstruktif: tidak diam saja, tidak sabotase, tidak publikasi membangkang tapi juga tidak blindly obedient. Penyampaian melalui channel resmi menunjukkan loyalty terhadap sistem hierarki sambil tetap menjalankan tanggung jawab sebagai pejabat yang competent dan concerned tentang wellbeing masyarakat.",
        "difficulty": "hard"
    },
    {
        "id": "tkp2_045", "category": "TKP", "subcategory": "Integritas Diri",
        "question": "Anda pejabat senior yang akan pensiun. Anda memiliki kesempatan untuk memberikan pesan dan nilai-nilai kepada generasi pejabat muda yang akan menggantikan. Anda tahu bahwa sepanjang karier ada momen-momen di mana Anda membuat keputusan yang tidak sepenuhnya puas: ada pilihan yang tidak Anda ambil karena terlalu afraid, ada kebenaran yang tidak Anda sampaikan karena terlalu political calculation, ada kesempatan yang Anda lewatkan untuk melakukan hal benar karena tidak nyaman. Sekarang Anda memiliki platform untuk meninggalkan pesan terakhir kepada pejabat muda.",
        "options": [
            "Sampaikan pesan bahwa dunia birokrasi adalah compromise dan pragmatism adalah kebutuhan, bahwa idealisme harus dikalibrasi dengan realitas politik dan sometimes you have to do what you have to do",
            "Sampaikan pesan bahwa integritas harus dijaga dengan konsisten terlepas dari circumstances, bahwa tidak ada justifikasi untuk compromise principle, bahwa meskipun dunia birokrasi tidak sempurna setiap pejabat memiliki pilihan untuk menentukan batas yang tidak boleh dilanggar",
            "Sampaikan pesan bahwa Anda tidak punya penyesalan karena semua keputusan yang Anda buat saat itu adalah yang terbaik dengan informasi yang tersedia pada saat itu",
            "Sampaikan pesan bahwa karier adalah marathon bukan sprint dan keseimbangan antara keluarga dan pekerjaan adalah sesuatu yang harus terus dilemma throughout career",
            "Sampaikan pesan bahwa pejabat muda harus membangun jaringan dan allies karena itu kunci sukses dalam birokrasi dan tanpa koneksii Anda tidak akan bisa berbuat banyak"
        ],
        "answer": "B",
        "explanation": "Opsi B menunjukkan legacy integritas yang jujur dan aspirasional: mengakui dunia tidak perfect tapi tidak membuat itu sebagai justifikasi untuk compromise, menyampaikan bahwa setiap individu memiliki agency untuk membuat pilihan ethical dan principle boundaries adalah personal responsibility yang tidak bisa didelegasikan. Bukan A yang terlalu realistis-skeptis, bukan C yang terlalu self-justifying, bukan D yang terlalu balanced tanpa principle jelas, bukan E yang terlalu Machiavellian.",
        "difficulty": "hard"
    },
]

data.extend(integritas)
with open('assets/questions/tkp_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Total: {len(data)}")

import re
bad = sum(1 for q in data for key in ['question','answer','explanation'] if key in q and re.search(r'[^\x00-\x7F]', q[key]))
bad += sum(1 for q in data for opt in q.get('options',[]) if re.search(r'[^\x00-\x7F]', opt))
hard = sum(1 for q in data if q['difficulty'] == 'hard')
med = sum(1 for q in data if q['difficulty'] == 'medium')
print(f"Hard: {hard}, Medium: {med}, Non-ASCII: {bad}")
print("DONE")