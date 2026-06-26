with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.lower().find('id="focus"')
if idx == -1:
    idx = text.lower().find('current focus')

if idx != -1:
    print("Found focus section in HTML:")
    print(text[idx-200:idx+2000])
else:
    print("Focus section not found in index.html")
