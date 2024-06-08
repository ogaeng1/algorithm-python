import sys
input = sys.stdin.readline
game, win = map(int, input().split())
win_rate = (win * 100) // game

res = 0
if win_rate >= 99:
  print(-1)
else:
  start, end = 0, game
  while start <= end:
    mid = (start+end) // 2
    update_rate = ((win+mid) * 100) // (game + mid)

    if update_rate > win_rate:
      res = mid
      end = mid - 1
    else:
      start = mid + 1

  print(res)