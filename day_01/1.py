#read from 1data.py
with open('day_01/1data.py', 'r') as file:
     data = file.read()

data = data.split('\n')
data = [(x[0], int(x[1:])) for x in data if x]

curr = 50

nums = [y[1] if y[0] == 'R' else -y[1] for y in data]

count = 0
count2 = 0
for rotation in nums:
    before = curr
    curr = (curr + rotation) % 100
    
    for _ in range(abs(rotation)):
        add = 1 if rotation > 0 else -1
        before = (before + add) % 100
        if before == 0: count2 += 1
    
    
    
    # if before + rotation < 0:
        # count2 += (abs(before + rotation) // 100) + 1
    # else: count2 += abs(before + rotation) // 100 + (1 if before + rotation == 0 else 0)
    
        
   

    # print(before, rotation, curr, count2)
    
    if curr == 0:
        count += 1
        
        
        
print(count)
print(count2)