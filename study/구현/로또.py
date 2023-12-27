from itertools import combinations

while True:
    s = list(map(int, input().split()))
    
    s_num = s[0]
    s_list = s[1:]
    
    if s_num == 0:
        exit()
    
    answer = list(combinations(s_list, 6))
    answer.sort()
    
    for num in answer:
        print(*num)
    print()