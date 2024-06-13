from collections import deque

file=open('input4.txt','r')
n, m, k, start = map(int,file.readline().split())
distance=[-1]*(n+1)
distance[start]=0

graph=[[] for i in range(n+1)]
while True:
    temp = file.readline()
    if len(temp)==0:
        break
    t=list(map(int,temp.split()))
    graph[t[0]].append(t[1])
file.close()
    
q=deque([start])
while q:
    node=q.popleft()
    for i in graph[node]:
        if distance[i]==-1:
            distance[i]=distance[node]+1
            q.append(i)
