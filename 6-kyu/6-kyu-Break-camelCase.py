def solution(s):
    import re
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)
