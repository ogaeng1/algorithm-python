# 바구니에 같은 모양 인형 두 개가 쌓이면 사라짐 => 자료구조 스택 문제

def solution(board, moves):
    stack = []
    answer = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
            
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        # 인형이 제거된 횟수가 아니라 제거된 인형 갯수니까 +2 를 해준다.
                        answer += 2
                break
                
    return answer