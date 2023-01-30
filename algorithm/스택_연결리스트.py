# 스택 - 연결리스트

class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class LinkedListStack():
    def __init__(self): 
        self.head = None 
    
    # 새로운 데이터를 담을 노드 생성
    def push(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node 
    
    # 데이터 삭제
    def pop(self): 
        pop_object = None 
        if self.isEmpty(): 
            print("Stack is Empty") 
        else: 
            pop_object = self.head.data 
            self.head = self.head.next 
            return pop_object 
    
    # 가장 상위의 데이터 리턴
    def top(self): 
        top_object = None 
        if self.isEmpty(): 
            print("Stack is Empty") 
        else: top_object = self.head.data 
        return top_object 
        
    # 스택이 비어있는지 확인
    def isEmpty(self): 
        is_empty = False 
        if self.head is None: 
            is_empty = True 
        return is_empty