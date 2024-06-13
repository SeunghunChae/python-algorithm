file=open('input3.txt','r')
n=4
m=5
graph=[]
while True:
    temp=file.readline().strip()
    if len(temp)==0:
        break
    graph.append([int(i) for i in temp])

#좌우상하
dx=[-1,1,0,0]
dy=[0,0,1,-1]


def dfs(x,y):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    '''
    print(f"x : {x}, y: {y}, graph: {graph[x][y]}")
    for i in range(len(graph)):
        print(graph[i])
    '''
    if graph[y][x]==0:
        graph[y][x]=1
        for i in range(4):
            dfs(y+dy[i],x+dx[i])
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(j,i)==True:
            result+=1

print(result)
