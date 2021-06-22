def get_count(input_str):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for i in input_str:
        if i in VOWELS:
            num_vowels += 1
    return num_vowels
