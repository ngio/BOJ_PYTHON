""" [백준] 1018번 체스판 다시 칠하기 - python
    https://www.acmicpc.net/problem/1018
    문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

예제 입력 1 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
예제 출력 1 
1
예제 입력 2 
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
예제 출력 2 
12
예제 입력 3 
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
예제 출력 3 
0
예제 입력 4 
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
예제 출력 4 
31
예제 입력 5 
10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB
예제 출력 5 
0
예제 입력 6 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW
예제 출력 6 
2
예제 입력 7 
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
예제 출력 7 
15
"""
import sys

N, M = map(int, sys.stdin.readline().split())

board = []
white_first = []
black_first = []

for _ in range(N):
    row = sys.stdin.readline().replace("\n", "")
    board.append([i for i in row])

initial_color = board[0][0]

# 흰색으로 시작하는 체스판을 만들 경우
for index, row in enumerate(board):
    painting = []
    if index % 2 == 0: current_color = "W"
    else: current_color = "B"

    for value in row:
        if value == current_color: painting.append(0)
        else: painting.append(1)
        
        if current_color == "W": current_color = "B"
        else: current_color = "W"
    white_first.append(painting)

# 검은색으로 시작하는 체스판을 만들 경우
for index, row in enumerate(board):
    painting = []
    if index % 2 == 0: current_color = "B"
    else: current_color = "W"

    for value in row:
        if value == current_color: painting.append(0)
        else: painting.append(1)
        
        if current_color == "W": current_color = "B"
        else: current_color = "W"
    black_first.append(painting)

# 최솟값을 초기화 할 때, 보드의 최대 크기인 50*50 = 2500으로 한다.
min_count = 2500
for i in range(N-8+1):
    rows = white_first[i:i+8]
    for j in range(M-8+1):
        paint = 0
        for row in rows:
            paint += sum(row[j:j+8])
        if paint < min_count: min_count = paint

for i in range(N-8+1):
    rows = black_first[i:i+8]
    for j in range(M-8+1):
        paint = 0
        for row in rows:
            paint += sum(row[j:j+8])
        if paint < min_count: min_count = paint

print(min_count)

# 참조 : https://nerogarret.tistory.com/35

