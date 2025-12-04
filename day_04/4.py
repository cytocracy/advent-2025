with open('day_04/4data.py', 'r') as file:
     data = file.read()
     
data = data.split('\n')
rows = len(data)
cols = len(data[0])

def get_cell(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return None
    return data[r][c]

def get_num_neighbors(r, c):
    count = 0
    if get_cell(r+1, c) == '@': count += 1
    if get_cell(r-1, c) == '@': count += 1
    if get_cell(r, c+1) == '@': count += 1
    if get_cell(r, c-1) == '@': count += 1
    if get_cell(r+1, c+1) == '@': count += 1
    if get_cell(r-1, c-1) == '@': count += 1
    if get_cell(r+1, c-1) == '@': count += 1
    if get_cell(r-1, c+1) == '@': count += 1
    return count
    
answer = 0

removed = True
while removed:
    removed = False

    for r in range(rows):
        for c in range(cols):
            if get_cell(r,c) == '@' and get_num_neighbors(r, c) < 4: 
                answer += 1
                data[r] = data[r][:c] + '.' + data[r][c+1:]
                removed = True
                
        
        
print(answer)
        
        
