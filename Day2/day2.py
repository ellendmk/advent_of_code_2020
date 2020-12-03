import numpy as np
import pandas as pd
from itertools import combinations

f = open('input.txt')
contents  = f.readlines()

def check_valid_count(pwd, limits, char):
    count = 0
    for i in pwd:
        if i==char:
            count+=1
    if(count>=limits[0]) and (count<=limits[1]):
        return True
    return False


def check_valid_pos(pwd, limits, char):
    count = 0
    if(pwd[limits[0]-1]==char):
        count +=1
    if (limits[1]-1)<=len(pwd):
        if (pwd[limits[1]-1]==char):
            count+=1
    if count ==1:
        return True
    return False

valid = []
for case in contents:
    pieces = case.split(' ')
    limits = pieces[0].split('-')
    limits = [int(x) for x in limits]
    char = pieces[1].strip(':')
    pwd = pieces[2]

    valid.append(check_valid_pos(pwd, limits, char))

print(sum(valid))