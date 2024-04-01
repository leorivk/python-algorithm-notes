'''
11404 플로이드
11780 플로이드 2
'''

n = 5   # 정점 수
m = 14   # 이동 경우의 수

INF = float("inf")
table = [[INF] * n for _ in range(n)]
nxt = [[0] * n for _ in range(n)]

for i in range(n):
    table[i][i] = 0

# 다른 정점을 거치지 않았을 때의 거리
for _ in range(m):
    start, end, cost = map(int, input().split())
    # 두 정점을 연결하는 노선이 여러 개일 경우
    if table[start-1][end-1] > cost:
        table[start-1][end-1] = cost
        nxt[start-1][end-1] = end-1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]
                nxt[i][j] = nxt[i][k]


