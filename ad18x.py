f = open("C:/Users/nikol/OneDrive/Desktop/Adventofcode/input.txt")
lines = f.readlines()
coordinates = []
temp = []
xmax = 70
for x in range(xmax+3):
    temp.append('#')
coordinates.append(temp) 
for y in range(xmax+1):
    temp = ['#']
    for x in range(xmax+1):
        temp.append('.')
    temp.append('#')
    coordinates.append(temp)
temp = []
for x in range(xmax+3):
    temp.append('#')
coordinates.append(temp) 

drops = []
for line in lines:
    if '\n' in line:
        line = line[:-1]
    temp = line.split(',')
    drops.append((int(temp[0]),int(temp[1])))
print(drops)
for a in range(2524):
    (x,y) = drops.pop(0)
    coordinates[y+1][x+1] = '#'
for y in range(len(coordinates)):
    sun = ""
    for x in coordinates[y]:
        sun += x
    print(sun)

for y in range(len(coordinates)):
    sun = ""
    for x in coordinates[y]:
        sun += x
    print(sun)

stack = [(1,1,0)]
costs = []
for y in range(len(coordinates)):
    temp = []
    for x in coordinates[y]:
        temp.append(100000000)
    costs.append(temp)
costs[1][1] = 0

while stack !=[]:
    (x,y,cost) = stack.pop()
    if coordinates[y][x+1] == '.':
        if costs[y][x+1] > cost+1:
            costs[y][x+1] = cost + 1
            stack.append((x+1,y,cost + 1))
    if coordinates[y][x-1] == '.':
        if costs[y][x-1] > cost+1:
                costs[y][x-1] = cost + 1
                stack.append((x-1,y,cost + 1))
    if coordinates[y+1][x] == '.':
        if costs[y+1][x] > cost+1:
                costs[y+1][x] = cost + 1
                stack.append((x,y+1,cost + 1))
    if coordinates[y-1][x] == '.':
        if costs[y-1][x] > cost+1:
                costs[y-1][x] = cost + 1
                stack.append((x,y-1,cost + 1))

stack = [(xmax+1,xmax+1, costs[xmax+1][xmax+1])]
#while stack != []:
 #   (x,y,cost) = stack.pop()
  #  if costs[y][x+1] == cost-1:
   #     coordinates[y][x+1] = 'O'
    #    stack.append((x+1,y,cost - 1))
 #   elif costs[y][x-1] == cost-1:
#        coordinates[y][x-1] = 'O'
 #       costs[y][x-1] = cost + 1
  #      stack.append((x-1,y,cost - 1))
   # elif costs[y+1][x] == cost-1:
#        coordinates[y+1][x] = 'O'
#        costs[y+1][x] = cost + 1
#        stack.append((x,y+1,cost - 1))
#    elif costs[y-1][x] == cost-1:
#        coordinates[y-1][x] = 'O'
#        stack.append((x,y-1,cost - 1))

for y in coordinates:
    sun = ""
    for x in y:
        sun += x
    print(sun)
print(costs[xmax+1][xmax+1])
nx = 0
ny = 0
i = 0
while costs[xmax+1][xmax+1] != 100000000:
    i += 1
    (nx,ny) = drops.pop(0)
    coordinates[ny+1][nx+1] = '#'
    costs = []
    for y in range(len(coordinates)):
        temp = []
        for x in coordinates[y]:
            temp.append(100000000)
        costs.append(temp)
    costs[1][1] = 0
    stack = [(1,1,0)]
    while stack !=[]:
        (x,y,cost) = stack.pop()
        if coordinates[y][x+1] == '.':
            if costs[y][x+1] > cost+1:
                costs[y][x+1] = cost + 1
                stack.append((x+1,y,cost + 1))
        if coordinates[y][x-1] == '.':
            if costs[y][x-1] > cost+1:
                    costs[y][x-1] = cost + 1
                    stack.append((x-1,y,cost + 1))
        if coordinates[y+1][x] == '.':
            if costs[y+1][x] > cost+1:
                    costs[y+1][x] = cost + 1
                    stack.append((x,y+1,cost + 1))
        if coordinates[y-1][x] == '.':
            if costs[y-1][x] > cost+1:
                    costs[y-1][x] = cost + 1
                    stack.append((x,y-1,cost + 1))

    print(i)
for y in range(len(coordinates)):
    sun = ""
    for x in coordinates[y]:
        sun += x
    print(sun)

stack = [(1,1,0)]
while stack != []:
    (x,y,cost) = stack.pop()
    if costs[y][x+1] == cost+1:
        coordinates[y][x+1] = 'O'
        stack.append((x+1,y,cost + 1))
    if costs[y][x-1] == cost+1:
        coordinates[y][x-1] = 'O'
        stack.append((x-1,y,cost + 1))
    if costs[y+1][x] == cost-1:
        coordinates[y+1][x] = 'O'
        stack.append((x,y+1,cost + 1))
    if costs[y-1][x] == cost-1:
        coordinates[y-1][x] = 'O'
        stack.append((x,y-1,cost + 1))

for y in range(len(coordinates)):
    sun = ""
    for x in coordinates[y]:
        sun += x
    print(sun)

print((nx,ny))
print()
    



