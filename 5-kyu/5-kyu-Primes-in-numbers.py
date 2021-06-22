def prime_factors(n):
    i = 2
    factors = []

    # the prime factor decomposition of n
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n/i
        else:
            i += 1
            continue

    # creating a list of factors without repetition
    factors_no_repetition = list(set(factors))
    factors_no_repetition.sort()

    result = ""

    for factor in factors_no_repetition:
        if factors.count(factor) > 1:
            result += f"({factor}**{factors.count(factor)})"
        else:
            result += f"({factor})"

    return result
