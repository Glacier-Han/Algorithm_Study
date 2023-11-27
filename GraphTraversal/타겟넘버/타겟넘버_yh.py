from collections import deque

def bfs(numbers, target):
    que = deque()
    que.append((numbers[0],0))
    que.append((numbers[0] * (-1), 0))

    while que:
        num,idx = que.popleft()
        if idx == len(numbers) - 1:
            break
        que.append((num + numbers[idx+1], idx+1))
        que.append((num - numbers[idx+1], idx+1))
    
    return sum(1 for num, idx in que if num == target)


def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    
    answer += dfs(numbers, target, depth+1)
    numbers[depth] *= -1
    answer += dfs(numbers, target, depth+1)
    return answer

def solution(numbers, target):
    # answer = dfs(numbers,target,0)
    answer = bfs(numbers,target)
    return answer


print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2