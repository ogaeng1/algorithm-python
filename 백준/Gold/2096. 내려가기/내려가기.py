import sys

N = int(sys.stdin.readline())

max_num = [0, 0, 0]
min_num = [0, 0, 0]

for _ in range(N):
  cur_num = list(map(int, input().split()))
  max_num = [cur_num[0] + max(max_num[:2]), cur_num[1] + max(max_num), cur_num[2] + max(max_num[1:])]
  min_num = [cur_num[0] + min(min_num[:2]), cur_num[1] + min(min_num), cur_num[2] + min(min_num[1:])]

print(max(max_num), min(min_num))