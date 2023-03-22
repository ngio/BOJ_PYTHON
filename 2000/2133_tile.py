"""_summary_
    타일 채우기 
    https://www.acmicpc.net/problem/2133
    문제 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
    입력 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
"""
n = int(input("값을 입력하세요~ : "))
tile = [0 for _ in range(31)]
tile[2] = 3
for i in range(4, n+1):
    if i%2 == 0:
        tile[i] = tile[i-2] * 3 + sum(tile[:i-2]) * 2 + 2
    else:
        tile[i] = 0

print(tile[n])

#2번째 풀이 

n = int(input())
dp = [0]*(n+1)

if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])
