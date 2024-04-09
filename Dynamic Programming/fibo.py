def df_fibo(n):
    if n <= 1:
        return n

    fibo_table = [0 for i in range(n+1)]

    fibo_table[0] = 0
    fibo_table[1] = 1

    for i in range(2, n+1):
        fibo_table[i] = fibo_table[i-1] + fibo_table[i-2]

    result = fibo_table[n]

    return result

