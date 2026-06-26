import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/untruncated_master_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = list(re.finditer(re.escape('Current Focus'), text))
print(f"Found {len(matches)} occurrences:")
for m in matches:
    print(f"Char {m.start()}:")
    print(text[m.start()-50:m.start()+400].strip())
    print("="*60)
