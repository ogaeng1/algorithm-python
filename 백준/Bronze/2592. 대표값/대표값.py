num = []
for i in range(10):
  n = int(input())
  num.append(n)

print(sum(num) // 10)
print(max(set(num), key=num.count))