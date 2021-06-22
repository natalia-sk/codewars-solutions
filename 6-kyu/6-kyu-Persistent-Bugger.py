from functools import reduce


def persistence(n):
    result = 1
    nums = [int(i) for i in str(n)]

    if len(nums) == 1:
        return 0
    else:
        while len(str(reduce((lambda x, y: x * y), nums))) != 1:
            nums = [int(i) for i in str(reduce((lambda x, y: x * y), nums))]
            result += 1
        return result
