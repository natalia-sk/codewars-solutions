def find_nb(m):
    n = 0
    to_compare = 0
    for idx, i in enumerate(range(1, m)):
        to_compare += i ** 3
        if to_compare == m:
            n = idx + 1
            return n
        elif to_compare > m:
            return -1
        else:
            continue
