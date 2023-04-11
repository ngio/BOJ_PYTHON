""" [백준] 1021번 회전하는 큐
    https://www.acmicpc.net/problem/1021
    
    문제
    지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

    지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
     1.첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
     2.왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
     3.오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
    
    큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

    입력
    첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
    
    예제 입력 1 
    10 3
    1 2 3
    예제 출력 1 
    0
    예제 입력 2 
    10 3
    2 9 5
    예제 출력 2 
    8
"""
import sys

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split(' ')))
queue = [i for i in range(1, N+1)]

ans = 0
for target in targets:
    plus_index = queue.index(target) # 앞에꺼를 뒤로 넘기는 연산 수
    minus_index = len(queue) - plus_index # 뒤에꺼를 앞으로 넘기는 연산 수
    steps = min(plus_index, minus_index) # 둘 중 최솟값

    # plus는 2번 연산
    # minus는 3번 연산
    if steps == plus_index: sign = 'plus' 
    else: sign = 'minus'

    if sign == 'plus':
        for _ in range(steps):
            temp = queue.pop(0)
            queue.append(temp)
    else:
        for _ in range(steps):
            temp = queue.pop(-1)
            queue.insert(0, temp)
    
    ans += steps
    queue.pop(0)

print(ans)


# 참고  : https://www.acmicpc.net/problem/1021
