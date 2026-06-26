import re

with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('projectsData =')
if idx != -1:
    data_text = text[idx:idx+25000] # get a large chunk
    print("Occurrences of 'architecture' in projectsData:")
    for m in re.finditer(re.escape('architecture'), data_text, re.IGNORECASE):
        print(f"Char {m.start()}: {data_text[m.start()-50:m.start()+100].strip()}")
else:
    print("projectsData not found")
