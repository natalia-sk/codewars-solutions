def two_sum(numbers, target):
    checked_nums = {}
    for index, num in enumerate(numbers):
        if (target - num) in checked_nums:
            return (checked_nums[target - num], index)
        else:
            checked_nums[num] = index
