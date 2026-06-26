import re

def search_file(filepath):
    print(f"--- Searching {filepath} ---")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for idx, line in enumerate(f, 1):
            if any(term in line.lower() for term in ['principle', 'philosophy', 'how i think', 'start with the business', 'architecture before']):
                print(f"{idx}: {line.strip()}")

search_file('d:/profile/redesign_spec.txt')
search_file('d:/profile/untruncated_master_spec.txt')
search_file('d:/profile/full_redesign_spec.txt')
