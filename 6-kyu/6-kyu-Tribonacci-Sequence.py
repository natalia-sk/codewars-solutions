def tribonacci(signature, n):
    if n < len(signature):
        return signature[:n]
    else:
        for i in range(n-3):
            signature.append(sum(signature[i:i+3]))
        return signature
