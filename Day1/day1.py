import numpy as np
import pandas as pd
from itertools import combinations

contents = np.genfromtxt('input.txt', delimiter = '\n')

def get_list_to_sum(num_list, target, n):
    vals = combinations(contents,3)
    for k in vals:
        if sum(k)==2020:
            prod = 1
            for i in k:
                prod*=i
            print(prod)
            break


print(get_list_to_sum(contents, 2020, 3))