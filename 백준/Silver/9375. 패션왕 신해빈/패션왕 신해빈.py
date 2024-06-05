import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  clothes = int(input())
  clothe_dict = {}
  res = 1

  for _ in range(clothes):
    name, kind = input().split()
    clothes_type = kind

    if clothes_type in clothe_dict:
      clothe_dict[clothes_type] += 1
    else:
      clothe_dict[clothes_type] = 1

  for i in clothe_dict.values():
    res *= i + 1

  print(res-1)