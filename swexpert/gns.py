str_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGH', 'NIN']

t = int(input())

for tc in range(1, t+1):
    n, length = map(str, input().split())
    number = list(map(str, input().split()))
    answer = []
    
    for i in range(10):
        for s in number:
            if str_list[i] == s:
                answer.append(s)
    print(n)
    print(*answer)