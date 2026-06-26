with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if './images/Screenshot' in line or './images/healthChecker' in line or './images/chatapp' in line or './images/amazon bot' in line:
        print(f"{idx}: {line.strip()}")
