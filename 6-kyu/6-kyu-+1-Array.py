def up_array(arr):
    # check in array isn't empty
    if not arr:
        return None

    # check numbers in array
    for number in arr:
        if number < 0 or number > 9:
            return None

    temp_arr = [str(i) for i in arr]
    temp_arr = ''.join(temp_arr)
    temp_arr = int(temp_arr) + 1

    return [int(i) for i in str(temp_arr)]
