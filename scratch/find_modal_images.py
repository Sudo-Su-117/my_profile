with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.finditer(r'images:\s*\[([^\]]+)\]', text)
for m in matches:
    print("Found images array:")
    print(m.group(0))
    print("="*40)
