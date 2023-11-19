t = int(input())
for tc in range(1, t+1):
    num = int(input())
    answer = ''
    for i in range(num):
        a, b = input().split()
        answer += a*int(b)
    
    for i in range(0, len(answer), 10):
        print(answer[i:i+10])