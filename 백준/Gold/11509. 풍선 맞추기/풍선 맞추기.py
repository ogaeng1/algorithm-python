n = int(input())
height = list(map(int, input().split()))

arrow = [0] * 1000001
cnt = 0

for i in range(n):
  if arrow[height[i]] == 0:
    cnt += 1
    arrow[height[i] - 1] += 1
  else:
    arrow[height[i]] -= 1
    arrow[height[i] - 1] += 1

print(cnt)