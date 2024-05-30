import sys

n = int(sys.stdin.readline())
in_out_log = {}

for _ in range(n):
  name, state = input().split()

  if state == 'enter':
    in_out_log[name] = True
  else:
    del in_out_log[name]

for stay_company in sorted(in_out_log, reverse=True):
  print(stay_company)