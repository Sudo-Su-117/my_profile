import os
import re

files = ['redesign_spec.txt', 'untruncated_master_spec.txt', 'full_redesign_spec.txt']
for fn in files:
    path = os.path.join('d:/profile', fn)
    if os.path.exists(path):
        print(f"--- Searching {fn} ---")
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for m in re.finditer(r'agentic', content, re.IGNORECASE):
            print(f"Found 'agentic' at char {m.start()}:")
            print(content[m.start()-100:m.start()+400])
            print("="*40)
