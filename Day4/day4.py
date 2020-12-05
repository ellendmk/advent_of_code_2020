
def format_check(d):
    invalid_count = 0
    for k,v in d.items():
        if k=='byr':
            v = int(v)
            if v<1920 or v>2002:
                invalid_count+=1
        elif k=='iyr':
            v = int(v)
            if v <2010 or v>2020:
                invalid_count+=1
        elif k=='eyr':
            v = int(v)
            if v <2020 or v>2030:
                invalid_count+=1
        elif k=='hgt':
            if v[-2:]=='cm':
                hgt = int(v[0:-2])
                if hgt<150 or hgt>193:
                    invalid_count+=1
            elif v[-2:]=='in':
                hgt = int(v[0:-2])
                if hgt<59 or hgt>76:
                    invalid_count+=1
            else:
                invalid_count+=1
        elif k=='hcl':
            if v[0]=='#' and len(v)==7:
                allowed_chars = 'abcdef0123456789'
                for i in v[1:]:
                    if i not in allowed_chars:
                        invalid_count+=1
            else:
                invalid_count+=1
        elif k=='ecl':
            if v not in ['amb','blu','brn','gry','grn','hzl','oth'] or len(v)!=3:
                invalid_count+=1
        elif k=='pid':
            if len(v.strip(' '))==9:
                for i in v:
                    if i not in '0123456789':
                        invalid_count+=1
            else:
                invalid_count+=1

        if invalid_count>0:
            return 0
    return 1

def is_valid(details):
    curr_counts = 0
    for k in fields:
        if k in details.keys():
            curr_counts+=1
    if curr_counts==7:
        if format_check(details)==1:
            return True
        return False
    else:
        return False

f = open('input.txt')
contents = f.read()

contents = contents.split('\n\n')
contents = [ k.replace('\n',' ') for k in contents]

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

valids = []
all_dicts = []

# Split contents into dict
for val in contents:
    if len(val)>0:
        temp = val.split(' ')
        temp = [i for i in temp if i] 
        current_dict = {}
        for item in temp:
            k,v = item.split(':')
            current_dict[k] = v
        all_dicts.append(current_dict)
    
count = 0
for d in all_dicts:
    valids.append(is_valid(d))
    
print(sum(valids))
