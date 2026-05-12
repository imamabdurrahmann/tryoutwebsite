import json, os, re

base = r'c:\Users\muham\tryout_cpns\assets\questions'

# English indicators (threshold: 3+ words = likely English/mixed)
eng_patterns = [
    r'\bthe\b', r'\bis\b', r'\bare\b', r'\bwas\b', r'\bwere\b',
    r'\bThis\b', r'\bThe\b', r'\bbecause\b', r'\btherefore\b',
    r'\bcorrect\b', r'\bincorrect\b', r'\banswer\b', r'\boption\b',
    r'\bwhich\b', r'\bthat\b', r'\bwith\b', r'\bfrom\b', r'\bhave\b',
    r'\bSince\b', r'\bHowever\b', r'\bThus\b', r'\bHence\b',
    r'\beach\b', r'\bnot\b', r'\bfor\b', r'\bbut\b', r'\band\b',
    r'\bcan\b', r'\bwill\b', r'\bnor\b', r'\bneither\b', r'\bpure\b',
]

# Mapping English fragments to Indonesian
replacements = {
    # Common English phrases in math/logic explanations
    'each': 'masing-masing',
    'Next': 'Selanjutnya',
    'next': 'selanjutnya',
    'So ': 'Jadi ',
    'Therefore': 'Oleh karena itu',
    'therefore': 'oleh karena itu',
    'However': 'Namun',
    'Thus': 'Dengan demikian',
    'Hence': 'Maka',
    'Since': 'Karena',
    'because': 'karena',
    'the correct answer': 'jawaban yang benar',
    'The correct answer': 'Jawaban yang benar',
    'is correct': 'adalah benar',
    'is incorrect': 'adalah salah',
    'the answer is': 'jawabannya adalah',
    'The answer is': 'Jawabannya adalah',
    'option': 'opsi',
    'Option': 'Opsi',
    'neither': 'bukan',
    'nor': 'maupun',
    'pure': 'murni',
    'balanced': 'seimbang',
    'approach': 'pendekatan',
    'optimal': 'optimal',
    'nuanced': 'bernuansa',
    'prioritizes': 'memprioritaskan',
    'emotional': 'emosional',
    'adaptation': 'adaptasi',
    'literalism': 'literalisme',
    'complete': 'sepenuhnya',
}

def has_english(text):
    """Check if text has significant English content"""
    count = 0
    for pat in eng_patterns:
        count += len(re.findall(pat, text))
    return count >= 3

def translate_explanation(exp):
    """Best-effort translation of mixed English/Indonesian to pure Indonesian"""
    result = exp
    for eng, ind in replacements.items():
        result = result.replace(eng, ind)
    return result

files = ['twk.json','twk_2.json','twk_3.json','tiu.json','tiu_2.json','tiu_3.json','tkp.json','tkp_2.json','tkp_3.json']

total_fixed = 0

for fname in files:
    fp = os.path.join(base, fname)
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data:
        exp = q.get('explanation', '')
        if has_english(exp):
            new_exp = translate_explanation(exp)
            if new_exp != exp:
                q['explanation'] = new_exp
                modified = True
                total_fixed += 1
                print(f"FIXED {q['questionId']} in {fname}")
                print(f"  BEFORE: {exp[:100]}...")
                print(f"  AFTER:  {new_exp[:100]}...")
                print()
    
    if modified:
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"SAVED: {fname}")

print(f"\nTotal fixed: {total_fixed} explanations")
