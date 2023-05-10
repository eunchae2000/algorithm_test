class ListQueue(object):
    def __init__(self):
        self.queue = []
    
    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    
    def enqueue(self, n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    queue_list = ListQueue()
    queue_list.enqueue(1)
    queue_list.enqueue(2)
    queue_list.enqueue(3)
    queue_list.enqueue(4)
    queue_list.enqueue(5)
    queue_list.printQueue()
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    queue_list.printQueue()