import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny)


t = int(input())

for _ in range(t):
    m,n,k = map(int, input().split())

    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        i,j = map(int, input().split())
        graph[i][j] = 1

    result = 0 
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                result += 1
    
    print(result)

