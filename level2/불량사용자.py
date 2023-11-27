from itertools import permutations

def check(user, banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(user[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    answer = []
    
    for user in user_permutation:
        if not check(user, banned_id):
            continue
        else:
            user = set(user)
            if user not in answer:
                answer.append(user)
    
    return len(answer)
    
                
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))