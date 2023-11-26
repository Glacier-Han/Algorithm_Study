import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m,t = map(int, input().rstrip().split())
graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(i,j):
    distance_gram = -1
    que = deque()
    que.append((i,j,0))
    visited[i][i] = True

    while que:
        x,y,distance = que.popleft()

        if graph[x][y] == 2:
            distance_gram = hasGram(x,y,distance)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if not visited[nx][ny] and graph[nx][ny] != 1:
                que.append((nx,ny,distance+1))
                visited[nx][ny] = True

            if nx == (n-1) and ny == (m-1):
                if distance_gram != -1 :
                    return min(distance + 1, distance_gram)
                else:
                    return distance + 1
    
    return max(-1, distance_gram)


def hasGram(i,j,dist):
    x_dist = (n-1) - i
    y_dist = (m-1) - j
    return x_dist + y_dist + dist
            

result = bfs(0,0)
if result == -1 or result > t:
    print("Fail")
else:
    print(result)




# 최단 거리 구하기 - bfs 사용 
# 그람의 유무에 따라 다르게 계산 후 비교 

