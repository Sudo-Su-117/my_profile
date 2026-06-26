with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if '<section' in line or 'id="skills"' in line or 'id="journey"' in line:
        print(f"{idx}: {line.strip()}")
