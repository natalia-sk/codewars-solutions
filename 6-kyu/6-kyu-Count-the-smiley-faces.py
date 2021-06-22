def count_smileys(arr):
    smiles = {':)': ':)',
              ';)': ';)',
              ':D': ':D',
              ';D': ';D',
              ':-)': ':-)',
              ';-)': ';-)',
              ':~)': ':~)',
              ';~)': ';~)',
              ':-D': ':-D',
              ';-D': ';-D',
              ':~D': ':~D',
              ';~D': ';~D'
              }
    result = 0
    for i in arr:
        if i in smiles:
            result += 1
    return result
