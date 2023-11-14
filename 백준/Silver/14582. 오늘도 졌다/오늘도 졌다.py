ulim = list(map(int, input().split()))
start_link = list(map(int, input().split()))

ulim_score, start_link_score = 0, 0
lead = False

for i in range(9):
    ulim_score += ulim[i]
    if ulim_score > start_link_score:
        lead = True
    start_link_score += start_link[i]

if ulim_score < start_link_score and lead == True:
    print("Yes")
else:
    print("No")