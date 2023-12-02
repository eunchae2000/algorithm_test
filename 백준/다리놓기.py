n = int(input())

def factorial(number):
    answer = 1
    for i in range(2, number+1):
        answer *= i
    return answer

for i in range(n):
    a, b = map(int, input().split())
    n1 = max(a, b)
    n2 = min(a, b)
    num1 = factorial(n1)
    num2 = factorial(n2)
    num3 = factorial(n1-n2)
    print(num1//(num2*num3))