import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/untruncated_master_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.lower().find('agentic ai')
if idx != -1:
    print("Found 'Agentic AI' in spec:")
    print(text[idx-200:idx+800])
else:
    print("'Agentic AI' not found in spec")
