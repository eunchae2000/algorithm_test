def way_to_buy(psum, k):
    MOD = 20091101
    ret = 0
    # 인형의 개수를 저장
    count = {}
    
    cum_sum = 0
    for num in psum:
        count[num] += 1
    
    for i in range(k + 1):  
        if count[i] >= 2:
            ret = (ret + ((count[i] * (count[i] - 1)) // 2)) % MOD
    
    return ret


def max_buys(psum, k):
    ret = [0] * len(psum)
    prev = {}
    
    for i in range(len(psum)):
        if i > 0:
            ret[i] = ret[i - 1]
        else:
            ret[i] = 0
        
        loc = prev[psum[i]]
        
        if loc != -1:
            ret[i] = max(ret[i], ret[loc] + 1)
        
        prev[psum[i]] = i
    
    return ret[-1]

# Example Usage
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    psum = list(map(int, input().split()))
    
    result1 = way_to_buy(psum, k)
    result2 = max_buys(psum, k)
    
    print(result1, result2)