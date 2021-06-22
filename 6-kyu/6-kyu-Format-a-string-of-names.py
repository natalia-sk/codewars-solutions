def namelist(names):
    result = ''

    if not names:
        return result

    if len(names) == 1:
        result = names[0]['name']
    else:
        for i in range(len(names)):
            if names[i] == names[-1]:
                result += ' & ' + names[i]['name']
            elif names[i] == names[-2]:
                result += names[i]['name']
            else:
                result += names[i]['name'] + ', '

    return result
