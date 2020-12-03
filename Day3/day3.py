import numpy as np

f = open('input.txt')

contents = f.readlines()

arr = np.zeros((len(contents),len(contents[0])))-1

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j]=='#':
            arr[i,j] = 2
        elif contents[i][j]=='.':
            arr[i,j] = 0



def get_counts(right, down):
    row = 0
    col = 0
    tree_count = 0
    while row < len(contents):
        if arr[row,col] == 2:
            tree_count += 1
        row+=down
        col+=right
        if col >= len(contents[0]):
            col = col-len(contents[0])
        if row>=len(contents):
            break
    return (tree_count)
        

counts = []

for r,d in zip([1,3,5,7,1],[1,1,1,1,2]):
    counts.append(get_counts(r,d))
    
print(counts)

prod = 1

for i in counts:
    prod *= i
    
print(prod)
