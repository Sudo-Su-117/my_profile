import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/untruncated_master_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "How I Build Systems" in the text and print surrounding context
idx = text.find('HOW I BUILD SYSTEMS')
if idx == -1:
    idx = text.find('How I Build Systems')

if idx != -1:
    print("Found How I Build Systems section:")
    print(text[idx:idx+2000])
else:
    print("How I Build Systems section not found in spec text")
