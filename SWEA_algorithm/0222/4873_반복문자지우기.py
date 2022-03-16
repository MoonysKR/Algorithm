import sys

sys.stdin = open('4873_반복문자지우기_input.txt')

T = int(input())

for tc in range(1, T+1):
    chars = input()

    # 결과를 담아줄 리스트 생성
    result = []

    # 주어진 문자열의 문자 하나 씩 호출해서 비교
    for i in range(0, len(chars)):
        if result == []:  # 빈 리스트면 추가
            result += chars[i]
        elif result[-1] == chars[i]:  # 맨 마지막 문자와 같다면 결과 값 슬라이싱
            result = result[:-1]
        else:
            result += [chars[i]]  # 맨 마지막 문자와 다르다면 추가

    print(f'{tc} {result}')