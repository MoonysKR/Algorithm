import sys

sys.stdin = open('4864_문자열비교_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()  # 찾는 문자열
    str2 = input()  # 주어진 문자열

    cnt = 0
    for i in range(len(str2)-len(str1)):  # 끝부분 맞추어준 range 잡아주고
        result = ''  # 빈 문자열로 같다면 추가, 한 번 돌면 초기화
        for j in range(len(str1)):  # 찾는 문자열의 길이만큼 for문 돌아주고
            if str2[i+j] == str1[j]:
                result += str1[j]  # 같다면 빈 문자열에 추가
        if result == str1:
            cnt += 1  # 한번 돌았을 때 문자열이 일치한다면 1회 추가

    if cnt == 0:  # 같은것이 없다면 0 출력
        print(f'#{tc} {cnt}')
    else:  # 같은 문자열에 1이상이라면 1출력
        print(f'#{tc} 1')

