N, M = map(int, input().split())
card_num = list(map(int, input().split()))

result = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      card_sum = card_num[i] + card_num[j] + card_num[k]
      if card_sum <= M:
        result = max(result, card_sum)

print(result)