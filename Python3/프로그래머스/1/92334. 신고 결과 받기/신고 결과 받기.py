def solution(id_list, report, k):
    # 각 유저가 신고한 유저와 신고당한 횟수 기록
    received = {user : set() for user in id_list}
    mail_count = {user : 0 for user in id_list}

    # 신고 내용 처리
    for r in report :
        reporter, reported = r.split()
        received[reported].add(reporter)

    # 정지된 유저 확인 및 메일 발송
    for reported, reporters in received.items() :
        if len(reporters) >= k :  # 신고 횟수가 기준 이상인 유저
            for reporter in reporters :
                mail_count[reporter] += 1

    # 결과를 id_list 순서대로 반환
    return [mail_count[user] for user in id_list]