from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리의 상태를 큐로 표현
    total_weight = 0  # 현재 다리 위 트럭들의 무게 합
    truck_weights = deque(truck_weights)  # 대기 트럭 큐

    while bridge:
        time += 1
        out_truck = bridge.popleft()  # 다리를 지난 트럭
        total_weight -= out_truck

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 트럭을 올리지 못하면 빈 공간 추가

    return time
