def solution(p):
    if not p:
        return ""
    
    def is_valid(w):
        count = 0
        for i in range(len(w)):
            count += 1 if w[i] == '(' else -1
            if count == 0:
                return w[:1+i], w[1+i:]
        return w, ""
    
    def is_correct(u):
        stack = []
        for i in u:
            if i == '(':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                return False
        return not stack
    
    def recursive(w):
        if not w:
            return ""
        
        u, v = is_valid(w)
        
        if is_correct(u):
            return u + recursive(v)
        else:
            result = '(' + recursive(v) + ')'
            result += ''.join(['(' if char == ')' else ')' for char in u[1:-1]])
            return result
    return recursive(p)