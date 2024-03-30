from collections import deque
adj_list = [
    [],
    [],
    [1, 3, 4],
    [],
    [3],
    [4, 7],
    [6],
    []
]

def topological_sort(adj_list):
    # 1. 모든 간선을 읽으면 indegree 테이블을 채움
    indegree_list = [len(i) for i in adj_list]
    queue = deque()
    for i in range(1, len(indegree_list)):
        # 2. indegree가 0인 정점들을 모두 큐에 넣음
        if indegree_list[i] == 0:
            queue.append(i)
    result = []
    # 5. 큐가 빌 때까지 3, 4번 반복
    while queue:
        # 3. 큐에서 정점을 꺼내 위상 정렬 결과에 추가
        node = queue.popleft()
        result.append(node)
        for next in adj_list[node]:
            # 4. 해당 정점으로부터 연결된 모든 정점의 indegree 값을 1 감소시킴
            indegree_list[next] -= 1
            # 이 때 indegree가 0이 되었다면 그 정점을 큐에 추가
            if indegree_list[i] == 0:
                queue.append(i)
        
        
    
    
 