N = int(input())
num = list(map(int, input().split()))
# 조건에 해당하지 않을 경우 -1
result = [-1 for _ in range(N)]
ans = []

for i in range(len(num)):
    # ans는 스택인데 스택이 비어있지 않고 오른쪽의 수가 왼쪽보다 클 경우(오큰수)
    while len(ans) != 0 and num[ans[-1]] < num[i]:
        result[ans.pop()] = num[i]
    ans.append(i)

# 배열의 요소만 출력 
print(*result)