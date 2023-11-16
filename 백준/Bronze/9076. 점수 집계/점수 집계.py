T = int(input())

for _ in range(T):
  score = sorted(list(map(int, input().split())))
  score = score[1:len(score)-1]
  if max(score) - min(score) >= 4:
    print("KIN")
  else:
    print(sum(score))