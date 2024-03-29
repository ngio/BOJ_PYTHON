""" https://www.acmicpc.net/problem/1016
    [백준] 2016번 제곱ㄴㄴ수 - PYTHON
    문제
    어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 
    제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

    입력
    첫째 줄에 두 정수 min과 max가 주어진다.

    출력
    첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

    제한
    1 ≤ min ≤ 1,000,000,000,000
    min ≤ max ≤ min + 1,000,000
    
    예제 입력 1 
    1 10
    예제 출력 1 
    7
    예제 입력 2 
    15 15
    예제 출력 2 
    1
    예제 입력 3 
    1 1000
    예제 출력 3 
    608
"""

import math

min, max = map(int, input().split())
 
NN = [1] * (max - min + 1) 

tmp_01 = []

for i in range(2, int(math.sqrt(max)) + 1):
    tmp_01.append(i ** 2)


for i in tmp_01:
    j = math.ceil(min / i)
    while i * j <= max:
        NN[i * j - min] = 0
        j += 1

print(sum(NN))
