def DNA_strand(dna):
    list_dna = [i for i in dna]
    for i, item in enumerate(list_dna):
        if item == 'A':
            list_dna[i] = item.replace('A', 'T')
        elif item == 'T':
            list_dna[i] = item.replace('T', 'A')
        elif item == 'C':
            list_dna[i] = item.replace('C', 'G')
        else:
            list_dna[i] = item.replace('G', 'C')
    return ''.join(list_dna)
