import json, re

with open('assets/questions/twk_3.json', encoding='utf-8') as f:
    data = json.load(f)

fixes = 0

for q in data:
    for key in ['questionText', 'explanation']:
        if key in q:
            # Remove all non-ASCII
            cleaned = q[key].encode('ascii', 'ignore').decode('ascii')
            if cleaned != q[key]:
                print(f"Fixed {q['id']} {key}")
                q[key] = cleaned
                fixes += 1
    for i, opt in enumerate(q.get('options', [])):
        cleaned = opt.encode('ascii', 'ignore').decode('ascii')
        if cleaned != opt:
            print(f"Fixed {q['id']} opt[{i}]")
            q['options'][i] = cleaned
            fixes += 1

with open('assets/questions/twk_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Validate
bad = 0
for i, q in enumerate(data):
    for key in ['questionText', 'answer', 'explanation']:
        if key in q:
            if re.search(r'[^\x00-\x7F]', str(q[key])):
                print(f"Q{i+1} {key}: NON-ASCII")
                bad += 1
    for j, opt in enumerate(q.get('options', [])):
        if re.search(r'[^\x00-\x7F]', str(opt)):
            print(f"Q{i+1} opt[{j}]: NON-ASCII")
            bad += 1

hard = sum(1 for q in data if q['difficulty'] == 'hard')
print(f"Total: {len(data)}, Hard: {hard}, Non-ASCII: {bad}")
print(f"Fixes applied: {fixes}")
print("DONE")
