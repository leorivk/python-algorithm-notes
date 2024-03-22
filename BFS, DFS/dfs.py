graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

def dfs_recursive(graph, current, visited):
    visited[current] = True
    for i in graph[current]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)

def dfs_stack(graph, current, visited):
    stack = []
    stack.append(current)
    visited[current] = True

    while stack:
        current = stack.pop()
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

    
