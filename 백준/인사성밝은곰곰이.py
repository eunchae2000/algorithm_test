def solution(n):
    member = set()
    count = 0
    for i in range(n):
        m = input()

        if m != 'ENTER':
            if m not in member:
                count += 1
                member.add(m)
        elif m == 'ENTER':
            member.clear()
    return count
print(solution(int(input())))