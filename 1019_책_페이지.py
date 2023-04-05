

""" [백준] 1019번 책 페이지 - PYTHON
    https://www.acmicpc.net/problem/1019
    문제
    지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

    입력
    첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

    출력
    첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

    예제 입력 1 
    11
    예제 출력 1 
    1 4 1 1 1 1 1 1 1 1
    예제 입력 2 
    7
    예제 출력 2 
    0 1 1 1 1 1 1 1 0 0
"""

import sys

n=int(sys.stdin.readline().strip())
a=[0]*10
b=1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            a[int(i)] += b
        n -= 1
        
    if n < 10:
        for k in range(n+1):
            a[k] += b
        a[0] -= b
        break
    
    else:
        for i in range(10):
            a[i] += (n//10 + 1) * b
    a[0] -= b
    b *= 10
    n //= 10
    
for i in a:
    print(i,end=' ')


""" [백준] 1019번 책 페이지 - PYTHON
    https://www.acmicpc.net/problem/1019
    문제
    지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

    입력
    첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

    출력
    첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

    예제 입력 1 
    11
    예제 출력 1 
    1 4 1 1 1 1 1 1 1 1
    예제 입력 2 
    7
    예제 출력 2 
    0 1 1 1 1 1 1 1 0 0
"""

import sys

n=int(sys.stdin.readline().strip())
a=[0]*10
b=1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            a[int(i)] += b
        n -= 1
        
    if n < 10:
        for k in range(n+1):
            a[k] += b
        a[0] -= b
        break
    
    else:
        for i in range(10):
            a[i] += (n//10 + 1) * b
    a[0] -= b
    b *= 10
    n //= 10
    
for i in a:
    print(i,end=' ')
