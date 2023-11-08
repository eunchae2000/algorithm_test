def solution(keymap, targets):
    answer = []
    
    for word in targets:
        times = 0
        
        for char in word:
            flag = False
            time = 101
            
            for key in keymap:
                if char in key:
                    flag = True
                    time = min(key.index(char)+1, time)
            
            if not flag:
                times = -1
                break
            
            times += time
        answer.append(times)
                    
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))