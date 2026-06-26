import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/redesign_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find sections or headings by splitting by double newlines or lines starting with # or capital letters
lines = text.split('\n')
for idx, line in enumerate(lines, 1):
    if line.strip().isupper() or line.strip().startswith('#'):
        print(f"{idx}: {line.strip()}")
