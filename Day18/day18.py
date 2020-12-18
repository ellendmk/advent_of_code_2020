import copy

f = open('input.txt')
# f = open('test.txt')

sums = f.read().split('\n')

def calculate(nums, ops):
    result = nums[0]
    for i in range(len(nums)-1):
        if ops[i]=='*':
            result *= nums[i+1]
        elif ops[i] == '+':
            result += nums[i+1]
    return result

def extract_brackets(sum_str):
    locations_left = []
    location_pairs = []
    for i in range(len(sum_str)):
        if sum_str[i]=='(':
            locations_left.append(i)
        elif  sum_str[i]==')':
            location_pairs.append((locations_left[-1],i))
            locations_left = locations_left[0:-1]
    return location_pairs

def extract_nums_ops(sum_str):
    all_list = sum_str.split(' ')
    ops = []
    nums = []
    for k in all_list:
        if k=='*' or k=='+':
            ops.append(k)
        else:
            nums.append(int(k))
    return ops,nums

all_results = []

for k in sums:
    temp_k = k[:]

    brackets = extract_brackets(temp_k)
    while len(brackets)>0: 
        bracket_vals = []
        b = brackets[0]
        ops, nums = extract_nums_ops( temp_k[b[0]+1:b[1]])
        bracket_vals.append(calculate(nums, ops))
        temp_k = temp_k[0:b[0]] +str(bracket_vals[-1])+temp_k[b[1]+1:]
        brackets = extract_brackets(temp_k)

    ops,nums=extract_nums_ops(temp_k)
    result = calculate(nums, ops)
    all_results.append(result)

print('part 1', sum(all_results))
print()

def calculate_precedence(nums, ops):
    temp_ops = ops[:]
    while '+' in temp_ops:
        i=0
        while i < (len(nums)-1):
            if temp_ops[i]=='+':
                result = nums[i] + nums[i+1]
                temp_ops = temp_ops[:i]+temp_ops[i+1:]
                nums = nums[:i]+[result]+nums[i+2:]
                
            i+=1

    result = nums[0]
    for i in range(len(nums)-1):
        if temp_ops[i]=='*':
            result *= nums[i+1]
    print(result)
    return result


all_results = []

for k in sums:
    print(k)
    temp_k = k[:]

    brackets = extract_brackets(temp_k)
    while len(brackets)>0: 
        bracket_vals = []
        b = brackets[0]
        ops, nums = extract_nums_ops( temp_k[b[0]+1:b[1]])
        bracket_vals.append(calculate_precedence(nums, ops))
        temp_k = temp_k[0:b[0]] +str(bracket_vals[-1])+temp_k[b[1]+1:]
        brackets = extract_brackets(temp_k)

    ops,nums=extract_nums_ops(temp_k)
    result = calculate_precedence(nums, ops)
    all_results.append(result)

print('part 2', sum(all_results))