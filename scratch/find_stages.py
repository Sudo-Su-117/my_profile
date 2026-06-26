import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/profile/untruncated_master_spec.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for stages
stages = ["Business Problem", "Understand Requirements", "Identify Constraints", "Design Architecture", "Build the Simplest Working System", "Validate", "Iterate", "Optimize", "Scale"]
for stage in stages:
    idx = text.lower().find(stage.lower())
    if idx != -1:
        print(f"Found stage '{stage}' at char {idx}:")
        print(text[idx-50:idx+250])
        print("="*40)
