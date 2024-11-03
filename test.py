def solution(book_time):
    start_times = []
    end_times = []
    
    for start, end in book_time:
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        start_total = start_h*60+start_m
        start_times.append(start_total)
        
        end_total = end_h*60+end_m+10
        end_times.append(end_total)
    
    start_times.sort()
    end_times.sort()
    
    s, e = 0, 0
    used_room = 0
    max_room = 0
    
    while s<len(book_time):
        if start_times[s] < end_times[e]:
            used_room += 1
            max_room = max(used_room, max_room)
            s += 1
        else:
            used_room -= 1
            e += 1
    return max_room


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))