def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time) :
        m, s = map(int, time.split(':'))
        return m * 60 + s

    def to_mmss(seconds) :
        return f'{seconds // 60:02}:{seconds % 60:02}'

    video_length = to_seconds(video_len)
    position = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    for command in commands :
        if op_start <= position <= op_end :  # 오프닝 구간이면 건너뛰기 먼저 실행
            position = op_end
        if command == 'prev' :
            position = max(0, position - 10)
        elif command == 'next' :
            position = min(video_length, position + 10)
        if op_start <= position <= op_end :  # 명령 처리 후에도 오프닝 구간 체크
            position = op_end

    return to_mmss(position)