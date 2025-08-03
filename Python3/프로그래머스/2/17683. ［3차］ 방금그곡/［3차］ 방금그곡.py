def solution(m, musicinfos):
    # 1) 샾 음 정규화 매핑
    SHARP_MAP = {
        "C#": "c", "D#": "d", "F#": "f",
        "G#": "g", "A#": "a", "E#": "e", "B#": "b"  # E#, B#는 일반적으로 잘 안 쓰이지만 안전하게 포함
    }

    def normalize(score: str) -> str :
        # 긴 패턴부터 치환되도록 2글자 샾 음을 먼저 처리
        i, out = 0, []
        while i < len(score) :
            if i + 1 < len(score) and score[i:i+2] in SHARP_MAP :
                out.append(SHARP_MAP[score[i:i+2]])
                i += 2
            else :
                out.append(score[i])
                i += 1
        return "".join(out)

    def time_to_min(t: str) -> int :
        h, s = map(int, t.split(":"))
        return h * 60 + s

    def build_played(sheet_norm: str, duration: int) -> str :
        if duration <= 0 :
            return ""
        L = len(sheet_norm)
        if L == 0 :
            return ""
        if duration <= L :
            return sheet_norm[:duration]
        # 반복 구성: 몫*전체 + 나머지 부분
        q, r = divmod(duration, L)
        return sheet_norm * q + sheet_norm[:r]

    target = normalize(m)
    best_title = "(None)"
    best_duration = -1  # 비교 기준

    for idx, info in enumerate(musicinfos) :
        start, end, title, sheet = info.split(",")
        duration = time_to_min(end) - time_to_min(start)

        sheet_norm = normalize(sheet)
        played = build_played(sheet_norm, duration)

        if target and target in played :
            # 재생 시간 긴 곡 우선, 같으면 입력 먼저
            if duration > best_duration :
                best_duration = duration
                best_title = title
            # duration 같으면 기존(best)이 더 먼저 들어온 것이므로 갱신하지 않음

    return best_title
