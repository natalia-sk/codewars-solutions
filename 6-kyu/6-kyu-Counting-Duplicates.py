def duplicate_count(text):
    lc_text = text.lower()
    dupl = set()
    for i in lc_text:
        if lc_text.count(i) > 1:
            dupl.add(i)
    return len(dupl)
