# 점프왕쩰리 glacier 231125

# 재귀 함수 1000번 제한을 풀기위한 코드
import sys
sys.setrecursionlimit(10**7)

dx = (1, 0)
dy = (0, 1)


def dfs(y, x, amount):
    global visited
    visited[y][x] = True

    for i in range(2):
        ny = y + dy[i] * amount
        nx = x + dx[i] * amount

        if 0 <= nx < N and 0 <= ny < N:
            if board[ny][nx] == -1:
                return "HaruHaru"

            elif board[ny][nx] != -1 and not visited[ny][nx]:
                result = dfs(ny, nx, board[ny][nx])
                if result == "HaruHaru":
                    return "HaruHaru"

    return "Hing"



N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
print(dfs(0, 0, board[0][0]))
