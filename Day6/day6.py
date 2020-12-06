f = open('input.txt', 'r')

contents = f.read().split('\n\n')

counts = 0
common_count = 0

for i in contents:
    ans = []
    text = (i.split('\n'))
    text = [k for k in text if k]
    
    text_joined=''.join(text)
    items = set(text_joined)
    check = 0
    for k in items:
        check = 0
        for n in text:
            if k in n:
                check+=1
        if check==len(text):
            common_count+=1

    counts+=len(set(text_joined))
print('Part 1:',counts)
print('Part 2:',common_count)

