L, P = map(int, input().split())
news = list(map(int, input().split()))
human = L * P

for i in range(5):
  print(news[i] - human, end=" ")