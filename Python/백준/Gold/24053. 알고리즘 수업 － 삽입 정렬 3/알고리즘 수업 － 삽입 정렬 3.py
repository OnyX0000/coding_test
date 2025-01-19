def insert_sort(n, a, b) :
    # 초기 상태 비교
    if a == b :
        print(1)
        return

    # 삽입 정렬 수행
    for i in range(1, n) :
        loc = i - 1
        tmp = a[i]

        while loc >= 0 and a[loc] > tmp :
            a[loc + 1] = a[loc]
            loc -= 1
            # 배열 상태 비교
            if a == b :
                print(1)
                return

        if loc + 1 != i :
            a[loc + 1] = tmp
            # 배열 상태 비교
            if a == b :
                print(1)
                return

    # 정렬 과정 중 배열 B와 동일한 상태가 없을 경우
    print(0)

# 입력 
n = int(input())  # 배열 크기 입력
a = list(map(int, input().split()))  # 배열 A 입력
b = list(map(int, input().split()))  # 배열 B 입력

# 결과
insert_sort(n, a, b)