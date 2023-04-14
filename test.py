from collections import deque

def solution(bridge_length,weight,truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    time = 0
    bridge_weight = 0
    while len(bridge) != 0:
        out = bridge.popleft()
        print(out)
        bridge_weight -= out
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left = truck_weights.popleft()
                bridge_weight += left
                bridge.append(left)
            else:
                bridge.append(0)
    return time
print(solution(2,10,[7,4,5,6]))