import heapq

INF=int(1e9)
file=open('input.txt','r')
e,v=map(int,file.readline().split())
start=int(file.readline())

graph=[[] for i in range(e+1)]
distance=[INF]*(e+1)

while True:
    temp=file.readline()
    if len(temp)==0:
        break
    a,b,c=map(int,temp.split())
    graph[a].append((b,c))

file.close()

q=[]
distance[start]=0
heapq.heappush(q,(0,start))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost=i[1]+dist
        if cost<distance[i[0]]:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
