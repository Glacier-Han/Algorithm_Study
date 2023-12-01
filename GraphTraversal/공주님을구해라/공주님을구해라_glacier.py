# 공주님을구해라 glacier 231201
from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(x, y):
    queue = deque()
    queue.append((0, 0, 0, False))
    visited[0][0] = True

    while queue:
        y, x, dist, isGroam = queue.popleft()

        if board[y][x] == 2:
            isGroam = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    if not isGroam:
                        visited[ny][nx] = True
                        continue

                if nx == M - 1 and ny == N - 1:
                    return dist + 1

                queue.append((ny, nx, dist + 1, isGroam))
                visited[ny][nx] = True


N, M, T = map(int, input().strip().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

res = bfs(0, 0)
if res and res <= T:
    print(res)
else:
    print("Fail")
