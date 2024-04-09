import heapq

'''
adj 리스트는 (노드, 거리) 쌍을 갖는 리스트의 리스트로 구성
'''

INF = float('inf')
# n : 정점 수
def dijkstra_naive(start, adj, n):
    global INF
    table = [INF] * n
    fixed = [False] * n
    
    table[start] = 0
    for end, cost in adj[start]:
        table[end] = cost
    
    while True:
        min_distance = INF
        idx = -1
        for i in range(n):
            if not fixed[i] and table[i] < min_distance:
                min_distance = table[i]
                idx = i    
                    
        if idx == -1:
            break

        fixed[idx] = True
        
        for end, cost in adj[idx]:
            if not fixed[end] and table[end] > table[idx] + cost:
                table[end] = table[idx] + cost
    
    return table


def dijkstra(start, adj, n):
    global INF
    pq = []
    heapq.heappush(pq, (0, start))
    table = [INF] * n
    table[start] = 0
     
    while pq:
        dis, v = heapq.heappop(pq)
        if table[v] != dis: # >도 됨
            continue
        
        for i, j in adj[v]:
            if table[i] > dis + j:
                table[i] = dis + j
                heapq.heappush(pq, (table[i], [i]))
    
    return table

'''
if table[v] != dis: 
위 조건문은 이미 더 짧은 경로를 통해 처리된 노드를 다시 처리하지 않기 위해 사용됩니다. 
이는 다익스트라 알고리즘에서의 최적화 기법 중 하나입니다.
다익스트라 알고리즘에서는 우선순위 큐(여기서는 최소 힙)를 사용하여
현재까지 발견된 가장 짧은 경로의 다음 노드를 선택합니다.
하지만, 한 노드를 대상으로 여러 경로가 힙에 추가될 수 있고,
이중 가장 짧은 경로가 먼저 처리됩니다.
그런 후, 더 긴 경로들도 힙에서 추출되지만, 
이미 더 짧은 경로로 처리되었기 때문에 더 이상 처리할 필요가 없습니다.
즉, 이 조건문은 힙에서 노드를 꺼낼 때,
그 노드에 도달하는 더 짧은 경로가 이미 발견되었는지를 확인합니다.
만약 table[v] (노드 v까지의 현재까지 발견된 최단 경로)가 
dis (힙에서 꺼낸 현재 노드까지의 경로 길이)와 다르다면,
이는 더 짧은 경로가 이미 존재한다는 의미이므로,
현재 꺼낸 경로는 무시하고 다음 경로를 처리합니다.
이러한 최적화는 알고리즘의 효율성을 높이는 데 도움이 되며, 불필요한 계산을 줄입니다.
'''
     
