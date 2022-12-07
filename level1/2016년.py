def solution(a, b):
    answer = ''
    result = b-1
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a-1):
        result += month[i]
    
    answer = result%7

    return days[answer]

print(solution(1, 11))
print(solution(5, 24))