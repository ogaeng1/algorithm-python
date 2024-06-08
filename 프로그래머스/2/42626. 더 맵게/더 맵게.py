import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0
    
    while scoville and scoville[0] < K and len(scoville) > 1:
        min_scov1 = heapq.heappop(scoville)
        min_scov2 = heapq.heappop(scoville)
        mix_scov = min_scov1 + (min_scov2 * 2)
        heapq.heappush(scoville, mix_scov)
        res += 1
        
    return res if scoville[0] >= K else -1