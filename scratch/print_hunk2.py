import subprocess

res = subprocess.run(['git', 'diff', 'HEAD', 'index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(res.stdout[res.stdout.find('@@ -1419'):res.stdout.find('@@ -1419')+2000])
