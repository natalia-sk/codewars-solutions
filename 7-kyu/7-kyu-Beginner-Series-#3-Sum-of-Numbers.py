def get_sum(a, b):
    if a == b:
        return a
    return sum(range(a, b+1)) if a < b else sum(range(b, a+1))
