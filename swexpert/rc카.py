# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     answer = []
#     result = 0
#     for i in range(n):
#         car = input()
#         if len(car) == 1:
#             car = int(car)
#             answer.append(answer[-1])
#         else:
#             a = int(car[0])
#             b = int(car[2])
#             if a == 1:
#                 result += b
#                 answer.append(result)
#             else:
#                 result -= b
#                 answer.append(result)
#     print(f'#{tc} {sum(answer)}')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    speed = 0
    distance = 0
    
    for i in range(n):
        c = list(map(int, input().split()))
        
        if(c[0] == 1):
            speed += c[1]
        elif (c[0] == 2):
            speed -= c[1]
            if (speed <0):
                speed = 0
        distance += speed
    print(f'#{tc} {distance}')