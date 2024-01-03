n = int(input())
dic = dict()


for _ in range(n):
  file = input().split('.')[-1]

  if file in dic:
    dic[file] += 1
  else:
    dic[file] = 1

sort_dic = dict(sorted(dic.items(), key=lambda x: x[0]))

for key, value in sort_dic.items():
  print(key, value)