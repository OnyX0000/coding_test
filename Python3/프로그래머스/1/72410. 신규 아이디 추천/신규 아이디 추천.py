def solution(new_id):
    # 1단계: 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 허용되지 않는 문자 제거
    new_id = ''.join(char for char in new_id if char.isalnum() or char in '-_.')

    # 3단계: 연속된 마침표를 하나로 치환
    while '..' in new_id :
        new_id = new_id.replace('..', '.')

    # 4단계: 마침표가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열이면 'a'를 대입
    if not new_id :
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 첫 15자를 제외한 나머지 제거, 끝 마침표 제거
    if len(new_id) >= 16 :
        new_id = new_id[:15].rstrip('.')

    # 7단계: 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자 반복
    while len(new_id) < 3 :
        new_id += new_id[-1]

    return new_id
