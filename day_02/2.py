with open('day_02/2data.py', 'r') as file:
     data = file.read()

data = data.split(',')

answer = 0
answer2 = 0

ranges = [r.split('-') for r in data]
ranges = [(int(r[0]), int(r[1])) for r in ranges]

for r in ranges:
     for i in range(r[0], r[1]+1):
          str_num = str(i)
          length = len(str_num)
          
          for x in range(1, length//2 +1):
               if length % x != 0: continue
               valid = True
               part = str_num[:x]
               for start in range(x, length, x):
                    if str_num[start:start+x] != part:
                         valid = False
                         break
               if valid:
                    answer2 += i
                    break
          
          
          if length %2 == 1: continue
          half = length//2
          first_half = str_num[:half]
          second_half = str_num[half:]
          if first_half == second_half:
               answer += i

print(ranges)

print(answer)
print(answer2)