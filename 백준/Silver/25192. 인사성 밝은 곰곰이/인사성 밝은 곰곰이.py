import sys
input = sys.stdin.readline
chatting_log = {}
cnt = 0

N = int(input())

for _ in range(N):
  chatting = input().strip()

  if chatting == 'ENTER':
    chatting_log.clear()
  else:
    if chatting not in chatting_log:
      cnt += 1
      chatting_log[chatting] = 1

print(cnt)