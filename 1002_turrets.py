"""_summary_
   1002번 터렛 turret https://www.acmicpc.net/problem/1002
   문제
        조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
        이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
        조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
        입력
            첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
            한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
        출력
            각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
        예제 입력 1 
            3
            0 0 13 40 0 37
            0 0 3 0 7 4
            1 1 1 1 1 5
        예제 출력 1 
            2
            1
            0
            
        두 원의 중심이 동일하고, 반지름이 같다면 적이 존재할 수 있는 좌표는 무한대이다 -> -1 리턴
        두 원의 반지름의 합이 두 원의 중심사이의 거리라면 외접, 두 원의 반지름의 차가 두 원의 중심사이의 거리라면 내접한다 -> 1리턴
        두 원의 반지름의 합이 두 원의 중심사이의 거리보다 크고, 두 원의 반지름의 차가 두 원의 중심사이의 거리보다 작다면 두개의 교점 -> 2리턴
        그 외에는 교점이 없다. -> 0리턴
        
         * 네 가지 경우가 존재
        첫 번째 경우 : 두 원이 접하지 않는 경우
        두 번째 경우 : 두 원이 한 점에서 접하는 경우
        세 번째 경우 : 두 원이 두 점에서 접하는 경우
        네 번째 경우 : 두 원이 일치하는 경우
"""

# x1, y1, r1, x2, y2, r2 = map(int, input().split())

def turret(x1,y1,r1,x2,y2,r2):
    dist = pow( ( (x1-x2)**2 + (y1-y2)**2 ), 0.5 )
    temp=r1+r2
    temp2=abs(r1-r2)

    if (dist == 0) :
        if (temp2 == 0):
            return -1
        else:
            return 0
    elif (dist == temp or dist == temp2):
        return 1
    elif (temp2 < dist and dist < temp):
        return 2
    else:
        return 0

testcase = int(input())
for i in range(testcase):
    a,b,c,d,e,f = map(int, input().split())
    print(turret(a,b,c,d,e,f))
    
#=============================================================   
    

import math
num = int(input())
results = []

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # 두 원의 중심 사이의 거리
    if x1 == x2 and y1 == y2 and r1 == r2: results.append(-1) # 교점이 무한대
    elif abs(r1 - r2) < d and r1 + r2 > d: results.append(2) # 교점이 두 개인 경우
    elif abs(r1 - r2) == d or r1 + r2 == d: results.append(1) # 접하는 경우
    else: results.append(0) # 교점이 없음

for result in results:
    print(result)




    
