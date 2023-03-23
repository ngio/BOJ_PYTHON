""" [백준] 1017번 소수 쌍 
    https://www.acmicpc.net/problem/1017
    
    문제
        지민이는 수의 리스트가 있을 때, 이를 짝지어 각 쌍의 합이 소수가 되게 하려고 한다. 
        예를 들어, {1, 4, 7, 10, 11, 12}가 있다고 하자. 지민이는 다음과 같이 짝지을 수 있다.
        1 + 4 = 5, 7 + 10 = 17, 11 + 12 = 23
        또는
        1 + 10 = 11, 4 + 7 = 11, 11 + 12 = 23
        수의 리스트가 주어졌을 때, 지민이가 모든 수를 다 짝지었을 때, 첫 번째 수와 어떤 수를 짝지었는지 오름차순으로 출력하는 프로그램을 작성하시오. 위의 예제에서 1 + 12 = 13으로 소수이다. 그러나, 남은 4개의 수를 합이 소수가 되게 짝지을 수 있는 방법이 없다. 따라서 위의 경우 정답은 4, 10이다.

    입력
        첫째 줄에 리스트의 크기 N이 주어진다. N은 50보다 작거나 같은 자연수이며, 짝수이다. 둘째 줄에 리스트에 들어있는 수가 주어진다. 리스트에 들어있는 수는 1,000보다 작거나 같은 자연수이며, 중복되지 않는다.

    출력
        첫째 줄에 정답을 출력한다. 없으면 -1을 출력한다.

    예제 입력 1 
    6
    1 4 7 10 11 12
    예제 출력 1 
    4 10
    예제 입력 2 
    6
    11 1 4 7 10 12
    예제 출력 2 
    12
    예제 입력 3 
    4
    8 9 1 14
    예제 출력 3 
    -1
    예제 입력 4 
    8
    34 39 32 4 9 35 14 17
    예제 출력 4 
    9 39
    예제 입력 5 
    20
    941 902 873 841 948 851 945 854 815 898 806 826 976 878 861 919 926 901 875 864
    예제 출력 5 
    806 926
"""

import sys
import math

def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if x + y in primes:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
# X.sort()

# 소수 목록을 미리 준비
primes = []
for i in range(2, 2000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime: primes.append(i)
    else: continue

answers = []
for i in X:
    matched = {}
    if i == X[0]: continue
    if X[0] + i in primes:
        if N == 2:
            answers.append(i)
            break
        # print(i)
        # 첫번째 숫자와 현재 매치된 숫자를 제외한 새 리스트 생성
        Y = [x for x in X]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)
    
    # if matched: print(matched)
    if N != 2 and len(matched) == N - 2: answers.append(i)

if not answers:
    answers.append(-1)

answers.sort()

print(' '.join(list(map(str, answers))))

# 출처 : https://nerogarret.tistory.com/34
