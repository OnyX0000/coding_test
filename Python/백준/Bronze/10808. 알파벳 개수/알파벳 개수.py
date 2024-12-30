# 입력 받기
strs = input()

# 알파벳 소문자 개수를 저장할 리스트 초기화
alphabet_count = [0] * 26

# 문자열 strs를 순회하면서 알파벳 개수 증가
for char in strs:
    alphabet_count[ord(char) - ord('a')] += 1

# 결과 출력
print(' '.join(map(str, alphabet_count)))