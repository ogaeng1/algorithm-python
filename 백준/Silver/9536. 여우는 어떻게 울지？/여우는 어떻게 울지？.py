t = int(input())

for _ in range(t):
  crying_sound = list(input().split())
  
  while True:
    animal_info = list(input().split())

    if animal_info[-1] == 'say?':
      break

    while animal_info[2] in crying_sound:
      crying_sound.pop(crying_sound.index(animal_info[2]))

  print(' '.join(crying_sound))