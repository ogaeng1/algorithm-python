jinho = input()
N = int(input())
cnt = 0

for _ in range(N):
  mbti = input()
  if mbti == jinho:
    cnt += 1
print(cnt)