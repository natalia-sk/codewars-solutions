def increment_string(strng):
    import re
    end_digits = re.search('[0-9]+$', strng)

    if end_digits is None:
        print(strng)
        print(strng + '1')
        return strng + '1'
    else:
        end_digits = end_digits.group()
        number = int(end_digits) + 1
        strng += 'X!@#%^BGFDECXZ'
        print(strng)
        final_str = strng.replace(end_digits + 'X!@#%^BGFDECXZ',
                                  str(number).zfill(len(end_digits)))
        return final_str
