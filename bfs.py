from collections import deque

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

n=8
q=deque([1])
visited=[False]*(n+1)

while q:
    v=q.popleft()
    print(v)
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i]=True
