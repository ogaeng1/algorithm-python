import sys
input = sys.stdin.readline
n = int(input())

stack = []

for _ in range(n):
  num = stack.append(int(input()))
  
stick = 1
height = stack.pop()

for _ in range(len(stack)):
  n = stack.pop()
  if n > height:
    stick += 1
    height = n

print(stick)