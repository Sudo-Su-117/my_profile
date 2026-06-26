with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('projectsData =')
if idx != -1:
    data_text = text[idx:]
    # Let's extract between caseStudyHTML: ` and the next closing backtick `
    start_tag = 'caseStudyHTML: `'
    start_idx = data_text.find(start_tag)
    if start_idx != -1:
        start_pos = start_idx + len(start_tag)
        end_pos = data_text.find('`', start_pos)
        print(data_text[start_pos:end_pos])
    else:
        print("caseStudyHTML not found")
else:
    print("projectsData not found")
