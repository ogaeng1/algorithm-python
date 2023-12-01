import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
own_card = list(map(int, input().split()))

dic = dict()

for i in card:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in own_card:
  if i in dic:
    print(dic[i], end=' ')
  else:
    print('0', end=' ')