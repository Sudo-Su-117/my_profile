import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/full_redesign_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = list(re.finditer(r'focus', text, re.IGNORECASE))
print(f"Found {len(matches)} in full_redesign_spec.txt:")
for m in matches:
    print(f"Char {m.start()}:")
    print(text[m.start()-50:m.start()+250])
    print("="*40)
