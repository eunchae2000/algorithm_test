import queue
data_queue = queue.PriorityQueue()

# 데이터 추가
# tuple 형식으로 데이터 추가(우선순위, 데이터)
# 우선순위는 숫자가 작을수록 높음
data_queue.put((10, "data1"))
data_queue.put((5, 7))
data_queue.put((15, "data2"))

# 현재 큐에 데이터가 몇 개인지 확인
data_queue.qsize()

# 데이터 제거
data_queue.get()

data_queue.get()