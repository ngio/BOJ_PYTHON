"""[BOJ] python 1015번 수열정렬 
    https://www.acmicpc.net/problem/1015

    문제
    P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다. 
    수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.

    배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오. 
    비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 
    만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.

    입력
    첫째 줄에 배열 A의 크기 N이 주어진다. 둘째 줄에는 배열 A의 원소가 0번부터 차례대로 주어진다. 
    N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수이다.

    출력
    첫째 줄에 비내림차순으로 만드는 수열 P를 출력한다.

    예제 입력 1 
    3
    2 3 1
    예제 출력 1 
    1 2 0

    예제 입력 2 
    4
    2 1 3 1
    예제 출력 2 
    2 0 3 1

    예제 입력 3 
    8
    4 1 6 1 3 6 1 4
    예제 출력 3 
    4 0 6 1 3 7 2 5
"""
import sys
import math

A_size = int(sys.stdin.readline())
A = sys.stdin.readline().replace("\n", "").split(' ')
A = [int(i) for i in A]

# A를 오름차순으로 정렬하여 작은 숫자부터 순서대로 정리된 새로운 list를 할당 
sorted_A = [i for i in A]
sorted_A.sort()

P = []
# A의 각 숫자들에 대해 sorted_A에서의 index를 찾아 몇번째로 작은 숫자인지 P 수열에 새롭게 append함.
for i in A:
    P.append(sorted_A.index(i))
    # 이미 할당한 숫자는 sorted_A에서 -1로 대채해 재탐색되지 않도록 함.
    sorted_A[sorted_A.index(i)] = -1

results = [i for i in P]

for result in results:
    sys.stdout.write(str(result)+' ')
    
#  출처 : https://nerogarret.tistory.com/31
