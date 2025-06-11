from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)

    while queue:
        current, steps = queue.popleft()

        if current == y:
            return steps

        for next_val in (current + n, current * 2, current * 3):
            if next_val <= y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, steps + 1))

    return -1