def solution(progresses, speeds):
    answer= []
    days = []

    for progress, speed in zip(progresses, speeds) :
        if (100 - progress) % speed == 0 :
            days.append((100 - progress) // speed)
        else :
            days.append((100 - progress) // speed + 1)

    i = 1
    while True :
        if len(days) > i and days[0] >= days[i] :
            i += 1
            # print(f'i : {i}')
        elif len(days) > i and days[0] < days[i] :
            answer.append(i)
            days = days[i:]
            i = 1
        else :
            answer.append(i)
            break

    return answer