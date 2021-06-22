code = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5',
        '1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}


def encode(st):
    for i in st:
        if i in code:
            st = st.replace(i, code[i])
    return st


def decode(st):
    return encode(st)
