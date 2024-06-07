import sys
input = sys.stdin.readline

def binary_search(coordinate, target):
  start, end = 0, N-1

  while start < end:
    mid = (start + end) // 2

    if coordinate[mid] == target:
      return mid
    elif target < coordinate[mid]:
      end = mid-1
    else:
      start = mid+1

  return start

N, M = map(int, input().split())
coordinate = sorted(map(int, input().split()))

for _ in range(M):
  s, e = map(int, input().split())
  start_index = binary_search(coordinate, s)
  end_index = binary_search(coordinate, e)

  res_s, res_e = 0, 0
  if coordinate[start_index] >= s:
    res_s = start_index
  else:
    start_index += 1

  if coordinate[end_index] <= e:
    res_e = end_index
  else:
    end_index -= 1

  print(end_index - start_index + 1)