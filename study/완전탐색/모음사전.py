from itertools import product

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6):
        for j in product(words, repeat=i):
            arr.append(''.join(j))

    arr.sort()
    return arr.index(word)+1
print(solution("AAAAE"))