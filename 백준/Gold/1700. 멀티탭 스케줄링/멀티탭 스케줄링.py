import sys
input = sys.stdin.readline

n, k = map(int, input().split())
elec = list(map(int, input().split()))
tap = []
res = 0

for i in range(k):
  product = elec[i]

  if product in tap:
    continue
    
  if len(tap) < n:
    tap.append(product)
  else:
    far = idx_replace = -1
    for j in range(n):
      if tap[j] in elec[i:]:
        use_product = elec[i:].index(tap[j])
        if use_product > far:
          far = use_product
          idx_replace = j
      else:
        idx_replace = j
        break

    tap[idx_replace] = product
    res += 1

print(res)