from itertools import permutations

def solution(expression):
    answer = []
    operator = ["+", "-", "*"]
    
    for oper in permutations (operator, 3):
        temp = [""]
        for exp in expression:
            if exp.isdigit() and temp[-1] not in operator:
                temp[-1] += exp
            else:
                temp.append(exp)
        for i in oper:
            while i in temp:
                index = temp.index(i)
                temp = temp[:index-1] + [str(eval(''.join(temp[index-1:index+2])))] + temp[index+2:]
        answer.append(abs(int(temp[0])))

    return max(answer)