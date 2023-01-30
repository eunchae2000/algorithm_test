def solve(a):
    result = 0
    for i in a:
        result += i
    return result
a = list(map(int, input().split()))
print(solve(a))