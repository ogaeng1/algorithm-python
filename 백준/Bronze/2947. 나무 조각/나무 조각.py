tree_slice = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(tree_slice)-1):
        if tree_slice[i] > tree_slice[i+1]:
            tree_slice[i], tree_slice[i+1] = tree_slice[i+1], tree_slice[i]
            print(" ".join(map(str, tree_slice)))

    if tree_slice == answer:
        break