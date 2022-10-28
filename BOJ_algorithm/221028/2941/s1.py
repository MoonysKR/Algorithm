# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s= 
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

S = input()

result = 0

while len(S) != 0:

    if len(S) == 1:
        result += 1
        break

    if S[0] not in ('c', 'd', 'l', 'n', 's', 'z'):
        result += 1
        S=S[1:]

    if S[0] == 'c':
        if S[1] == '=' | S[1] == '-':
            result += 1
            S=S[2:]
    elif S[0] == 'l':
        if  S[1] == 'j':
            result += 1
            S=S[2:]
    elif S[0] == 'n':
        if S[1] == 'j':
            result += 1
            S=S[2:]
    elif S[0] == 's':
        if S[1] == '=':
            result += 1
            S=S[2:]
    elif S[0] == 'd':
        if S[1] == '-':
            result += 1
            S=S[2:]
        elif len(S) > 2:
            if S[1:2] == 'z=':
                result += 1
                S=S[3:]
    elif S[0] == 'z':
        if S[1] == '=':
            result += 1
            S=S[2:]

print(result)