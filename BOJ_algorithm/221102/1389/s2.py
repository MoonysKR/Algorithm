import sys
from collections import deque
# 큐랑 스택 그리고 덱
# 큐가 선입 선출, 스택이 후입선출
# deque(덱)은 둘 다 가능
# popleft 메서드는 선입선출 pop 메서드는 후입선출

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = []
    for i in range(1, n+1):
        result.append(bfs(graph, i))

    print(result.index(min(result))+1)
    # index(value) 메서드는 value 가 가장 먼저 나오는 인덱스 값.