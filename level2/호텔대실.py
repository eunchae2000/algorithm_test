def solution(book_time):
    start_time = []
    end_time = []
    
    for start, end in book_time:
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        start_total = start_h*60+start_m
        end_total = end_h*60+end_m+10
        
        start_time.append(start_total)
        end_time.append(end_total)
        
    start_time.sort()
    end_time.sort()
    
    s, e = 0, 0
    room = 0
    max_room = 0
    
    while s < len(book_time):
        if start_time[s] < end_time[e]:
            room += 1
            max_room = max(room, max_room)
            s += 1
        else:
            room -= 1
            e += 1
    return max_room