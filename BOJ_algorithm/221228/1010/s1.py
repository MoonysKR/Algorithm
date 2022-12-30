import sys

sys.stdin = open('input1.txt')

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    
    

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    # mCn == m! / (n! * (m - n)!) 

    # print(factorial(M), factorial(N), factorial(M-N))
    result = factorial(M) // (factorial(N) * factorial(M - N))

    print(result)

            

        
