def solution(players, callings):
    # 선수들의 현재 순위를 저장할 딕셔너리 생성
    player_indices = {player : idx for idx, player in enumerate(players)}

    for calling in callings :
        # 현재 호출된 선수의 등수와 바로 앞 선수의 등수를 가져옴
        current_index = player_indices[calling]
        
        if current_index == 0 :
            continue  # 1등인 경우 추월할 수 없으므로 건너뜀

        # 앞 선수의 이름 가져오기
        previous_player = players[current_index - 1]

        # 선수들 리스트에서 위치 교환
        players[current_index - 1], players[current_index] = players[current_index], players[current_index - 1]

        # 딕셔너리에서 인덱스 업데이트
        player_indices[calling] -= 1
        player_indices[previous_player] += 1

    return players