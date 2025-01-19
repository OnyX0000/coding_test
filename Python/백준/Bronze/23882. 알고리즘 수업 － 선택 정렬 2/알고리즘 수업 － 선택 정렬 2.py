def selection_sort_kth_swap(N, K, A):
    swap_count = 0  # 교환 횟수 추적

    for last in range(N - 1, 0, -1):
        # A[0..last]에서 가장 큰 원소의 인덱스를 찾음
        max_idx = last
        for i in range(last):
            if A[i] > A[max_idx]:
                max_idx = i

        # 가장 큰 원소가 마지막 위치에 있지 않으면 교환
        if max_idx != last:
            A[max_idx], A[last] = A[last], A[max_idx]
            swap_count += 1  # 교환 횟수 증가

        # K번째 교환 직후의 배열 출력
        if swap_count == K:
            return A

    # 교환 횟수가 K보다 적으면 -1 출력
    return -1


# 입력 처리
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
result = selection_sort_kth_swap(N, K, A)
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))