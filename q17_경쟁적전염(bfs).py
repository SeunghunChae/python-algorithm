from collections import deque

file=open('input6.txt','r')
n,k=map(int,file.readline().split())
graph=[]
virus=[]
for i in range(n):
    graph.append(list(map(int,file.readline().split())))
target,tx,ty=map(int,file.readline().split())
file.close()

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],0,i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus.sort()
q=deque(virus)
print(virus)
count=0
while q:
    print(q)
    v,t,x,y=q.popleft()
    if t==target:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<=-1 or ny<=-1 or nx>=n or ny>=n:
            print(f"nx : {nx}, ny : {ny}")
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=v
            q.append((graph[nx][ny],t+1,nx,ny))
