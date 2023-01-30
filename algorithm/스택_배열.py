# 스택 - 배열

class Stack():
    def __init__(self):
        self.stack = [1, 2, 3]

    # 데이터 삽입
    def push(self, data):
        # append를 이용해 데이터 삽입
        self.stack.append(data)

    # 데이터 삭제
    def pop(self):
        pop_object = None
        # stack이 비어있는지 isEmpty를 통해서 확인
        if self.isEmpty():
            print("Stack is Empty")
        #  만약 비어있지 않다면 삭제
        else:
            pop_object = self.stack.pop()
        return pop_object

    def top(self): 
        top_object = None 
        # stack이 비어있는지 isEmpty를 통해서 확인
        if self.isEmpty(): 
            print("Stack is Empty")
        # stack이 비어있지 않다면 가장 마지막 값을 인덱스 -1을 활용하여 값만 가져와서 리턴
        else: 
            top_object = self.stack[-1]
        return top_object 
    
    # 스택이 비었는지 확인
    def isEmpty(self): 
        is_empty = False 
        # 스택의 길이를 통해서 stack이 비어있는지 확인
        if len(self.stack) == 0: 
            is_empty = True 
        return is_empty