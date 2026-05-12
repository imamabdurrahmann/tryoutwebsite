import json, os, re

base = r'c:\Users\muham\tryout_cpns\assets\questions'
files = ['twk.json','twk_2.json','twk_3.json','tiu.json','tiu_2.json','tiu_3.json','tkp.json','tkp_2.json','tkp_3.json']

# English indicators
eng_patterns = [
    r'\bthe\b', r'\bis\b', r'\bare\b', r'\bwas\b', r'\bwere\b',
    r'\bThis\b', r'\bThe\b', r'\bbecause\b', r'\btherefore\b',
    r'\bcorrect\b', r'\bincorrect\b', r'\banswer\b', r'\boption\b',
    r'\bwhich\b', r'\bthat\b', r'\bwith\b', r'\bfrom\b', r'\bhave\b',
    r'\bSince\b', r'\bHowever\b', r'\bThus\b', r'\bHence\b',
]

for fname in files:
    fp = os.path.join(base, fname)
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    eng_count = 0
    total = len(data)
    examples = []
    for q in data:
        exp = q.get('explanation', '')
        # Count English words
        eng_words = 0
        for pat in eng_patterns:
            eng_words += len(re.findall(pat, exp))
        if eng_words >= 3:  # at least 3 English indicator words
            eng_count += 1
            if len(examples) < 2:
                examples.append(f"  {q['questionId']}: {exp[:150]}...")
    
    print(f"\n{'='*60}")
    print(f"FILE: {fname} ({total} soal)")
    print(f"Soal dengan pembahasan INGGRIS/CAMPURAN: {eng_count}/{total}")
    if examples:
        print("Contoh:")
        for e in examples:
            print(e)
