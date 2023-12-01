import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0]
dy = [0,1]

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]

for _ in range (n):
    graph.append(list(map(int, input().split())))

def bfs(i,j):
    que = deque()
    que.append((i,j))
    visited[i][j] = True

    while que:
        x,y = que.popleft()
        step = graph[x][y]

        if step == 0 or step > n:
            continue

        for d in range(2):
            nx = x + (step * dx[d])
            ny = y + (step * dy[d])

            if nx < n and ny < n and not visited[nx][ny]:
                if graph[nx][ny] == -1:
                    return True
                
                que.append((nx,ny))
                visited[nx][ny] = True 
            
    return False

if bfs(0,0):
    print("HaruHaru")
else:
    print("Hing")



# 시간 초과 
    # visited 배열 부재

# 메모리 초과 
    # visited[nx][ny] = True 위치 설정 (line 36)