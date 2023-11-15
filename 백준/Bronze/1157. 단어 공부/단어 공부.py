word = input().upper()
w_list = list(set(word))
cnt = []

for i in w_list:
  w_count = word.count
  cnt.append(w_count(i))

if cnt.count(max(cnt)) > 1:
  print("?")
else:
  print(w_list[(cnt.index(max(cnt)))])