def solution(prices):
    result = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            top = stack.pop()
            result[top] = i - top
        stack.append(i)

    for i in stack:
        result[i] = len(prices) - i - 1

    return result