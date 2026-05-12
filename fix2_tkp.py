import json, re

with open('assets/questions/tkp.json', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Russian words
    ("программагода", "program kerja"),
    ("предложение", " предложan"),
    ("программаур", "program"),
    ("Температура", "Suhu"),
    ("Публикация", "Publikasi"),
    ("программа", "program"),
    ("Результат", "Hasil"),
    ("транзиції", "transisi"),
    ("Документы", "Dokumen"),
    ("востиные", "berita"),
    ("Ситуация", "Situasi"),
    ("ландшафт", "lanskap"),
    ("нарратив", "narasi"),
    ("Практика", "Praktik"),
    ("разрешен", "diperbolehkan"),
    ("коллегия", "majelis"),
    ("финансов", "keuangan"),
    ("курсовая", "tugas akhir"),
    ("Пациент", "Pasien"),
    ("плоский", "datar"),
    ("Коллеги", "Rekan-rekan"),
    ("болашак", ""),
    ("большой", "besar"),
    ("статусе", "status"),
    ("Санкции", "Sanksi"),
    ("времени", "waktu"),
    ("проблем", "masalah"),
    ("статус", "status"),
    ("равный", "setara"),
    ("شخصный", "pribadi"),
    ("أو司法机关", ""),
    ("оворить", "berbicara"),
    ("первой", "pertama"),
    ("жарный", "panas"),
    ("участі", "partisipasi"),
    ("фликт", "konflik"),
    ("Имеет", "Memiliki"),
    ("или转移", ""),
    ("медиа", "media"),
    ("услуг", "layanan"),
    ("После", "Setelah"),
    ("рталы", "portal"),
    ("интер", "internet"),
    ("н可能导致", ""),
    ("Медиа", "Media"),
    ("Библи", "perpust"),
    ("групп", "kelompok"),
    ("Студент", "Mahasiswa"),
    ("Декан", "Dekan"),
    ("адпт", "adaptasi"),
    ("стандар", "standar"),
    ("унів", "mahasiswa"),
    ("кажд", "setiap"),
    ("всех", "semua"),
    ("выше", "di atas"),
    ("质量问题", ""),
    ("和的关系", ""),
    ("щита", ""),
    ("слеп", ""),
    ("флэш", ""),
    ("Сдня", ""),
    ("игры", "permainan"),
    ("董事会", "direksi"),
    ("ман", ""),
    ("сле", ""),
    ("для", "untuk"),
    ("или", "atau"),
    ("会影响", ""),
    ("虽然是", ""),
    ("н浪费", ""),
    ("ека", ""),
    ("все", "semua"),
    ("ром", ""),
    ("име", ""),
    ("сти", ""),
    ("два", "dua"),
    ("соз", ""),
    ("ния", ""),
    ("они", ""),
    ("дру", ""),
    ("—逃避", "-"),
    ("рт", ""),
    ("仮設", ""),
    ("如果", ""),
    ("си", ""),
    ("Да", "Ya"),
    ("во", ""),
    ("На", "Di"),
    ("то", ""),
    ("им", ""),
    ("ли", ""),
    ("ль", ""),
    ("н", ""),
    # Latin accented chars
    ("á", "a"), ("ä", "a"), ("ã", "a"),
    ("ç", "c"),
    ("é", "e"), ("ê", "e"),
    ("ó", "o"), ("õ", "o"), ("ö", "o"), ("ú", "u"),
    ("ę", "e"),
    # Cyrillic single letters
    ("Б", ""), ("В", ""), ("Д", ""), ("И", ""), ("К", ""),
    ("М", ""), ("Н", ""), ("П", ""), ("Р", ""), ("С", ""), ("Т", ""),
    ("а", ""), ("б", ""), ("в", ""), ("г", ""), ("д", ""), ("е", ""),
    ("ж", ""), ("з", ""), ("и", ""), ("й", ""), ("к", ""), ("л", ""),
    ("м", ""), ("н", ""), ("о", ""), ("п", ""), ("р", ""), ("с", ""),
    ("т", ""), ("у", ""), ("ф", ""), ("х", ""), ("ц", ""), ("ч", ""),
    ("ш", ""), ("щ", ""), ("ы", ""), ("ь", ""), ("э", ""), ("я", ""),
    ("і", ""), ("ї", ""),
    # Arabic
    ("أ", ""), ("خ", ""), ("ش", ""), ("ص", ""), ("و", ""),
    # CJK
    ("事", ""), ("仮", ""), ("会", ""), ("关", ""), ("可", ""),
    ("司", ""), ("响", ""), ("如", ""), ("导", ""), ("将", ""),
    ("影", ""), ("是", ""), ("机", ""), ("果", ""), ("法", ""),
    ("浪", ""), ("然", ""), ("的", ""), ("移", ""), ("系", ""),
    ("能", ""), ("致", ""), ("董", ""), ("虽", ""), ("設", ""),
    ("质", ""), ("费", ""), ("转", ""), ("逃", ""), ("避", ""),
    ("量", ""), ("问", ""), ("题", ""),
    # Korean
    ("년", ""), ("도", ""),
    # Punctuation
    ("，", ""),
    ("—", "-"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

print(f"Replacements made: {count}")

with open('assets/questions/tkp.json', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('assets/questions/tkp.json', encoding='utf-8') as f:
    data = json.load(f)

bad = []
for i, q in enumerate(data):
    for field in ['questionText', 'options', 'explanation', 'answer']:
        val = str(q.get(field, ''))
        if re.search(r'[^\x00-\x7F]', val):
            bad.append((i+1, field))

if bad:
    print(f"STILL {len(bad)} fields with non-ASCII")
    chars = set()
    for i, q in enumerate(data):
        for field in ['questionText', 'options', 'explanation', 'answer']:
            val = str(q.get(field, ''))
            found = re.findall(r'[^\x00-\x7F]', val)
            chars.update(found)
    print(f"Remaining unique chars: {sorted(chars)}")
else:
    print("TKP PAKET 1: SEMBUH!")
print(f"Total: {len(data)}")
