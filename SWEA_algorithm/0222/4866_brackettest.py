import sys

sys.stdin = open('4866_brackettest_input.txt')

T = int(input())

for tc in range(1, T + 1):
    chars = input()

    # 문자열을 제외한 괄호 만 담을 빈 문자열
    brackets = ''

    for char in chars:
        if char == '(' or char == '{' or char == '[':
            brackets += char
        if char == ')' or char == '}' or char == ']':
            brackets +=char

    # print(brackets)
    # ({}{}())
    # (()())
    # ({}{}(())
    # {(})

    # 무조건 괄호가 짝이 맞는 순간이 나옴
    # 순회를 통해 삭제 후 재 순회 방식
    i = 0  # 순회할 인덱스의 위치
    while len(brackets) > 1 and i < len(brackets):  # 남은 괄호는 2개 이상일 때 유의미, i를 순회 해야하는데 괄호 길이보다 길어지면 무의미(오류발생)
        if brackets[i] == '(' and brackets[i+1] == ')':  # 연속으로 나온다면
            brackets = brackets[:i] + brackets[i+2:]  # 슬라이싱 후 연결
            i = 0  # 처음부터 재순회
        elif brackets[i] == '{' and brackets[i+1] == '}':
            brackets = brackets[:i] + brackets[i+2:]
            i = 0
        elif brackets[i] == '[' and brackets[i+1] == ']':
            brackets = brackets[:i] + brackets[i+2:]
            i = 0
        else:
            i += 1

    # print(f'#{tc} {brackets}')
    # 1
    # 2
    # 3 (
    # 4 {(})

    if len(brackets) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
