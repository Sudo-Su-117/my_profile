import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/untruncated_master_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if any(term in line.lower() for term in ['principle', 'philosophy']):
        print(f"{idx}: {line.strip()}")
