def sort_array(source_array):
    odd_idx = []
    odd_num = []

    for idx, num in enumerate(source_array):
        if num % 2 != 0:
            odd_idx.append(idx)
            odd_num.append(num)

    odd_num.sort()

    for idx, num in enumerate(odd_num):
        source_array[odd_idx[idx]] = num

    return source_array
