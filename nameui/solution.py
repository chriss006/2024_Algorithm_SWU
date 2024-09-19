def solution(N, K):
    arr = [True] * N
    base = 0
    deletionTarget = (base + K - 1) % N

    for _ in range(len(arr)-1):
        while not arr[base]:
            base = (base + 1) % N
            deletionTarget = (base + K - 1) % N

        while not arr[deletionTarget]:
            deletionTarget = (deletionTarget + 1) % N

        arr[deletionTarget] = False
        
        base = (deletionTarget + 1) % N
        deletionTarget = (base + K - 1) % N

    for j in range(len(arr)):
        if arr[j]:
            return j+1

print(solution(5, 2))

from collections import deque

def solution(N, K):
    #❶ 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1, N+1))

    while len(queue) > 1: #❷ deque에 하나의 요소가 남을 때까지
        for _ in range(K-1):
            queue.append(queue.popleft()) #❸ K번째 요소를 찾기 위해 앞에서부터 제거하고 뒤에 추가
        queue.popleft() #❹ K번째 요소 제거
    return queue[0] #❺ 마지막으로 남은 요소 반환
    
    
print(solution(5,2))