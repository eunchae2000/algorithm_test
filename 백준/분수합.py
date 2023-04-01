import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

bunmo = b1*b2
bunja = (a1*b2) + (a2*b1)

# gcd: 최대공약수
# lcm: 최소공배수

result = math.gcd(bunja, bunmo)

print(bunja//result, bunmo//result)