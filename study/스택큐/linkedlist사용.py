class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return -1
        
        v = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        return v
    
    # 출력
    def print(self):
        current = self.head
        string = ""
        while current:
            string += str(current.data)
            if current.next:
                string += "->"
            current = current.next
        print(string)

if __name__ == "__main__":
    s = SingleyLinkedList()
    # 데이터 삽입
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.enqueue(Node(4))
    s.print()

    # 데이터 제거
    print(s.dequeue())
    print(s.dequeue())
    s.print()
    print(s.dequeue())
    print(s.dequeue())