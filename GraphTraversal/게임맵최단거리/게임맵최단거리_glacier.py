from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(x, y, visited, maps):
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        y, x, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                if nx == N - 1 and ny == M - 1:
                    return dist + 1

                if maps[ny][nx] == 0:
                    continue

                queue.append((ny, nx, dist + 1))
                visited[ny][nx] = True

    return -1


def solution(maps):
    global N, M

    N = len(maps[0])
    M = len(maps)

    visited = [[False] * N for i in range(M)]
    answer = bfs(0, 0, visited, maps)

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
