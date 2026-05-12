import json, re

with open('assets/questions/tkp.json', encoding='utf-8') as f:
    content = f.read()

# Get all remaining non-ASCII words (length >= 2)
remaining_words = {}
for m in re.finditer(r'[^\x00-\x7F]{2,}', content):
    seg = m.group()
    if seg not in remaining_words:
        remaining_words[seg] = m.start()

print(f"Remaining {len(remaining_words)} non-ASCII words:")
# Sort by length descending
for seg in sorted(remaining_words.keys(), key=lambda x: -len(x))[:100]:
    print(f"  [{len(seg)}] {repr(seg)}")
