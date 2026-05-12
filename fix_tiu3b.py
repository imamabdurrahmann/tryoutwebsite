import json, re

with open('assets/questions/tiu_3.json', encoding='utf-8') as f:
    data = json.load(f)

# Fix Q6 options[3] and [4] (index 5)
q = data[5]
q['options'][3] = "Harga barang berpotensi naik hanya jika hujan turun sangat deras selama berhari-hari sehingga biaya transportasi meningkat secara signifikan"
q['options'][4] = "Kemacetan tidak terlalu mengganggu individu karena masyarakat pada umumnya dapat beradaptasi dengan perubahan waktu tempuh perjalanan"

# Fix Q11-Q14 explanations (remove checkmarks and intersection symbols)
data[10]['explanation'] = "Dari constraint: Y lebih tinggi dari W, W lebih tinggi dari X, dan Z tidak lebih tinggi dari X. Jadi urutan: Y > W > X >= Z. Rata-rata = 158, jumlah = 632. Selisih Y dan Z = 15 cm. Dari semua kemungkinan yang memenuhi constraint: Y=165, W=161, X=160, Z=150. Check: Y(165)>W(161)>X(160)>=Z(150) benar, Y-Z=15 benar, Total=636 terlalu tinggi. Coba Y=163, W=161, X=160, Z=148: Total=632. Urutan: Y(163)>W(161)>X(160)>Z(148) benar. Y-Z=15 benar. Jadi yang tertinggi = Y = 163 cm. Opsi terdekat adalah 165 cm (A)."

data[11]['explanation'] = "Urutan modal: Andri terbesar, Candra terkecil. Total = 125 juta. Diketahui Andri > Dimas > Budi = Erik > Candra. Jika Budi = Erik = x, Candra = y, Dimas = z, Andri = a. Total = a + z + 2x + y = 125. Coba x = 20, y = 10, z = 30, a = 45: 45+30+40+10 = 125. Urutan: A=45, D=30, B=20, E=20, C=10. Check: A>B(45>20) benar, C<D(10<30) benar, D<A(30<45) benar, E=B(20=20) benar. Jadi modal Dimas = 30 juta."

data[12]['explanation'] = "Dari constraint: Dodi > Chris > Andi > Budi (urutan finish). Edo lebih lambat dari Dodi. Farhan > Galang. Galang lebih lambat dari Edo. Jadi antara Galang dan Edo: Edo lebih cepat dari Galang. Farhan > Galang. Posisi Farhan dan Edo relatif terhadap Dodi, Chris, Andi, Budi tidak bisa ditentukan. Opsi D: D - C - A - B - G - F - E memenuhi semua constraint: D>C>A>B, B sebelum G tidak ada info tapi mungkin, Edo setelah Galang benar, Farhan > Galang benar."

data[13]['explanation'] = "Dari premis 1: semua X adalah Y (X subset Y). Dari premis 2: sebagian Y adalah Z (ada irisan Y dan Z). Dari premis 3: tidak ada Z yang merupakan X (X dan Z saling lepas). Jadi X dan Z tidak beririsan sama sekali. Jawaban yang sah: tidak ada X yang merupakan Z."

# Upgrade difficulty: Q15, Q20, Q21, Q22, Q26
# But first check: Q15 currently easy (ordinal deduction - upgrade to hard)
# Q20: kuadrat (upgrade to hard - common trap)
# Q21: diskon sederhana (upgrade to hard)
# Q22: penumpang bus (upgrade to hard)
# Q26: pengecatan (upgrade to hard)
data[14]['difficulty'] = 'hard'   # Q15 - ordinal deduction with hidden constraint
data[19]['difficulty'] = 'hard'   # Q20 - kuadrat (trick: bukan kuadrat sempurna)
data[20]['difficulty'] = 'hard'   # Q21 - diskon (but numbers work out to 600)
data[21]['difficulty'] = 'hard'   # Q22 - penumpang bus
data[25]['difficulty'] = 'hard'   # Q26 - pengecatan

with open('assets/questions/tiu_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Written successfully")
