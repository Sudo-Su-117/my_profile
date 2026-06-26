with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('projectsData =')
if idx != -1:
    print("Found projectsData in index.html:")
    print(text[idx:idx+2500])
else:
    print("projectsData not found in index.html")
