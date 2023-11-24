# 유기농배추 glacier 231124

# 재귀 함수 1000번 제한을 풀기위한 코드
import sys
sys.setrecursionlimit(10**7)

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def dfs(y, x):
    global visited
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로길이 M, 세로길이 N, 배추 위치 개수 K
    cabbage_locations = [list(map(int, input().split())) for _ in range(K)]

    board = [[0] * M for _ in range(N)]
    for cabbage in cabbage_locations:
        board[cabbage[1]][cabbage[0]] = 1

    visited = [[False] * M for _ in range(N)]

    answer = 0
    # 모든 board상의 점들을 방문했던 점 제외하고 dfs로 탐색
    # dfs가 종료되면 인접한 점이 없는 상황임으로 ans += 1 해줌
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)
