import math

def solutoion(progress, speeds):
    arr = []
    answer = []
    
    for i in range(len(progress)):
        num = math.ceil((100-progress[i])/speeds[i])
        arr.append(num)
    
    max_days = arr[0]
    count = 0
    
    for i in range(len(arr)):
        if arr[i] <= max_days:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_days = arr[i]  # 위치 옮기기
    answer.append(count)
    return answer
        
print(solutoion([93, 30, 55], [1, 30, 5]))
print(solutoion([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))