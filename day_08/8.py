import math
with open('day_08/8.txt', 'r') as file:
     data = file.read()
     
lines = data.split('\n')

distances = []

def straight_dist(coord1, coord2):
     return math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2 + (coord1[2]-coord2[2])**2)

lines = [line.split(',') for line in lines]
lines = [[int(coord) for coord in line] for line in lines]

circuits = {i: set([i]) for i in range(len(lines))}

circuit_names = {i: i for i in range(len(lines))}

for r in range(len(lines)):
     for r2 in range(r+1,len(lines)):
          if r != r2:
               distance = straight_dist(lines[r], lines[r2])
               distances.append((distance, r, r2, lines[r][0], lines[r2][0]))
               
               
distances = sorted(distances, key=lambda x: x[0])


for distance in distances:
     
     circuit1_name = circuit_names[distance[1]]
     circuit2_name = circuit_names[distance[2]]     
     
     circuit1 = circuits[circuit1_name]
     circuit2 = circuits[circuit2_name]
     
     if circuit1 is not circuit2:
          
          circuits[circuit2_name] = None     
          combined = circuit1.union(circuit2)
          combined.add(distance[1])
          combined.add(distance[2])
          circuits[circuit1_name] = combined
          
     for member in circuit2:
          circuit_names[member] = circuit1_name

     if len([x for x in circuits.values() if x is not None]) == 1:
          print(distance[3] * distance[4])
          break

print(circuits)
sizes = [len(circuit) for circuit in circuits.values() if circuit is not None]
sorted_sizes = sorted(sizes, reverse=True)
three_largest = sorted_sizes[:3]
product = 1
for size in three_largest:
     product *= size
print(product)