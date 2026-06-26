with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

keywords = ["fiverr", "freelance", "saved businesses", "10+ hours", "10+ hrs"]
for kw in keywords:
    idx = text.lower().find(kw.lower())
    if idx != -1:
        print(f"Found keyword '{kw}' at position {idx}:")
        print(text[idx-50:idx+150])
        print("="*40)
    else:
        print(f"Keyword '{kw}' not found in index.html")
