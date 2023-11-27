N, money = map(int, input().split())
coin = [int(input()) for i in range(N)]
cnt = 0

for i in coin[::-1]:
  cnt += money // i
  money = money % i

print(cnt)