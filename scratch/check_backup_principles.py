with open('d:/profile/index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's see if id="principles" exists
idx = text.find('id="principles"')
if idx != -1:
    print("Found id=\"principles\" in index.html.bak around char", idx)
    print(text[idx-100:idx+1000])
else:
    print("id=\"principles\" not found in index.html.bak")
