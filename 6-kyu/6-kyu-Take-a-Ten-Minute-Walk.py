def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        all_nswe = [True if walk.count('n') == walk.count('s') else False,
                    True if walk.count('w') == walk.count('e') else False]
        return all(all_nswe)
