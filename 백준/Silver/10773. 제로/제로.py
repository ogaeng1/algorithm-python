n = int(input())
money_record = []

for _ in range(n):
  num = int(input())
  if num != 0:
    money_record.append(num)
  else:
    money_record.pop()

print(sum(money_record))