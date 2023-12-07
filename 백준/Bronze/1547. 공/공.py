m = int(input())

ball = [1, 0, 0]

for _ in range(m):
  cup1, cup2 = map(int, input().split())
  ball[cup1-1], ball[cup2-1] = ball[cup2-1], ball[cup1-1]

print(ball.index(1)+1)