import json
import os

files = ['tiu', 'tiu_2', 'tiu_3', 'tkp', 'tkp_2', 'tkp_3']

for f in files:
    path = f'assets/questions/{f}.json'
    if not os.path.exists(path):
        print(f'{f}.json: FILE NOT FOUND')
        continue
    with open(path, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    
    print(f'\n=== {f}.json ===')
    print(f'  Total questions: {len(data)}')
    if not data:
        print('  EMPTY FILE!')
        continue
    
    # Check keys
    print(f'  Keys: {list(data[0].keys())}')
    
    # Check subcategories
    subcats = {}
    issues = []
    for i, q in enumerate(data):
        sc = q.get('subcategory', q.get('subcategory', '???'))
        subcats[sc] = subcats.get(sc, 0) + 1
        
        # Check for missing/empty fields
        qid = q.get('id', q.get('questionId', ''))
        qtext = q.get('question', q.get('questionText', ''))
        opts = q.get('options', [])
        ans = q.get('answer', '')
        
        if not qid:
            issues.append(f'  Q#{i}: MISSING ID')
        if not qtext or len(qtext) < 10:
            issues.append(f'  Q#{i} ({qid}): EMPTY/SHORT questionText')
        if not opts or len(opts) < 4:
            issues.append(f'  Q#{i} ({qid}): Missing/insufficient options ({len(opts)})')
        if not ans:
            issues.append(f'  Q#{i} ({qid}): MISSING answer')
        
        # Check answer validity
        if ans and ans not in ['A', 'B', 'C', 'D', 'E']:
            issues.append(f'  Q#{i} ({qid}): INVALID answer="{ans}"')
        
        # For TKP check 5 options
        if 'tkp' in f and opts and len(opts) != 5:
            issues.append(f'  Q#{i} ({qid}): TKP should have 5 options, has {len(opts)}')
    
    print(f'  Subcategories: {subcats}')
    
    if issues:
        print(f'  ISSUES FOUND ({len(issues)}):')
        for iss in issues[:15]:
            print(f'    {iss}')
        if len(issues) > 15:
            print(f'    ... and {len(issues)-15} more issues')
    else:
        print(f'  ✓ No issues found')
