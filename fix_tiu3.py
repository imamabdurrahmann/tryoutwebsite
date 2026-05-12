import json, re

with open('assets/questions/tiu_3.json', encoding='utf-8') as f:
    data = json.load(f)

# Fix Q8 (index 7) - questionText
q = data[7]
q['questionText'] = (
    "Perhatikan premis-premis berikut!\n"
    "1. Tidak semua mahasiswa membutuhkan kegiatan di luar jam kuliah karena sebagian lebih memilih belajar secara mandiri.\n"
    "2. Beberapa mahasiswa mengambil program multitasking yang memengaruhi kualitas pembelajaran.\n"
    "3. Program multitasking yang memengaruhi kualitas pembelajaran berpotensi menurunkan prestasi akademik.\n"
    "4. Mahasiswa yang mengambil program multitasking berpotensi menghadapi tekanan yang lebih besar dan tantangan yang lebih berat.\n"
    "5. Tekanan yang besar berpotensi menurunkan kesehatan mental dan produktivitas.\n"
    "6. Jika kesehatan mental terpengaruh, maka kualitas hidup berpotensi menurun.\n\n"
    "Simpulan yang tepat adalah..."
)
q['options'] = [
    "Semua mahasiswa berpotensi waktunya terbuang karena multitasking tidak diperlukan dalam menuntut ilmu",
    "Mahasiswa yang mengambil program multitasking berpeluang mengalami tekanan lebih besar sehingga berpotensi menurunkan kesehatan mental dan kualitas hidup, meskipun ada sebagian yang mampu menyeimbangkan",
    "Program multitasking tidak penting karena tidak menurunkan prestasi akademik secara signifikan",
    "Kualitas hidup berpotensi menurun hanya jika mahasiswa mengambil program multitasking secara berlebihan tanpa jeda",
    "Mahasiswa sebaiknya tidak mengikuti kegiatan ekstrakurikuler agar bisa fokus sepenuhnya pada akademik"
]
q['answer'] = "Mahasiswa yang mengambil program multitasking berpeluang mengalami tekanan lebih besar sehingga berpotensi menurunkan kesehatan mental dan kualitas hidup, meskipun ada sebagian yang mampu menyeimbangkan"
q['explanation'] = "Dari premis 4: multitasking berpotensi menimbulkan tekanan lebih besar. Dari premis 5: tekanan besar berpotensi menurunkan kesehatan mental dan produktivitas. Dari premis 6: kesehatan mental terpengaruh berpotensi menurunkan kualitas hidup. Dari premis 1: tidak semua mahasiswa memiliki preferensi yang sama. Jadi ada yang mampu mengelola keseimbangan, namun ada juga yang terpengaruh tekanan dan mengalami penurunan kualitas hidup."

# Fix Q9 (index 8) - questionText
q = data[8]
q['questionText'] = (
    "Perhatikan premis-premis berikut!\n"
    "1. Semua jenis buah yang berwarna merah mengandung antioksidan tinggi yang baik untuk kesehatan.\n"
    "2. Mangga berwarna hijau dan memiliki rasa manis yang khas namun tidak mengandung antioksidan tinggi sesuai standar laboratorium.\n"
    "3. Makanan yang kaya antioksidan berpotensi meningkatkan kesehatan dan meningkatkan sistem imun tubuh.\n"
    "4. Jika sistem imun tubuh meningkat, maka tubuh lebih mampu menangkal berbagai penyakit infeksi.\n"
    "5. Namun, tidak semua orang bersedia mengonsumsi buah karena preferensi rasa atau ketersediaan.\n\n"
    "Berdasarkan premis-premis tersebut, Simpulan yang paling tepat adalah..."
)
q['options'] = [
    "Mangga bukan buah yang baik untuk kesehatan karena berwarna hijau",
    "Buah berwarna merah yang kaya antioksidan berpotensi meningkatkan kesehatan namun tidak semua orang bersedia mengonsumsi buah sehingga manfaat tersebut tidak dirasakan semua orang",
    "Semua buah berpotensi meningkatkan kesehatan karena semua buah mengandung antioksidan dalam kadar berbeda",
    "Mengonsumsi buah saja tidak cukup karena tubuh还需要 sumber nutrisi lain yang beragam",
    "Mangga tidaklayak dikonsumsi karena kurang memiliki zat gizi penting yang dibutuhkan tubuh"
]
q['options'][3] = "Mengonsumsi buah saja tidak cukup karena tubuh juga membutuhkan sumber nutrisi lain yang beragam"
q['options'][4] = "Mangga tidaklayak dikonsumsi karena kurang memiliki zat gizi penting yang dibutuhkan tubuh"
q['options'][4] = "Mangga tidaklayak dikonsumsi karena kurang memiliki zat gizi penting yang dibutuhkan tubuh"
q['answer'] = "Buah berwarna merah yang kaya antioksidan berpotensi meningkatkan kesehatan namun tidak semua orang bersedia mengonsumsi buah sehingga manfaat tersebut tidak dirasakan semua orang"
q['explanation'] = "Dari premis 1 dan 3: buah berwarna merah kaya antioksidan berpotensi meningkatkan kesehatan. Dari premis 5: tidak semua orang bersedia mengonsumsi buah karena preferensi rasa atau ketersediaan. Dari premis 2: mangga hijau tidak kaya antioksidan tapi tetap manis. Jadi meskipun buah merah kaya antioksidan, tidak semua orang bersedia mengonsumsinya. Kesimpulan: buah merah berpotensi meningkatkan kesehatan namun penerima manfaatnya terbatas karena keterbatasan konsumsi."

# Fix Q10 (index 9) - questionText
q = data[9]
q['questionText'] = (
    "Perhatikan premis-premis berikut!\n"
    "1. Setiap mahasiswa yang rajin belajar berpeluang memperoleh nilai yang lebih baik.\n"
    "2. Sebagian mahasiswa tidak mengikuti kelas secara teratur meskipun jadwal sudah ditetapkan.\n"
    "3. Kelas yang tidak teratur diikuti berpotensi memengaruhi pemahaman materi kuliah.\n"
    "4. Pemahaman materi kuliah yang baik berpotensi menghasilkan prestasi akademik yang optimal.\n"
    "5. Prestasi akademik yang optimal berpotensi membuka peluang kerja yang lebih baik.\n"
    "6. Namun, belajar tekun tidak menjamin keberhasilan karena juga bergantung pada faktor-faktor lain seperti koneksi, kondisi kesehatan, dan kondisi pasar kerja.\n\n"
    "Berdasarkan premis-premis tersebut, Simpulan yang paling mungkin adalah..."
)
q['options'] = [
    "Semua mahasiswa yang rajin belajar berpeluang memperoleh nilai lebih baik dan berpotensi sukses dalam karier",
    "Mahasiswa yang rajin belajar berpeluang memperoleh nilai lebih baik namun bukan jaminan kesuksesan karena ada faktor lain yang juga berpengaruh seperti koneksi, kesehatan, dan kondisi pasar kerja",
    "Mahasiswa yang tidak rajin belajar berpotensi gagal dan tidak akan memperoleh pekerjaan yang layak",
    "Hanya nilai akademik yang menentukan kesuksesan seseorang di dunia kerja",
    "Belajar tidak penting karena ada banyak orang yang berhasil tanpa pendidikan formal"
]
q['answer'] = "Mahasiswa yang rajin belajar berpeluang memperoleh nilai lebih baik namun bukan jaminan kesuksesan karena ada faktor lain yang juga berpengaruh seperti koneksi, kesehatan, dan kondisi pasar kerja"
q['explanation'] = "Dari premis 1: rajin belajar memberikan peluang memperoleh nilai lebih baik. Dari premis 6: namun belajar tekun tidak menjamin keberhasilan karena juga bergantung pada faktor-faktor lain seperti koneksi, kesehatan, dan kondisi pasar kerja. Jadi rajin belajar memberikan peluang nilai lebih baik tapi bukan jaminan kesuksesan karena ada banyak faktor lain yang juga berpengaruh."

# Upgrade difficulty: Q11, Q14, Q16, Q18, Q19, Q25
data[10]['difficulty'] = 'hard'   # Q11
data[13]['difficulty'] = 'hard'   # Q14
data[15]['difficulty'] = 'hard'   # Q16
data[17]['difficulty'] = 'hard'   # Q18
data[18]['difficulty'] = 'hard'   # Q19
data[24]['difficulty'] = 'hard'   # Q25

with open('assets/questions/tiu_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Written successfully")
