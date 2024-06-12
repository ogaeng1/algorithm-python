import sys
input = sys.stdin.readline
move = {
  "R": (0, 1),
  "L": (0, -1),
  "B": (1, 0),
  "T": (-1, 0),
  "RT": (-1, 1),
  "LT": (-1, -1),
  "RB": (1, 1),
  "LB": (1, -1)
}

king, stone, moving = input().split()

king_r, king_c = 8-(int(king[1])), ord(king[0])-ord('A')
stone_r, stone_c = 8-(int(stone[1])), ord(stone[0])-ord('A')
for _ in range(int(moving)):
  direction = input().strip()

  nx, ny = move[direction]
  if king_r+nx < 0 or king_r+nx >= 8 or king_c+ny < 0 or king_c+ny >= 8:
    continue
  king_r += nx
  king_c += ny

  if king_r == stone_r and king_c == stone_c:
    if stone_r+nx < 0 or stone_r+nx >= 8 or stone_c+ny < 0 or stone_c+ny >= 8:
      king_r -= nx
      king_c -= ny
      continue
    stone_r += nx
    stone_c += ny

print(chr(ord("A")+king_c)+str(8-king_r))
print(chr(ord("A")+stone_c)+str(8-stone_r))