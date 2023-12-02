from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()

    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        num, order = q.popleft()

        if order == len(numbers) - 1:
            if target == num:
                answer += 1
            continue

        q.append((num + numbers[order + 1], order + 1))
        q.append((num - numbers[order + 1], order + 1))

    return answer