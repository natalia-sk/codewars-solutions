def cakes(recipe, available):
    result = []
    for i in recipe:
        if i in available:
            result.append(available[i]//recipe[i])
        else:
            return 0
    return min(result)
