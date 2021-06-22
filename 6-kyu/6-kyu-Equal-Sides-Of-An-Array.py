def find_even_index(arr):
    left = 0
    right = 0
    N = 0

    while N < len(arr):
        left = sum(arr[:N])
        right = sum(arr[N+1:])
        if left == right:
            return N
            break
        else:
            N += 1

    return -1
