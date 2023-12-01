import sys

n = int(input())
num = []

for _ in range(n):
  number = int(sys.stdin.readline())
  num.append(number)

num.sort()
print(round(sum(num) / n))
print(num[n//2])

dic = dict()

for i in num:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

most_num = max(dic.values())
most_list = [key for key, value in dic.items() if value == most_num]
most_list.sort()

print(most_list[0] if len(most_list) == 1 else most_list[1])
print(max(num) - min(num))