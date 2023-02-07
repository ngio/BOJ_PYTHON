"""_summary_
    https://www.acmicpc.net/problem/1001
    문제
    두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
    입력
    첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
    출력
    첫째 줄에 A-B를 출력한다.

    예제 입력 1 
    3 2
    예제 출력 1 
    1
"""

# A, B = input("값을 입력하세요~ (ex; 3 2 ): ").split()  

A, B = input().split()
print(int(A)-int(B))
