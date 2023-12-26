from collections import Counter

n = int(input())
best_seller = []

for _ in range(n):
  best_seller.append(input())

best_seller = sorted(best_seller)

cnt = Counter(best_seller).most_common()
print(cnt[0][0])