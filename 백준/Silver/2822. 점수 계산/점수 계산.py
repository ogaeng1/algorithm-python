score = [int(input()) for _ in range(8)]

score_sort = sorted(score)[-5:]

problem_num = []
for i in score_sort:
  problem_num.append(score.index(i)+1)

problem_num.sort()

print(sum(score_sort))

for i in problem_num:
  print(i, end=' ')