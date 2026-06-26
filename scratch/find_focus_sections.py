import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/redesign_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find any occurrences of "focus" that are followed by headings or lists
matches = re.finditer(r'focus', text, re.IGNORECASE)
for m in matches:
    print(f"Char {m.start()}:")
    print(text[m.start()-50:m.start()+250])
    print("="*40)
