def dig_pow(n, p):
    nums = [int(i) for i in str(n)]
    nk = 0
    for i in nums:
        nk += i ** p
        p += 1
    k = nk / n
    return -1 if k % 1 else int(k)
