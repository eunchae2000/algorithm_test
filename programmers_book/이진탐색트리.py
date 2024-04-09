class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key<current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(key)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(key)
                        break
    def search(self, key):
        current = self.root
        while current ans current.val != key:
            if key<current.val:
                current = current.left
            else:
                current = current.right
        return current
    

def solution(lst, search_list):
    bst = BST()
    for key in lst:
        bst.insert(key)
    
    result = []
    for search_val in search_list:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result
