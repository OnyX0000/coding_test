def solution(record):
    user_nick = {}
    actions = []

    for entry in record :
        parts = entry.split()
        command = parts[0]
        uid = parts[1]

        if command == "Enter" :
            nickname = parts[2]
            user_nick[uid] = nickname
            actions.append((uid, "들어왔습니다."))
        elif command == "Leave" :
            actions.append((uid, "나갔습니다."))
        elif command == "Change" :
            nickname = parts[2]
            user_nick[uid] = nickname

    result = [f"{user_nick[uid]}님이 {action}" for uid, action in actions]
    return result
