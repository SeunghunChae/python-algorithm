import heapq

INF=int(1e9)

file=open('input.txt','r')
n,m = map(int, file.readline().split())
start=int(file.readline().strip())
dist=[INF]*(n+1)
visited=[False]*(n+1)

graph=[[] for i in range(n+1)]
while True:
    temp=file.readline()
    if len(temp)==0:
        break
    a,b,c=map(int, temp.split())
    graph[a].append((b,c)) 
file.close()

q=[]
heapq.heappush(q,(0,start))
dist[start]=0
while q:
    d, now=heapq.heappop(q)
    if dist[now] < d:
        continue
    for i in graph[now]:
        cost=d+i[1]
        if cost < dist[i[0]]:
            dist[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

