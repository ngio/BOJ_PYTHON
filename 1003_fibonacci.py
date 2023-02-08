"""_summary_
   1003번 피보나치 함수  https://www.acmicpc.net/problem/1003
   문제
        다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

        int fibonacci(int n) {
            if (n == 0) {
                printf("0");
                return 0;
            } else if (n == 1) {
                printf("1");
                return 1;
            } else {
                return fibonacci(n‐1) + fibonacci(n‐2);
            }
        }
        fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

        fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
        fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
        두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
        fibonacci(0)은 0을 출력하고, 0을 리턴한다.
        fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
        첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
        fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
        1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
        입력
            첫째 줄에 테스트 케이스의 개수 T가 주어진다.
            각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

        출력
            각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

        예제 입력 1 
            3
            0
            1
            3
        예제 출력 1 
            1 0
            0 1
            1 2
        예제 입력 2 
            2
            6
            22
        예제 출력 2 
            5 8
            10946 17711
 
처음에 zero는 1,0,1로 나열되고 one은 0,1,1로 나열된다.
그 이후의 n번째부터는 피보나치 수열(N2 = N1 + N0)로 나열된다.

그렇다면 이제, 규칙을 가지고 구현해보자.

0과 1의 초기배열을 먼저 만들어준다.
0은 [1,0,1] 1은 [0,1,1] 로 정해져있음.
for문으로 초기배열 이후 피보나치 수열로 구한 값을 배열에 추가해준다.
각 테스트케이스마다 0과 1의 횟수를 공백으로 출력해야한다.

"""

t = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n) : #[0,1,3]
    if len(zero) <= n :
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t) : #[3]
    a = int(input()) #[0,1,3]
    fibo(a)
