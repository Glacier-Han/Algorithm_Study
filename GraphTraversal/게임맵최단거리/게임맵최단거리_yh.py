from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(maps, n, m):
    que = deque()
    que.append((0,0))
    while que:
        x,y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
                
            if nx == (m-1) and ny == (n-1):
                return maps[nx][ny] + maps[x][y]
            
            if maps[nx][ny] == 1 and not (nx == 0 and ny == 0):
                maps[nx][ny] += maps[x][y]
                que.append((nx,ny))
            
    return -1

def solution(maps):
    answer = bfs(maps, len(maps[0]), len(maps))
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# bfs 사용