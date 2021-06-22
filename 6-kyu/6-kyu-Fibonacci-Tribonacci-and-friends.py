def Xbonacci(signature, n):
    m = len(signature)
    if n < m:
        return signature[:n]
    else:
        for i in range(n-m):
            signature.append(sum(signature[i:i+m+1]))
        return signature
