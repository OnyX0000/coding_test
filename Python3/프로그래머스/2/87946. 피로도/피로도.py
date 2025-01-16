def solution(k, dungeons):
    def generate_permutations(arr, depth, n, result, current):
        if depth == n:
            result.append(current[:])
            return
        for i in range(len(arr)):
            generate_permutations(arr[:i] + arr[i+1:], depth + 1, n, result, current + [arr[i]])

    max_explored = 0
    n = len(dungeons)
    permutations = []

    # 순열 생성
    generate_permutations(dungeons, 0, n, permutations, [])

    # 생성된 순열로 탐험 시뮬레이션
    for order in permutations:
        current_fatigue = k
        explored_count = 0

        for required, consume in order:
            if current_fatigue >= required:
                current_fatigue -= consume
                explored_count += 1
            else:
                break

        # 최대 탐험 가능한 던전 수 갱신
        max_explored = max(max_explored, explored_count)

    return max_explored