def bubblesort_once(arr):
    n = len(arr)
    result = arr.copy()
    for i in range(n - 1):
        if result[i] > result[i + 1]:
            result[i], result[i + 1] = result[i + 1], result[i]
    return result
