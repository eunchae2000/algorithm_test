def w(a, b, c, memo={}):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    
    if a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20)
        memo[(a, b, c)] = result
        return result

    if a < b and b < c:
        result = (
            w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
        )
        memo[(a, b, c)] = result
        return result
    
    result = (
        w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
    )
    
    memo[(a, b, c)] = result
    return result

while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    answer = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {answer}')
