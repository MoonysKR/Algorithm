import sys

sys.stdin = open('연습문제2_정수를문자열로반환_input.txt')

def itoa(n):
    # 10으로 나눈 나머지 문자열로 변환, 몫을 저장할 초기값 설정
    # 아스키 코드의 문자열 참고해 나머지에서 48을 더해줌
    # 양수일 경우 그대로 진행
    # 0은 0출력
    # 음수일 경우 양수 화 이후 마지막 리턴값에 하이픈 문자 추가
    num_str = ''
    if n > 0:
        while n != 0:
            num_str += chr((n%10)+48)
            n = n // 10
        return num_str
    elif n == 0:
        num_str = chr(n+48)
    else:
        n = -1 * n
        while n != 0:
            num_str += chr((n%10)+48)
            n = n // 10
        return '-' + num_str

for tc in range(1, 7):
    num = int(input())

    print(f'#{tc} {itoa(num)} {type(itoa(num))}')

