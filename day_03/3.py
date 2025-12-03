with open('day_03/3data.py', 'r') as file:
     data = file.read()
     
data = data.split('\n')

data = [x for x in data if x]

count = 0
count2 = 0

def find_max(num, num_on):
    # print(f"find_max({num}, {num_on})")
    if num_on == 0:
        return ''
    if len(num) == num_on:
        return num
    num_possible_first_digits = len(num) - num_on + 1
    max_d = 0
    max_pos = -1
    for d in range(num_possible_first_digits):
        # print(d)
        if int(num[d]) > max_d:
            max_d = int(num[d])
            max_pos = d
    return str(max_d) + find_max(num[max_pos+1:], num_on-1)
            
            

for num in data:
    max_val = 0
    for first in range(len(num)-1):
        for second in range(first+1, len(num)):
            joltage = int(num[first] + num[second])
            if joltage > max_val:
                max_val = joltage
                
    count2 += int(find_max(num, 12))
    count += max_val
    
    

    

    
print(count)
print(count2)