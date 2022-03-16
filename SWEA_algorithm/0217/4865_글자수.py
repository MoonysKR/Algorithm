import sys

sys.stdin = open('4865_글자수_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 숫자만 세는 경우
    # 리스트 => 세트 => 리스트 중복된 값 제거 후 개수 세기

    str_tmp = []
    for st in str1:
        str_tmp += st
    str_list = list(set(str_tmp))

    # print(str_list)
    # ['P', 'V', 'Y', 'X']

    # 글자수 세기
    str_cnt = []
    for i in range(len(str_list)):
        cnt = 0
        for j in range(len(str2)):
            if str_list[i] == str2[j]:
                cnt += 1  # 글자수가 같으면 cnt증가
        str_cnt += [cnt]  # 리스트에 담기

    # 리스트에서 최대값 구하기
    str_max = str_cnt[0]
    for i in range(len(str_cnt)):
        if str_max < str_cnt[i]:
            str_max = str_cnt[i]

    # print(f'#{tc} {str_max}')




    # 글자도 알고 싶은 경우
    str_tmp = []
    for st in str1:
        str_tmp += st
    str_list = list(set(str_tmp))

    str_dict = {}
    str_cnt = []
    for i in range(len(str_list)):
        cnt = 0
        for j in range(len(str2)):
            if str_list[i] == str2[j]:
                cnt += 1
        str_dict[str_list[i]] = cnt
        str_cnt += [cnt]

    # print(str_dict)
    # {'Y': 2, 'V': 1, 'P': 1, 'X': 1}
    # {'T': 1, 'S': 1, 'J': 1}
    # {'I': 1, 'B': 1, 'Y': 1, 'D': 1, 'X': 2, 'S': 1, 'J': 1, 'Z': 3, 'T': 3, 'G': 2}

    str_max = str_cnt[0]
    for i in range(len(str_cnt)):
        if str_max < str_cnt[i]:
            str_max = str_cnt[i]  # 최대값 구하기

    alp_dict = str_dict.items()

    # print(alp_dict)
    # dict_items([('X', 1), ('Y', 2), ('P', 1), ('V', 1)])

    # 리스트 안의 튜플의 2번째 인자가 최대값이랑 일치하는 글자까지 호출
    for alp in alp_dict:
        if alp[1] == str_max:
            print(f'#{tc} {alp[0]} {alp[1]}')
            #1 Y 2
            #2 J 1
            #2 S 1
            #2 T 1
            #3 Z 3
            #3 T 3


