def array_diff(a, b):
    if not a or not b:
        return a

    for i in b:
        while i in a:
            a.remove(i)
    return a


# 2nd solution:
# def array_diff(a, b):
#     for n in b:
#         a = [m for m in a if m != n]
#     return a
