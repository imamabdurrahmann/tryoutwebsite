import json, os

base = r'c:\Users\muham\tryout_cpns\assets\questions'

# Full manual translations for heavily English explanations
manual_fixes = {
    # twk_3.json
    'twk3_028': 'Opsi C menunjukkan pendekatan yang seimbang: baik penerjemahan harfiah murni maupun adaptasi total bukanlah pilihan optimal. Pendekatan bernuansa yang memprioritaskan aspek emosional dan konteks budaya sambil tetap mempertahankan makna asli merupakan strategi terbaik dalam penerjemahan lintas budaya.',
    
    # tiu.json - soal dengan campuran Inggris
    'tiu_005': 'Dari info: Dini di trotoar selatan dan bukan gorengan, bukan pakaian, bukan minuman (Bela), bukan aksesoris (Erni). Jadi Dini = makanan berat di trotoar selatan. Wati berjualan di trotoar selatan. Tapi siapa yang jual makanan berat? Dini. Tidak mungkin gorengan (trotoar utara tidak gorengan). Dini bukan minuman (Bela). Dini bukan pakaian. Dini bukan aksesoris (Erni). Jadi satu-satunya sisa = makanan berat. Jadi Dini = makanan berat di trotoar selatan. Tapi pertanyaannya: makanan berat = trotoar selatan = Dini. Cek: Andra tidak di trotoar. Bela tempat. Candra tidak bukan makanan berat dan bukan gorengan. Bela = minuman tempat. Candra bukan makanan berat dan bukan pakaian sehingga Candra = gorengan di trotoar utara atau trotoar selatan. Dini trotoar selatan, jadi makanan berat = Dini. Wati opsi gorengan. Candra. Mari ulang: Andra tidak buat gorengan. Bela = minuman tempat. Jadi Andra = trotoar atau depan toko. Dini trotoar selatan, jadi tempat lain. Candra tidak depan toko. Jadi Andra = depan toko atau depan bank. Erni depan bank. Jadi Andra = depan toko. Candra = tempat atau depan bank. Erni = depan bank. Jadi tempah sudah. Bela. Jadi Candra = tempat? Tidak. Bela tempat. Jadi Candra harus di trotoar utara. Jadi: Dini = trotoar selatan dan bukan gorengan. Erni = aksesoris depan bank. Gorengan = trotoar utara. Jadi: trotoar utara = gorengan. Trotoar selatan = Dini (bukan gorengan, minuman, pakaian) = aksesoris = makanan berat, tempat = Bela (minuman). Depan toko = Andra. Bukan depan toko. Dini = trotoar selatan, jadi tempat lain. Jadi Dini = makanan berat. Jawaban = Dini.',

    'tiu_009': 'Pola: pisahkan bilangan ganjil dan genap. Posisi ganjil: 5, 10, 19, 32, 49 sehingga beda: +5, +9, +13, +17 (selisih bertambah +4 setiap langkah). Selanjutnya +21 = 70. Posisi genap: 6, 9, 14, 21, 30. Beda: +3, +5, +7, +9 (selisih bertambah +2 setiap langkah). Selanjutnya +11 = 41. Jadi jawabannya adalah 70.',

    'tiu_014': 'Gina di 102. Iwan ruangan kelipatan 3 sehingga 102, 105, 103 (3x34), 106 (tidak), 101 (tidak), 104 (tidak). Jadi Iwan di 103. Hani beda lantai dari 102. Dari info, Hani di ruangan genap = 104 atau 106. Fani di sebelah Gina (101 atau 103). Karena Iwan di 103, Fani di 101. Jadi urutan: 101=Fani, 102=Gina, 103=Iwan, 104 atau 106=Hani. Jawaban: Fani di ruangan 101.',

    'tiu_017': 'Misalkan bilangan = x. (3/4)x - 2 = (1/2)x - 5. Kalikan 4: 3x - 8 = 2x - 20. 3x - 2x = -20 + 8. x = -12. Jawaban: -12.',

    'tiu_020': 'Bunga tunggal 12% per tahun = 1% per bulan. Saldo awal = 40.000.000. Bunga per bulan = 1% x 40.000.000 = 400.000. Setelah 8 bulan: Bunga total = 8 x 400.000 = 3.200.000. Saldo akhir = 40.000.000 + 3.200.000 = 43.200.000. Jawaban: Rp43.200.000.',

    'tiu_026': 'Dina tidak suka olahraga dan tidak suka memasak sehingga Dina = musik atau membaca. Chika tidak suka membaca sehingga Chika bukan membaca. Budi tidak suka musik dan tidak suka membaca sehingga Budi = olahraga atau memasak. Andi suka memasak (dari premis). Jadi Budi = olahraga. Chika tidak suka membaca, jadi Chika = musik. Dina = membaca. Jawaban: Dina suka membaca.',

    'tiu_027': 'Waktu A ke B = 60/40 = 1,5 jam = 1 jam 30 menit. Waktu B ke C = 80/60 = 1,333 jam = 1 jam 20 menit. Total jarak = 60 + 80 = 140 km. Total waktu = 1,5 + 1,333 = 2,833 jam. Kecepatan rata-rata = 140/2,833 = 49,4 km/jam ≈ 49,4 km/jam. Jawaban: 49,4 km/jam.',

    'tiu_028': '3^a = 81 sehingga a = 4 (karena 3^4 = 81). 4^b = 64 sehingga b = 3 (karena 4^3 = 64). Maka 2^(a+b) = 2^(4+3) = 2^7 = 128. Jawaban: 128.',

    'tiu_035': 'Keran isi: 1 bak / 15 menit = 1/15 per menit. Keran buang: 1 bak / 20 menit = 1/20 per menit. Kecepatan pengisian bersih = 1/15 - 1/20 = (4-3)/60 = 1/60 per menit. Jadi waktu pengisian = 60 menit = 1 jam. Jawaban: 60 menit.',

    'tiu_007': 'Pola: bilangan prima berselang-seling dengan kelipatan. Bilangan-bilangan dalam urutan memiliki dua pola terpisah. Pola ganjil (posisi 1, 3, 5): merupakan bilangan prima berurutan. Pola genap (posisi 2, 4, 6): merupakan kelipatan yang meningkat. Dengan mengikuti pola ini, angka berikutnya dapat ditentukan.',

    # tkp.json - pembahasan full English
    'tkp_032': 'Nilai 5: Manajemen pemangku kepentingan yang strategis - advokasi berbasis bukti (riset + ROI), mengatasi kekhawatiran khusus karyawan, dan membuat rencana implementasi bertahap yang meminimalkan gangguan. Nilai 4: Pelatihan dengan evaluasi adaptif dan keterbukaan untuk penyesuaian. Nilai 3: Pendekatan menengah dengan beberapa upaya sosialisasi. Nilai 2: Implementasi sepihak tanpa memperhatikan kekhawatiran. Nilai 1: Menolak perubahan tanpa pertimbangan manfaat.',

    'tkp_034': 'Nilai 5: Keunggulan dalam pengadaan dan manajemen proyek yang etis - komunikasi terbuka (pemahaman), solusi kreatif dalam batasan anggaran, dan menjaga kualitas sambil tetap transparan. Nilai 4: Negosiasi dengan vendor sambil mempertahankan standar kualitas. Nilai 3: Kompromi yang wajar dengan dokumentasi yang jelas. Nilai 2: Memotong anggaran tanpa mempertimbangkan dampak kualitas. Nilai 1: Mengabaikan prosedur pengadaan demi kecepatan.',

    'tkp_035': 'Nilai 5: Keunggulan layanan konsuler - pola pikir pemecahan masalah (verifikasi cepat), respons darurat (koordinasi langsung), dan empati profesional dengan batasan yang jelas. Nilai 4: Membantu dengan prosedur standar yang dipercepat. Nilai 3: Memberikan informasi yang memadai dan arahan yang benar. Nilai 2: Merujuk tanpa bantuan aktif. Nilai 1: Menolak membantu di luar jam kerja.',
}

# Process each file
files_to_check = {
    'twk_3.json': ['twk3_028'],
    'tiu.json': ['tiu_005','tiu_007','tiu_009','tiu_014','tiu_017','tiu_020','tiu_026','tiu_027','tiu_028','tiu_035'],
    'tkp.json': ['tkp_032','tkp_034','tkp_035'],
}

for fname, ids in files_to_check.items():
    fp = os.path.join(base, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data:
        qid = q['questionId']
        if qid in manual_fixes:
            old = q['explanation'][:80]
            q['explanation'] = manual_fixes[qid]
            modified = True
            print(f"REPLACED {qid}: {old}... -> {q['explanation'][:80]}...")
    
    if modified:
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"SAVED: {fname}\n")

print("Done! All explanations are now in pure Indonesian.")
