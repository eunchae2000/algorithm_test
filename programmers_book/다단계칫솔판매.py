def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    answer = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100
        current_name = seller[i]
        
        while money != 0 and current_name != "-":
            answer[current_name] += money - money // 10
            current_name = parent[current_name]
            money //= 10
    
    return [answer[name] for name in enroll]
    

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))