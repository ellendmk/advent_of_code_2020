import numpy as np

f = open('input.txt')
contents = f.read().split('\n')

# 128 rows
# 8 columns
# ID = row*8 + col

def get_element(upper, lower, boarding_pass):
    seat = 0
    for i in range(len(boarding_pass)):
        c = boarding_pass[i]
        if i==len(boarding_pass):
            if c=='F' or c=='L':
                seat = lower
            else:
                seat = upper
            break
        if c=='F' or c=='L':
            upper = int(upper-((upper-lower+1)/2))
            seat = upper
        else:
            lower = int(lower + ((upper-lower+1)/2))
            seat = lower
    return seat

def get_seat(boarding_pass):
    row = get_element(128,0,boarding_pass[0:7])
    col = get_element(7,0,boarding_pass[7:])

    return(row,col,row*8+col)

seats=np.zeros((128,8))

answers = []
count = 0
all_bids = []
for item in contents:
    if len(item)>7:
        r,c,bid = get_seat(item)
        seats[r,c] = 1
        all_bids.append(bid)
        
# Find my seat
for i in range(seats.shape[0]):
    for j in range(seats.shape[1]):
        if seats[i,j]==0:
            curr_bid = i*8+j
            if (curr_bid-1 in all_bids) and (curr_bid+1 in all_bids):
                print('row:',i,'col:',j)
                print('Possible ID:',curr_bid)