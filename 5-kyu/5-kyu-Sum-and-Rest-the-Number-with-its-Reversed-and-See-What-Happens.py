def make_checks_dict(x):
    checks = []

    while len(checks) < 66:
        if x not in checks:
            if str(x)[-1] != '0':
                y = int(str(x)[::-1])
                dif = abs(x - y)
                if dif:
                    add = x + y
                    if not add % dif:
                        checks.append(x)
                        checks.append(y)
        x += 1

    checks.sort()
    checks_dict = {}

    for k, v in enumerate(checks, start=1):
        checks_dict[k] = v

    return checks_dict


CHECKS = make_checks_dict(45)


def sum_dif_rev(n):
    return CHECKS[n]
