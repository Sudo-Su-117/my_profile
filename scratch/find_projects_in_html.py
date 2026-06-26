with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if 'id="projects"' in line or 'flagship' in line.lower() or 'knowledge management' in line.lower():
        if idx > 1500 and idx < 1900:
            print(f"{idx}: {line.strip()}")
