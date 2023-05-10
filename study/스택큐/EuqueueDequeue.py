queue_list = list()

# 배열의 마지막에 데이터 삽입
def enqueue(data):
    queue_list.append(data)

# 배열의 가장 앞에 있는 데이터 제거
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

# 배열에 0부터 9까지 추가
for index in range(10):
    enqueue(index)

print(len(queue_list))