with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = 148192
print(text[pos-500:pos+500])
