from collections import deque

file=open('input3.txt','r')
n,m=map(int,file.readline().split())

graph=[]
while True:
    temp=file.readline().rstrip()
    if len(temp)==0:
        break
    graph.append([int(i) for i in temp])

dy=[1,-1,0,0]
dx=[0,0,1,-1]

q=deque([(0,0)])

while q:
    x, y=q.popleft()

    for i in graph:
        print(i)
    print()
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<=-1 or ny<=-1 or nx>=n or ny>=m:
            continue
        if graph[nx][ny]==0:
            continue
        if graph[nx][ny]==1:
            if nx==0 and ny==0:
                continue
            graph[nx][ny]=graph[x][y]+1
            q.append((nx,ny))
        
