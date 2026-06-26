import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/redesign_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(330, 365):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()}")
