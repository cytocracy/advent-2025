with open('day_05/5data.txt', 'r') as file:
     data = file.read()
     
data = data.split('\n')

ranges = set()

answer = 0


def in_range(num, ranges):
    for r in ranges:
        if r[0] <= num <= r[1]:
            return True, r
    return False, None

def does_overlap(r1, r2):
    return not (r1[1] < r2[0] or r2[1] < r1[0])


def add_range(start, end, ranges):
    new_range = (start, end)
    to_remove = []
    for r in ranges:
        if does_overlap(r, new_range):
            new_range = (min(r[0], new_range[0]), max(r[1], new_range[1]))
            to_remove.append(r)
    for r in to_remove:
        ranges.remove(r)
    ranges.add(new_range)
    

for line in data:
    if '-' in line:
        start, end = line.split('-')
        add_range(int(start), int(end), ranges)
        # print(ranges)
        
    elif len(line) > 0:
        num = int(line)
        if in_range(num, ranges):
            answer += 1
            
            
answer2 = 0
for r in ranges:
    answer2 += r[1] - r[0] + 1
            
print(answer)
print(answer2)