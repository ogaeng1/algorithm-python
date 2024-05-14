# 스택을 활용한 풀이

def solution(order):
    # 실을 수 있는 상자 수, 트럭에 실어야 하는 상자 순서
    answer, cur_box = 0, 0
    # 보조 컨테이너 스택
    sub_container = []
    
    # 컨테이너 순회
    for i in range(1, len(order)+1):
        # 현재 상자를 일단 보조 컨테이너로 이동
        sub_container.append(i)
        
        # 조건이 일치하면 상자를 실을 수 있으니까 상자 개수 및 현재 상자 카운트
        while sub_container and sub_container[-1] == order[cur_box]:
            sub_container.pop()
            answer += 1
            cur_box += 1
            
    return answer

