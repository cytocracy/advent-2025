with open('day_06/6.txt', 'r') as file:
     data = file.read()
     
data = data.split('\n')
data = [line.split() for line in data]
data = [[line[i] for line in data] for i in range(len(data[0]))]

answer = 0
answer2 = 0

def compute(nums, operation):
    if operation == '+':
        return sum(nums)
    elif operation == '*':
        result = 1
        for n in nums:
            result *= n
        return result
    else:
        return None
    
def column_wise(line):
    got_number = True
    index = 0
    column_line = []
    while got_number:
        string = ''
        got_number = False
        for num in line:
            if index < len(num):
                string += num[index]
                got_number = True
        index += 1
        if got_number:
            column_line.append(string)
    return column_line

for line in data:
    operation = line[-1]
    columns = column_wise(line[:-1])
    nums = [int(x) for x in line[:-1]]
    nums2 = [int(x) for x in columns]
    print(nums2)
    result = compute(nums, operation)
    result2 = compute(nums2, operation)
    
    answer += result
    answer2 += result2
    

print(data)
print(answer)
print(answer2)

