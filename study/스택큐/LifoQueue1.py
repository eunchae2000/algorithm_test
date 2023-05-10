import queue
data_queue = queue.LifoQueue()

# 큐에 데이터 삽입
data_queue.put("data")
data_queue.put(7)

# 현재 큐에 데이터가 몇 개인지 확인
data_queue.qsize()

# 큐에 데이터 제거
data_queue.get()

data_queue.qsize()

data_queue.get()

data_queue.qsize()