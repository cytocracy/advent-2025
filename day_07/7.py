with open('day_07/7.txt', 'r') as file:
     data = file.read()
     
data = data.split('\n')

split = 0
timelines = 1

memo = {}

def count_timelines(r,c):
    if (r, c) in memo:
        return memo[(r, c)]
    if r == len(data)-1:
        return 1
    below = data[r+1][c]
    if below == '.':
        ret = count_timelines(r+1, c)
        memo[(r, c)] = ret
        return ret
    elif below == '^':
        # print('split at', r, c)
        return count_timelines(r+1, c-1) + count_timelines(r+1, c+1)

    else:
        return 0

timelines = count_timelines(0, data[0].index('S'))

for r in range(len(data)-1):
    # print(data[r])
    for c in range(len(data[0])):
        if data[r][c] == 'S':
            data[r+1] = data[r+1][:c] + '|' + data[r+1][c+1:]
        elif data[r][c] == '|':
            # print('pipe at', r, c)
            below = data[r+1][c]
            if below == '.':
                data[r+1] = data[r+1][:c] + '|' + data[r+1][c+1:]
            elif below == '^':
                data[r+1] = data[r+1][:c-1] + '|^|' + data[r+1][c+2:] 
                split += 1
                # timelines *= 2
                
                
print(split)
print(timelines)