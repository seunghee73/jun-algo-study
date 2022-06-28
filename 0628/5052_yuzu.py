def search(graph):
    global ans
    graph = dict(sorted(graph.items()))
    if not graph:
        ans -= 1
        return
    for child in graph:
        search(graph[child])

t = int(input())
for _ in range(t):
    n = int(input())
    graph = {}
    for _ in range(n):
        nodes = list(input())
        cur = graph
        for node in nodes:
            if node not in cur:
                cur[node] = {}
            cur = cur[node]

    ans = n
    search(graph)
    print('YES') if ans == 0 else print('NO')