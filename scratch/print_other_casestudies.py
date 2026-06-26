with open('d:/profile/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('projectsData =')
if idx != -1:
    data_text = text[idx:]
    
    def print_case_study(proj_id):
        proj_idx = data_text.find(f"{proj_id}: {{")
        if proj_idx != -1:
            start_tag = 'caseStudyHTML: `'
            start_idx = data_text.find(start_tag, proj_idx)
            if start_idx != -1:
                start_pos = start_idx + len(start_tag)
                end_pos = data_text.find('`', start_pos)
                print(f"--- CASE STUDY FOR {proj_id} ---")
                print(data_text[start_pos:end_pos][:1500])
                print("\n...[truncated]...\n")
                print(data_text[start_pos:end_pos][-800:])
                print("="*60)
                
    print_case_study('chat')
    print_case_study('tracker')
    print_case_study('healthchecker')
else:
    print("projectsData not found")
