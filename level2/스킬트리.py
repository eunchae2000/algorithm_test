def solution(skill, skill_trees):
    count = 0
    
    for skill_tree in skill_trees:
        s = ''
        for sk in skill_tree:
            if sk in skill:
                s += sk
        if skill[:len(s)] == s:
            count += 1
    return count

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))