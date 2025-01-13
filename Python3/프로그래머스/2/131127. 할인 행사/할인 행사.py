def solution(want, number, discount):
    required_items = {item: qty for item, qty in zip(want, number)}
    
    num_days = 0
    n = len(discount)
    window_size = sum(number)

    current_window = {}
    for item in discount[:window_size]:
        if item in current_window:
            current_window[item] += 1
        else:
            current_window[item] = 1

    if all(current_window.get(item, 0) >= required_items[item] for item in required_items):
        num_days += 1

    for i in range(window_size, n):
        outgoing_item = discount[i - window_size]
        current_window[outgoing_item] -= 1
        if current_window[outgoing_item] == 0:
            del current_window[outgoing_item]

        incoming_item = discount[i]
        if incoming_item in current_window:
            current_window[incoming_item] += 1
        else:
            current_window[incoming_item] = 1
            
        if all(current_window.get(item, 0) >= required_items[item] for item in required_items):
            num_days += 1

    return num_days