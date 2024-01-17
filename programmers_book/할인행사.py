def solution(want, number, discount):
    dic = {}
    count = 0
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        market = {}
        for j in range(i, i+10):
            if discount[j] in dic:
                market[discount[j]] = market.get(discount[j], 0)+1
        if market == dic:
            count += 1
    return count

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))