"""_summary_
   두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
   https://www.acmicpc.net/problem/1000
   입력
    첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
    출력
    첫째 줄에 A+B를 출력한다.

    예제 입력 1 
    1 2
    예제 출력 1 
    3
    
    입력을 받을 때 A와 B는 같은 줄에 입력을 받아야하기 때문에
    공백을 기준으로 나눠주는 split 함수를 이용하도록 하겠습니다.
    받아온 a와 b는 문자형이기 때문에 int() 를 이용하여 정수로 바꾸어 더해주었습니다.

"""

# 아래 처럼 쓸데없이 정보를 많이 넣으면 틀렸습니다. 로 나오니 주의하자. 
# A, B = input("값을 입력하세요~ (ex; 1 2 ): ").split()  

A, B = input().split()
print(int(A)+int(B))

a, b = map(int, input().split())
print(a+b)
