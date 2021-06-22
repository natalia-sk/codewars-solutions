import string


def is_pangram(s):
    abc = [i for i in string.ascii_lowercase]
    result = [i in s.lower() for i in abc]

    return all(result)
