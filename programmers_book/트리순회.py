def preorder(nodes, index):
    if len(nodes) > index:
        ret = str(nodes[index]) + " "
        ret += preorder(nodes, index*2+1)
        ret += preorder(nodes, index*2+2)
        return ret
    else:
        return ""

def inorder(nodes, index):
    if index<len(nodes):
        ret = inorder(nodes, index*2+1)
        ret += str(nodes[index]) + " "
        ret += inorder(nodes, index*2+2)
        return ret
    else:
        return ""

def postorder(nodes, index):
    if index<len(nodes):
        ret = inorder(nodes, index*2+1)
        ret += inorder(nodes, index*2+2)
        ret += str(nodes[index]) + " "
        return ret
    else:
        return ""

def solution(nodes):
    return[
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]

print(solution([1, 2, 3, 4, 5, 6, 7]))