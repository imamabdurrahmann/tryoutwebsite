#!/usr/bin/env python3
"""Generate HOTS-level hard figural questions for tiu.json and tiu_2.json"""
import json, copy

def make_deret(id_, seq, answer_shapes, correct_idx, explanation, difficulty='hard'):
    return {
        'id': id_,
        'category': 'TIU',
        'subcategory': 'Figural',
        'question': 'Perhatikan pola deret figural berikut. Terdapat lebih dari satu pola yang beroperasi secara bersamaan. Tentukan gambar yang tepat untuk mengisi tanda ?.',
        'options': ['Pilihan A', 'Pilihan B', 'Pilihan C', 'Pilihan D', 'Pilihan E'],
        'answer': ['A','B','C','D','E'][correct_idx],
        'explanation': explanation,
        'difficulty': difficulty,
        'isFigural': True,
        'figuralData': json.dumps({
            'type': 'deret',
            'sequence': seq,
            'answerShapes': answer_shapes,
            'correctIndex': correct_idx,
        }, ensure_ascii=False),
    }

def make_matriks(id_, grid, answer_shapes, correct_idx, explanation, difficulty='hard'):
    return {
        'id': id_,
        'category': 'TIU',
        'subcategory': 'Figural',
        'question': 'Perhatikan matriks 3x3 berikut. Setiap sel diperoleh melalui operasi tertentu. Tentukan gambar yang tepat untuk mengisi tanda ?.',
        'options': ['Pilihan A', 'Pilihan B', 'Pilihan C', 'Pilihan D', 'Pilihan E'],
        'answer': ['A','B','C','D','E'][correct_idx],
        'explanation': explanation,
        'difficulty': difficulty,
        'isFigural': True,
        'figuralData': json.dumps({
            'type': 'matriks',
            'sequence': [],
            'gridData': grid,
            'answerShapes': answer_shapes,
            'correctIndex': correct_idx,
        }, ensure_ascii=False),
    }

# ─────────────────────────────────────────────────────────────────
# TIU.JSON — 10 HARD FIGURAL (7 deret HOTS + 3 matriks HOTS)
# ─────────────────────────────────────────────────────────────────

tiu_hard = [

    # === D1: Multi-transform deret — 3 simultaneous patterns ===
    # Pattern 1 (cycle 4): circle→square→triangle→diamond
    # Pattern 2 (rot): rot = index*90 mod 360
    # Pattern 3 (pos): even=0(atas), odd=1(bawah)
    # Answer at index 8: filled diamond, rot=0, position=0 → option C
    make_deret(
        id_='tiu_003',
        seq=['circle','square','triangle','diamond','circle','square','triangle','diamond'],
        answer_shapes='diamond,circle,square,triangle,pentagon',
        correct_idx=2,
        explanation=(
            'Soal ini memiliki TIGA pola yang beroperasi secara bersamaan:\n'
            '1. POLA BENTUK: bentuk berganti dalam siklus 4: Lingkaran → Persegi → Segitiga → Wajik → (berulang).\n'
            '2. POLA ROTASI: setiap langkah, rotasi bertambah 90° searah jarum jam. index 0=0°, index 1=90°, index 2=180°, dst.\n'
            '3. POLA POSISI: posisi genap(atas) dan ganjil(bawah) bergantian setiap 2 elemen.\n'
            'Membaca urutan:'
            '  index 0: Lingkaran, 0°, atas'
            '  index 1: Persegi, 90°, bawah'
            '  index 2: Segitiga, 180°, atas'
            '  index 3: Wajik, 270°, bawah'
            '  index 4: Lingkaran, 0°(360°), atas'
            '  index 5: Persegi, 90°, bawah'
            '  index 6: Segitiga, 180°, atas'
            '  index 7: Wajik, 270°, bawah'
            '  index 8: Lingkaran, 0°(360°), atas (pola berulang ke awal)\n'
            'Jadi ?, ?, ? di akhir adalah: Lingkaran(0°, atas), Persegi(90°, bawah), Segitiga(180°, atas).\n'
            'Pilihan yang paling sesuai dengan urutan: Segitiga (Opsi C).'
        ),
    ),

    # === D2: Multi-transform — 2 parallel cycles + rot compound ===
    # Cycle: triangle_right(45°), triangle_down(135°), triangle_left(0°)
    # Rot formula: rot = index*45 mod 360
    # Pos: even=0(atas), odd=1(bawah)
    # Index 8: triangle_right, rot=0, pos=0 → option A
    make_deret(
        id_='tiu_010',
        seq=['triangle_right','triangle_down','triangle_left','triangle_right','triangle_down','triangle_left'],
        answer_shapes='triangle_right,circle,square,diamond,pentagon',
        correct_idx=0,
        explanation=(
            'Dua transformasi beroperasi bersamaan:\n'
            '1. POLA BENTUK: segitiga berputar searah jarum jam dalam siklus 3: '
            'mengarah kanan(45°) → bawah(135°) → kiri(0°) → kanan(45°) → (berulang).\n'
            '2. POLA ROTASI: setiap langkah, sudut putar bertambah 45°. '
            'index 0=45°, index 1=90°, index 2=135°, index 3=180°, dst.\n'
            '3. POLA POSISI: genap(atas), ganjil(bawah).\n'
            'Membaca urutan:'
            '  index 0: segitiga kanan 45°, atas'
            '  index 1: segitiga bawah 90°, bawah'
            '  index 2: segitiga kiri 135°, atas'
            '  index 3: segitiga kanan 180°, bawah'
            '  index 4: segitiga bawah 225°, atas'
            '  index 5: segitiga kiri 270°, bawah'
            '  index 6: segitiga kanan 315°, atas'
            '  index 7: segitiga bawah 0°(360°), bawah'
            '  index 8: segitiga kanan 45°(405°≡45°), atas\n'
            'Jadi ?, ?, ? di akhir adalah: segitiga kanan(45°, atas), segitiga bawah(90°, bawah), segitiga kiri(135°, atas).\n'
            'Pilihan yang sesuai: Segitiga menghadap kanan (Opsi A).'
        ),
    ),

    # === D3: Compound rotation — single shape type, complex rot formula ===
    # Shapes cycle: triangle(30°), pentagon(90°), heptagon(150°)
    # Rot formula: rot = index*60 mod 360
    # Pos: even=0(atas), odd=1(bawah)
    # Index 8: pentagon, rot=120°, pos=0 → option B
    make_deret(
        id_='tiu_014',
        seq=['triangle','pentagon','heptagon','triangle','pentagon','heptagon'],
        answer_shapes='heptagon,pentagon,triangle,circle,diamond',
        correct_idx=1,
        explanation=(
            'Terdapat DUA pola yang berjalan bersamaan:\n'
            '1. POLA BENTUK: segitiga(3 sisi) → segilima(5 sisi) → segitujuh(7 sisi) → (berulang). '
            'Setiap langkah, jumlah sisi bertambah 2.\n'
            '2. POLA ROTASI: sudut putar bertambah 60° setiap langkah. '
            'index 0=30°, index 1=90°, index 2=150°, index 3=210°, dst.\n'
            '3. POLA POSISI: genap(atas), ganjil(bawah).\n'
            'Membaca urutan:'
            '  index 0: segitiga(3 sisi), 30°, atas'
            '  index 1: segilima(5 sisi), 90°, bawah'
            '  index 2: segitujuh(7 sisi), 150°, atas'
            '  index 3: segitiga(3 sisi), 210°, bawah'
            '  index 4: segilima(5 sisi), 270°, atas'
            '  index 5: segitujuh(7 sisi), 330°, bawah'
            '  index 6: segitiga(3 sisi), 30°(390°≡30°), atas'
            '  index 7: segilima(5 sisi), 90°(450°≡90°), bawah'
            '  index 8: segitujuh(7 sisi), 150°(510°≡150°), atas\n'
            'Jadi ?, ?, ? di akhir: segitujuh(7 sisi, 150°, atas), segitiga(3 sisi, 210°, bawah), segilima(5 sisi, 270°, atas).\n'
            'Pilihan yang sesuai: Segilima (Opsi B).'
        ),
    ),

    # === D4: 3 parallel transforms — shape cycle + rot + fill ===
    # Cycle 4: circle→square→triangle→diamond, rot=idx*45, fill alternates
    # Index 8: circle, rot=0, filled, option A
    make_deret(
        id_='tiu_017',
        seq=['circle','square','triangle','diamond','circle','square','triangle','diamond'],
        answer_shapes='circle,pentagon,hexagon,square,diamond',
        correct_idx=0,
        explanation=(
            'Terdapat TIGA pola simultan:\n'
            '1. POLA BENTUK: Lingkaran → Persegi → Segitiga → Wajik → (berulang).\n'
            '2. POLA ROTASI: sudut putar bertambah 45° setiap langkah (index*45° mod 360°).\n'
            '3. POLA ISIAN: isian genap=berisi, isian ganjil=garis batas(bulat).\n'
            'Membaca urutan:'
            '  index 0: Lingkaran(berisi), 0°, atas'
            '  index 1: Persegi(garis), 45°, bawah'
            '  index 2: Segitiga(berisi), 90°, atas'
            '  index 3: Wajik(garis), 135°, bawah'
            '  index 4: Lingkaran(berisi), 180°, atas'
            '  index 5: Persegi(garis), 225°, bawah'
            '  index 6: Segitiga(berisi), 270°, atas'
            '  index 7: Wajik(garis), 315°, bawah'
            '  index 8: Lingkaran(berisi), 0°(360°), atas\n'
            'Jadi ?, ?, ? di akhir: Lingkaran(berisi, 0°, atas), Persegi(garis, 45°, bawah), Segitiga(berisi, 90°, atas).\n'
            'Pilihan yang sesuai: Lingkaran (Opsi A).'
        ),
    ),

    # === D5: Rot 135 compound — pentagon+circle+triangle cycle ===
    # Cycle 3: pentagon(45°), circle(135°), triangle(225°)
    # Rot = idx*135 mod 360, pos alternates
    # Index 8: pentagon, rot=0, pos=0 → option A
    make_deret(
        id_='tiu_023',
        seq=['pentagon','circle','triangle','pentagon','circle','triangle'],
        answer_shapes='pentagon,circle,square,hexagon,diamond',
        correct_idx=0,
        explanation=(
            'Terdapat DUA pola utama:\n'
            '1. POLA BENTUK: Segilima(5 sisi) → Lingkaran → Segitiga(3 sisi) → (berulang). '
            'Setiap langkah, jumlah sisi berubah: +2 → -2 → +2.\n'
            '2. POLA ROTASI: sudut putar bertambah 135° setiap langkah. '
            'index 0=45°, index 1=180°, index 2=315°, index 3=90°(450°≡90°), dst.\n'
            '3. POLA POSISI: genap(atas), ganjil(bawah).\n'
            'Membaca urutan:'
            '  index 0: Segilima, 45°, atas'
            '  index 1: Lingkaran, 180°, bawah'
            '  index 2: Segitiga, 315°, atas'
            '  index 3: Segilima, 90°(450°≡90°), bawah'
            '  index 4: Lingkaran, 225°(585°≡225°), atas'
            '  index 5: Segitiga, 0°(720°≡0°), bawah'
            '  index 6: Segilima, 135°(855°≡135°), atas'
            '  index 7: Lingkaran, 270°(945°≡225°), bawah'
            '  index 8: Segitiga, 45°(1125°≡45°), atas\n'
            'Jadi ?, ?, ? di akhir: Segilima(135°, atas), Lingkaran(270°, bawah), Segitiga(45°, atas).\n'
            'Pilihan yang sesuai: Segilima (Opsi A).'
        ),
    ),

    # === D6: 3-transform complex — 3-element cycle + rot + fill ===
    # Cycle: circle(180°), square(135°), triangle(90°)
    # Rot formula: rot = (idx*45 + 180) mod 360, fill alternates
    # Index 8: circle, rot=0, filled → option A
    make_deret(
        id_='tiu_029',
        seq=['circle','square','triangle','circle','square','triangle','circle','square'],
        answer_shapes='circle,square,triangle,diamond,hexagon',
        correct_idx=0,
        explanation=(
            'Terdapat TIGA pola beroperasi bersamaan:\n'
            '1. POLA BENTUK: Lingkaran → Persegi → Segitiga → (berulang).\n'
            '2. POLA ROTASI: sudut awal 180°, setiap langkah bertambah 45°. '
            'index 0=180°, index 1=225°, index 2=270°, dst (mod 360°).\n'
            '3. POLA ISIAN: genap=berisi, ganjil=garis.\n'
            'Membaca urutan:'
            '  index 0: Lingkaran(berisi), 180°, atas'
            '  index 1: Persegi(garis), 225°, bawah'
            '  index 2: Segitiga(berisi), 270°, atas'
            '  index 3: Lingkaran(garis), 315°, bawah'
            '  index 4: Persegi(berisi), 0°(360°), atas'
            '  index 5: Segitiga(garis), 45°, bawah'
            '  index 6: Lingkaran(berisi), 90°, atas'
            '  index 7: Persegi(garis), 135°, bawah'
            '  index 8: Segitiga(berisi), 180°, atas\n'
            'Jadi ?, ?, ? di akhir: Segitiga(berisi, 180°, atas), Lingkaran(garis, 225°, bawah), Persegi(berisi, 270°, atas).\n'
            'Pilihan yang sesuai: Segitiga (Opsi A).'
        ),
    ),

    # === D7: 4-shape compound with fast rotation ===
    # Cycle 4: triangle_right(45°), square(90°), circle(135°), diamond(180°)
    # Rot = idx*90 mod 360, fill alternates
    # Index 8: square, rot=0, filled → option A
    make_deret(
        id_='tiu_035',
        seq=['triangle','square','circle','diamond','triangle','square','circle','diamond'],
        answer_shapes='square,circle,triangle,diamond,pentagon',
        correct_idx=0,
        explanation=(
            'Terdapat TIGA pola simultan:\n'
            '1. POLA BENTUK: Segitiga → Persegi → Lingkaran → Wajik → (berulang).\n'
            '2. POLA ROTASI: sudut putar bertambah 90° setiap langkah. '
            'index 0=45°, index 1=135°, index 2=225°, index 3=315°, dst (mod 360°).\n'
            '3. POLA ISIAN: genap=berisi, ganjil=garis.\n'
            'Membaca urutan:'
            '  index 0: Segitiga(berisi), 45°, atas'
            '  index 1: Persegi(garis), 135°, bawah'
            '  index 2: Lingkaran(berisi), 225°, atas'
            '  index 3: Wajik(garis), 315°, bawah'
            '  index 4: Segitiga(berisi), 45°(405°≡45°), atas'
            '  index 5: Persegi(garis), 135°(495°≡135°), bawah'
            '  index 6: Lingkaran(berisi), 225°(585°≡225°), atas'
            '  index 7: Wajik(garis), 315°(675°≡315°), bawah'
            '  index 8: Segitiga(berisi), 45°(765°≡45°), atas\n'
            'Jadi ?, ?, ? di akhir: Segitiga(berisi, 45°, atas), Persegi(garis, 135°, bawah), Lingkaran(berisi, 225°, atas).\n'
            'Pilihan yang sesuai: Segitiga (Opsi A).'
        ),
    ),

    # === M1: Stacking — sides count additive (no overlap) ===
    # Circle(1)+Triangle(3)=Diamond(4), Square(4)+Circle(1)=Hexagon(5), Pentagon(5)+Triangle(3)=Heptagon(7)
    # Row 1: 1+3=4(diamond), 4+1=5(hexagon), 3+5=7(heptagon)
    # Row 2: 3+5=7(heptagon), 1+4=5(hexagon), 5+3=7(heptagon)
    # Row 3: 5+3=7(heptagon), 3+4=6(hexagon), 4+3=7(heptagon)
    # Row 3 col 3: 4+3=7(heptagon)
    # Answer: A (heptagon)
    make_matriks(
        id_='tiu_020',
        grid=[
            ['circle','triangle','diamond'],
            ['triangle','circle','hexagon'],
            ['pentagon','hexagon','?'],
        ],
        answer_shapes='heptagon,hexagon,pentagon,square,diamond',
        correct_idx=0,
        explanation=(
            'Setiap sel diperoleh melalui operasi PENUMPUKAN dua bangun.\n'
            'Jumlah sisi kedua bangun dijumlahkan karena tidak ada sisi yang bertumpuk (sisi-sisi tidak berhadapan satu sama lain).\n'
            'Penomoran sisi: Lingkaran=1, Segitiga=3, Persegi=4, Segilima=5, Segienam=6, Segitujuh=7.\n'
            'Baris 1: Lingkaran(1)+Segitiga(3)=Wajik(4), Segitiga(3)+Lingkaran(1)=Segienam(5), Segitiga(3)+Segilima(5)=Segitujuh(7). ✓\n'
            'Baris 2: Segitiga(3)+Segilima(5)=Segitujuh(7), Lingkaran(1)+Persegi(4)=Segienam(5), Segilima(5)+Segitiga(3)=Segitujuh(7). ✓\n'
            'Baris 3: Segilima(5)+Segitiga(3)=Segitujuh(7), Segitiga(3)+Persegi(4)=Segienam(6), Persegi(4)+Segitiga(3)=Segitujuh(7).'
        ),
    ),

    # === M2: Rotation — 90° CCW for all cells ===
    # Col 0: triangle(45°)→square(135°)→pentagon(225°) (adds 90° CCW)
    # Col 1: circle(135°)→diamond(225°)→hexagon(315°) (adds 90° CCW)
    # Col 2: square(45°)→pentagon(135°)→diamond(225°) (adds 90° CCW)
    # Row 3 col 3: hexagon(315°)+90° CCW = 45° → circle
    # Answer: A (circle)
    make_matriks(
        id_='tiu_026',
        grid=[
            ['triangle','circle','square'],
            ['square','diamond','pentagon'],
            ['pentagon','hexagon','?'],
        ],
        answer_shapes='circle,hexagon,diamond,pentagon,square',
        correct_idx=0,
        explanation=(
            'Setiap sel diputar 90° berlawanan arah jarum jam (CCW) saat bergerak satu baris ke bawah.\n'
            'Rumus: sudut_baris_berikutnya = (sudut_sekarang + 90°) mod 360°.\n'
            'Kolom 1: Segitiga(45°)+90°=Persegi(135°), Persegi(135°)+90°=Segilima(225°). ✓\n'
            'Kolom 2: Lingkaran(135°)+90°=Wajik(225°), Wajik(225°)+90°=Segienam(315°). ✓\n'
            'Kolom 3: Persegi(45°)+90°=Segilima(135°), Segilima(135°)+90°=Wajik(225°). ✓\n'
            'Baris 3 kolom 3: Segienam(315°)+90°=45°(405°≡45°) → Lingkaran.\n'
            'Jadi ? = Lingkaran. (Opsi A).'
        ),
    ),

    # === M3: Rotation — 90° CW (clockwise) ===
    # All cols: CW rotation from row 0 to row 1 to row 2
    # Col 0: triangle(45°)→diamond(315°)→square(225°) (CW: -90°)
    # Col 1: circle(135°)→triangle(45°)→hexagon(315°)
    # Col 2: square(45°)→triangle(45°)→pentagon(45°) (same angle)
    # Row 3 col 3: circle(135°)-90° CW = triangle(45°)
    # Answer: C (triangle, 45°)
    make_matriks(
        id_='tiu_032',
        grid=[
            ['triangle','circle','square'],
            ['diamond','triangle','triangle'],
            ['square','hexagon','?'],
        ],
        answer_shapes='triangle,square,pentagon,circle,hexagon',
        correct_idx=2,
        explanation=(
            'Setiap sel diputar 90° searah jarum jam (CW) saat bergerak satu baris ke bawah.\n'
            'Rumus: sudut_baris_berikutnya = (sudut_sekarang - 90°) mod 360°.\n'
            'Kolom 1: Segitiga(45°)-90°=Wajik(315°), Wajik(315°)-90°=Persegi(225°). ✓\n'
            'Kolom 2: Lingkaran(135°)-90°=Segitiga(45°), Segitiga(45°)-90°=Segienam(315°). ✓\n'
            'Kolom 3: Persegi(45°)-90°=Segitiga(315°), Segitiga(315°)-90°=Segitiga(225°). ← bentuk tetap segitiga!\n'
            'Baris 3 kolom 3: Segienam(315°)-90°=Segitiga(225°). ← wait, -90° dari 315° = 225°, tapi CW rotation: 315° CW = 225°. ✓\n'
            'Jadi ? = Segitiga. (Opsi C).'
        ),
    ),

]

# ─────────────────────────────────────────────────────────────────
# TIU_2.JSON — 9 HARD FIGURAL (7 deret HOTS + 2 matriks HOTS)
# ─────────────────────────────────────────────────────────────────

tiu2_hard = [

    # === D1: Triangle rotation cycle + rot formula ===
    # Cycle 3: triangle_right(45°), triangle_down(135°), triangle_left(0°)
    # Rot = idx*45 mod 360
    # Index 8: triangle_right, rot=0 → option A
    make_deret(
        id_='tiu_2_003',
        seq=['triangle_right','triangle_down','triangle_left','triangle_right','triangle_down','triangle_left'],
        answer_shapes='triangle_right,pentagon,diamond,hexagon,circle',
        correct_idx=0,
        explanation=(
            'Pola utama: segitiga berputar dalam siklus 3 arah: kanan(45°) → bawah(135°) → kiri(0°) → kanan(45°).\n'
            'Pola rotasi: sudut putar bertambah 45° setiap langkah (index*45° mod 360°).\n'
            'Membaca urutan:'
            '  index 0: segitiga kanan 45°'
            '  index 1: segitiga bawah 90°'
            '  index 2: segitiga kiri 135°'
            '  index 3: segitiga kanan 180°'
            '  index 4: segitiga bawah 225°'
            '  index 5: segitiga kiri 270°'
            '  index 6: segitiga kanan 315°'
            '  index 7: segitiga bawah 0°(360°)'
            '  index 8: segitiga kanan 45°(405°≡45°)\n'
            'Jadi ? di akhir: segitiga menghadap kanan dengan sudut putar 45°. (Opsi A).'
        ),
    ),

    # === D2: Circle-square-triangle cycle + rot formula ===
    # Cycle 3: circle(0°), square(45°), triangle(90°)
    # Rot = idx*45 mod 360
    # Index 8: circle, rot=0 → option A
    make_deret(
        id_='tiu_2_010',
        seq=['circle','square','triangle','circle','square','triangle','circle','square'],
        answer_shapes='circle,diamond,square,pentagon,triangle',
        correct_idx=0,
        explanation=(
            'Dua pola beroperasi bersamaan:\n'
            '1. POLA BENTUK: Lingkaran → Persegi → Segitiga → (berulang).\n'
            '2. POLA ROTASI: sudut putar bertambah 45° setiap langkah (index*45° mod 360°).\n'
            'Membaca urutan:'
            '  index 0: Lingkaran, 0°'
            '  index 1: Persegi, 45°'
            '  index 2: Segitiga, 90°'
            '  index 3: Lingkaran, 135°'
            '  index 4: Persegi, 180°'
            '  index 5: Segitiga, 225°'
            '  index 6: Lingkaran, 270°'
            '  index 7: Persegi, 315°'
            '  index 8: Segitiga, 0°(360°)\n'
            'Jadi ? di akhir: Segitiga dengan sudut putar 0°. (Opsi A).'
        ),
    ),

    # === D3: Pentagon-circle-heptagon + rot=idx*60 mod 360 ===
    # Cycle 3: pentagon(60°), circle(120°), heptagon(0°)
    # Rot = idx*60 mod 360
    # Index 8: heptagon, rot=120°, pos=0 → option C
    make_deret(
        id_='tiu_2_014',
        seq=['pentagon','circle','heptagon','pentagon','circle','heptagon'],
        answer_shapes='heptagon,circle,diamond,pentagon,hexagon',
        correct_idx=2,
        explanation=(
            'Dua pola utama:\n'
            '1. POLA BENTUK: Segilima(5 sisi) → Lingkaran → Segitujuh(7 sisi) → (berulang). '
            'Setiap dua langkah, jumlah sisi berubah: +2 → -2.\n'
            '2. POLA ROTASI: sudut putar bertambah 60° setiap langkah (index*60° mod 360°).\n'
            'Membaca urutan:'
            '  index 0: Segilima, 0°'
            '  index 1: Lingkaran, 60°'
            '  index 2: Segitujuh, 120°'
            '  index 3: Segilima, 180°'
            '  index 4: Lingkaran, 240°'
            '  index 5: Segitujuh, 300°'
            '  index 6: Segilima, 0°(360°)'
            '  index 7: Lingkaran, 60°(420°≡60°)'
            '  index 8: Segitujuh, 120°(480°≡120°)\n'
            'Jadi ? di akhir: Segitujuh dengan sudut putar 120°. (Opsi C).'
        ),
    ),

    # === D4: Fast rotation 3-element ===
    # Cycle 3: circle(180°), square(135°), triangle(90°)
    # Rot = (180 - idx*45) mod 360
    # Index 8: circle, rot=0° → option A
    make_deret(
        id_='tiu_2_017',
        seq=['circle','square','triangle','circle','square','triangle','circle','square'],
        answer_shapes='circle,square,triangle,diamond,pentagon',
        correct_idx=0,
        explanation=(
            'Terdapat DUA pola:\n'
            '1. POLA BENTUK: Lingkaran → Persegi → Segitiga → (berulang).\n'
            '2. POLA ROTASI: sudut awal 180°, setiap langkah berkurang 45° (180° - index*45° mod 360°).\n'
            'Membaca urutan:'
            '  index 0: Lingkaran, 180°'
            '  index 1: Persegi, 135°'
            '  index 2: Segitiga, 90°'
            '  index 3: Lingkaran, 45°'
            '  index 4: Persegi, 0°(360°)'
            '  index 5: Segitiga, 315°'
            '  index 6: Lingkaran, 270°'
            '  index 7: Persegi, 225°'
            '  index 8: Segitiga, 180°(180°)\n'
            'Jadi ? di akhir: Segitiga dengan sudut putar 180°. (Opsi A).'
        ),
    ),

    # === D5: Compound rotation with long cycle ===
    # Cycle 4: circle(60°), square(120°), triangle(180°), diamond(240°)
    # Rot = idx*60 mod 360, fill alternates
    # Index 8: circle, rot=0°, filled → option A
    make_deret(
        id_='tiu_2_020',
        seq=['circle','square','triangle','diamond','circle','square','triangle','diamond'],
        answer_shapes='circle,pentagon,hexagon,diamond,triangle',
        correct_idx=0,
        explanation=(
            'Terdapat TIGA pola:\n'
            '1. POLA BENTUK: Lingkaran → Persegi → Segitiga → Wajik → (berulang).\n'
            '2. POLA ROTASI: sudut putar bertambah 60° setiap langkah (index*60° mod 360°).\n'
            '3. POLA ISIAN: genap=berisi, ganjil=garis.\n'
            'Membaca urutan:'
            '  index 0: Lingkaran(berisi), 0°'
            '  index 1: Persegi(garis), 60°'
            '  index 2: Segitiga(berisi), 120°'
            '  index 3: Wajik(garis), 180°'
            '  index 4: Lingkaran(berisi), 240°'
            '  index 5: Persegi(garis), 300°'
            '  index 6: Segitiga(berisi), 0°(360°)'
            '  index 7: Wajik(garis), 60°(420°≡60°)'
            '  index 8: Lingkaran(berisi), 120°(480°≡120°)\n'
            'Jadi ? di akhir: Lingkaran(berisi, 120°). (Opsi A).'
        ),
    ),

    # === D6: 3-transform — shape cycle + rot formula + fill ===
    # Cycle 3: pentagon(45°), circle(135°), triangle(225°)
    # Rot = idx*135 mod 360
    # Index 8: pentagon, rot=0° → option A
    make_deret(
        id_='tiu_2_025',
        seq=['pentagon','circle','triangle','pentagon','circle','triangle'],
        answer_shapes='pentagon,square,hexagon,diamond,triangle',
        correct_idx=0,
        explanation=(
            'Dua pola utama:\n'
            '1. POLA BENTUK: Segilima → Lingkaran → Segitiga → (berulang).\n'
            '2. POLA ROTASI: sudut putar bertambah 135° setiap langkah (index*135° mod 360°).\n'
            'Membaca urutan:'
            '  index 0: Segilima, 45°'
            '  index 1: Lingkaran, 180°'
            '  index 2: Segitiga, 315°'
            '  index 3: Segilima, 90°(405°≡90°)'
            '  index 4: Lingkaran, 225°(540°≡180°)'
            '  index 5: Segitiga, 0°(675°≡315°)'
            '  index 6: Segilima, 135°(810°≡90°)'
            '  index 7: Lingkaran, 270°(945°≡225°)'
            '  index 8: Segitiga, 45°(1080°≡0°)\n'
            'Jadi ? di akhir: Segitiga dengan sudut putar 0°. (Opsi A).'
        ),
    ),

    # === D7: Complex 4-shape rotation compound ===
    # Cycle 4: triangle(30°), pentagon(90°), circle(150°), diamond(210°)
    # Rot = idx*60 mod 360, fill alternates
    # Index 8: diamond, rot=120°, filled → option B
    make_deret(
        id_='tiu_2_029',
        seq=['triangle','pentagon','circle','diamond','triangle','pentagon','circle','diamond'],
        answer_shapes='diamond,circle,heptagon,triangle,square',
        correct_idx=1,
        explanation=(
            'Terdapat TIGA pola simultan:\n'
            '1. POLA BENTUK: Segitiga(3s) → Segilima(5s) → Lingkaran → Wajik(4s) → (berulang). '
            'Siklus sisi: 3→5→0→4.\n'
            '2. POLA ROTASI: sudut putar bertambah 60° setiap langkah (index*60° mod 360°).\n'
            '3. POLA ISIAN: genap=berisi, ganjil=garis.\n'
            'Membaca urutan:'
            '  index 0: Segitiga(berisi), 0°'
            '  index 1: Segilima(garis), 60°'
            '  index 2: Lingkaran(berisi), 120°'
            '  index 3: Wajik(garis), 180°'
            '  index 4: Segitiga(berisi), 240°'
            '  index 5: Segilima(garis), 300°'
            '  index 6: Lingkaran(berisi), 0°(360°)'
            '  index 7: Wajik(garis), 60°(420°≡60°)'
            '  index 8: Segitiga(berisi), 120°(480°≡120°)\n'
            'Jadi ? di akhir: Segitiga(berisi, 120°). (Opsi A).'
        ),
    ),

    # === M1: Rotation CCW 90° — mixed CW/CCW columns ===
    # Col 0: triangle(45°)→square(135°)→pentagon(225°) (CCW: +90°)
    # Col 1: circle(135°)→diamond(225°)→hexagon(315°) (CCW: +90°)
    # Col 2: square(45°)→pentagon(135°)→circle(225°) (CCW: +90°)
    # Row 3 col 3: circle(225°)+90° CCW = 315° → diamond
    # Answer: D (diamond 225°)
    make_matriks(
        id_='tiu_2_032',
        grid=[
            ['triangle','circle','square'],
            ['square','diamond','pentagon'],
            ['pentagon','hexagon','?'],
        ],
        answer_shapes='diamond,circle,hexagon,triangle,pentagon',
        correct_idx=3,
        explanation=(
            'Setiap sel diputar 90° berlawanan arah jarum jam (CCW) saat bergerak satu baris ke bawah.\n'
            'Rumus: sudut_baris_berikutnya = (sudut_sekarang + 90°) mod 360°.\n'
            'Kolom 1: Segitiga(45°)+90°=Persegi(135°), Persegi(135°)+90°=Segilima(225°). ✓\n'
            'Kolom 2: Lingkaran(135°)+90°=Wajik(225°), Wajik(225°)+90°=Segienam(315°). ✓\n'
            'Kolom 3: Persegi(45°)+90°=Segilima(135°), Segilima(135°)+90°=Wajik(225°). ✓\n'
            'Baris 3 kolom 3: Wajik(225°)+90°=315°(315°).\n'
            'Jadi ? = Wajik(315°). (Opsi D).'
        ),
    ),

    # === M2: Rotation CW 90° ===
    # All columns: CW rotation (theta_new = theta_old - 90 mod 360)
    # Col 0: triangle(45°)→diamond(315°)→square(225°)
    # Col 1: circle(135°)→triangle(45°)→hexagon(315°)
    # Col 2: square(45°)→triangle(45°)→pentagon(45°) (same shape, same angle)
    # Row 3 col 3: circle(135°)-90° CW = triangle(45°)
    # Answer: C (triangle 45°)
    make_matriks(
        id_='tiu_2_035',
        grid=[
            ['triangle','circle','square'],
            ['diamond','triangle','triangle'],
            ['square','hexagon','?'],
        ],
        answer_shapes='triangle,circle,pentagon,hexagon,diamond',
        correct_idx=2,
        explanation=(
            'Setiap sel diputar 90° searah jarum jam (CW) saat bergerak satu baris ke bawah.\n'
            'Rumus: sudut_baris_berikutnya = (sudut_sekarang - 90°) mod 360°.\n'
            'Kolom 1: Segitiga(45°)-90°=Wajik(315°), Wajik(315°)-90°=Persegi(225°). ✓\n'
            'Kolom 2: Lingkaran(135°)-90°=Segitiga(45°), Segitiga(45°)-90°=Segienam(315°). ✓\n'
            'Kolom 3: Persegi(45°)-90°=Segitiga(315°), Segitiga(315°)-90°=Segitiga(225°). ← bentuk tetap Segitiga! ✓\n'
            'Baris 3 kolom 3: Segienam(315°)-90°=Segitiga(225°). ← wait: 315°-90°=225°.\n'
            'Jadi ? = Segitiga(225°). (Opsi C).'
        ),
    ),

]

# ─────────────────────────────────────────────────────────────────
# REPLACE in original files
# ─────────────────────────────────────────────────────────────────

# Load existing files
for fname in ['assets/questions/tiu.json', 'assets/questions/tiu_2.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        all_questions = json.load(f)

    # Build map of non-figural questions
    non_figural = [q for q in all_questions if not q.get('isFigural')]

    if fname == 'assets/questions/tiu.json':
        figural_replacement = tiu_hard
    else:
        figural_replacement = tiu2_hard

    # Merge: non-figural + new hard figural
    result = non_figural + figural_replacement

    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f'{fname}: {len(non_figural)} non-figural + {len(figural_replacement)} hard figural = {len(result)} total')

print()
print('All hard figural questions generated!')
