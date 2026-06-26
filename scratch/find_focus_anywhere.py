with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = list(re.finditer(re.escape('id="focus"'), text, re.IGNORECASE))
print(f"Found {len(matches)} id=\"focus\" in index.html")
for m in matches:
    print(text[m.start()-100:m.start()+800])
