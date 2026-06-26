import subprocess

res = subprocess.run(['git', 'diff', 'HEAD', 'index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
diff_lines = res.stdout.split('\n')

# Let's count how many additions and deletions are inside or outside journey section
deletions_outside = 0
additions_outside = 0
inside_journey = False

for line in diff_lines:
    if line.startswith('@@'):
        # Parse line range if needed, but we can just check context
        pass
    elif line.startswith('-'):
        # Check if this deletion is inside the journey section by looking at its content or context
        if not inside_journey:
            deletions_outside += 1
            if deletions_outside < 20:
                print("Deletion outside journey:", line)
    elif line.startswith('+'):
        if not inside_journey:
            additions_outside += 1
            if additions_outside < 20:
                print("Addition outside journey:", line)

print(f"Total additions outside journey: {additions_outside}")
print(f"Total deletions outside journey: {deletions_outside}")
