def lcs(X, Y):
    m = len(X)
    n = len(Y)

    table = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    # LCS 문자열 역추적
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:    # 같으면 추가
            lcs_str += X[i-1]
            i -= 1
            j -= 1
        elif table[i][j-1] > table[i-1][j]: # 들 증 큰 쪽으로 이동
            j -= 1
        else:
            i -= 1

    return lcs_str
