with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.lower().find('ltts')
if idx != -1:
    print("Found 'LTTS' in index.html at char", idx)
    print(text[idx-200:idx+800])
else:
    print("'LTTS' not found in index.html")
