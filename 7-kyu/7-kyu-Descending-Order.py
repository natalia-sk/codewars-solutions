def descending_order(num):
    result = sorted(str(num), reverse=True)
    result = int(''.join(result))
    return result


# 2nd solution:
# def descending_order(num):
#     result = [i for i in str(num)]
#     result.sort(reverse=True)
#     result = int(''.join(result))
#     return result
