""" [백준] 1007번 벡터 매칭 - PYTHON vector matching
    https://www.acmicpc.net/problem/1007
    문제
        평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자. 집합 P의 벡터 매칭은 벡터의 집합인데, 모든 벡터는 집합 P의 한 점에서 시작해서, 또 다른 점에서 끝나는 벡터의 집합이다. 또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.
        벡터 매칭에 있는 벡터의 개수는 P에 있는 점의 절반이다.
        평면 상의 점이 주어졌을 때, 집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 출력하는 프로그램을 작성하시오.
    입력
        첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.
        테스트 케이스의 첫째 줄에 점의 개수 N이 주어진다. N은 짝수이다. 둘째 줄부터 N개의 줄에 점의 좌표가 주어진다. N은 20보다 작거나 같은 자연수이고, 좌표는 절댓값이 100,000보다 작거나 같은 정수다. 모든 점은 서로 다르다.
    출력
        각 테스트 케이스마다 정답을 출력한다. 절대/상대 오차는 10-6까지 허용한다.
    알고리즘 분류
        수학
        브루트포스 알고리즘
"""

import sys, itertools
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input()) # 점의 개수
    points = [] # 좌표의 리스트
    total_x,total_y = 0,0
 
    for _ in range(N):
        x,y = map(int,input().split())
        total_x +=x ; total_y += y # 모든 x의 합과 y의 합 저장
        points.append((x,y))
 
    comb = list(itertools.combinations(points, N//2))
    ans=3e5
    
    for c in comb[:len(comb)//2]: # len(comb)는 항상 짝수
        x1,y1 = 0,0
        for x,y in c:
            x1 += x ; y1 += y
        x2,y2 = total_x-x1,total_y-y1 # x와 y를 x1,y1과 x2,y2 두 그룹으로 절반 나누기
        
        hab_vector = ((x2-x1)**2 + (y2-y1)**2)**(0.5) # 절반 나눈 두 그룹간의 합벡터
        ans=min(ans,hab_vector)
    print(ans)
