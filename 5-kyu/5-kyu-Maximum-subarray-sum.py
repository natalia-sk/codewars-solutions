def max_sequence(arr):
    if not len(arr):
        return 0
    else:
        subarr_sums = []
        for i in range(len(arr)):
            for k in range(len(arr)):
                subarr_sums.append(sum(arr[i:k+1]))
        return max(subarr_sums)
