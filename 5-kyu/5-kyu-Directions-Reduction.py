def dirReduc(arr):
    directions = {"NORTH": "SOUTH",
                  "SOUTH": "NORTH",
                  "EAST": "WEST",
                  "WEST": "EAST"}
    result = []

    for i in arr:
        if result and directions[i] == result[-1]:
            result.pop()
        else:
            result.append(i)

    return result
