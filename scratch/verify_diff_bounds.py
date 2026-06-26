import subprocess
import re

res = subprocess.run(['git', 'diff', 'HEAD', 'index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
hunks = re.findall(r'@@ -\d+,\d+ \+\d+,\d+ @@', res.stdout)
print("Diff hunks:")
for hunk in hunks:
    print(hunk)
