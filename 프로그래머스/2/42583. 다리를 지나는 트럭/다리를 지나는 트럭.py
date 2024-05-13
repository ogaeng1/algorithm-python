# 트럭이 순서대로 건너야 함 -> 큐 활용

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_on_truck = deque([0] * bridge_length)
    truck = deque(truck_weights)
    cur_bridge_weight = 0
    
    while truck:
        time += 1
        cur_bridge_weight -= bridge_on_truck.popleft()

        if cur_bridge_weight + truck[0] <= weight:
            cur_bridge_weight += truck[0]
            bridge_on_truck.append(truck.popleft())
        else:
            bridge_on_truck.append(0)
            
    return time + bridge_length
