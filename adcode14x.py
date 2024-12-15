f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
q = open("C:/Users/nikol/Downloads/shit54532.txt", 'w')
little = f.readlines()
robots = []
time = 100
x_max = 101
y_max = 103
one = 0
two = 0
three = 0
four = 0
x_middle = (x_max//2)+1
y_middle = (y_max//2)+1
424 
527
12

473
574
69
for time in range(12,10000,103):
    q.write(str(time) + '\n')

    robots = []
    for line in little:
        if '\n' in line:
            line = line[:-1]
        a = line.split(' ')
        xp = int(a[0].split('=')[1].split(',')[0])
        yp = int(a[0].split('=')[1].split(',')[1])
        xv = int(a[1].split('=')[1].split(',')[0])
        yv = int(a[1].split('=')[1].split(',')[1])
        new_xp = (xp + xv*time)%x_max
        new_yp = (yp + yv*time)%y_max

        if new_xp < (x_max//2) and new_yp < (y_max//2):
            one += 1
        elif new_xp < (x_max//2) and new_yp > (y_max//2):
            two += 1
        elif new_xp > (x_max//2) and new_yp < (y_max//2):
            three += 1
        elif new_xp > (x_max//2) and new_yp > (y_max//2):
            four += 1
        robots.append((new_xp,new_yp))
    grid = []
    for y in range(y_max):
        grid.append([])
        for x in range(x_max):
            grid[y].append(' ')

    
    for (x,y) in robots:
        grid[y][x] = '#'

    for y in range(y_max):
        lin = ""
        for x in range(x_max):
            lin = lin + grid[y][x]
        q.write(lin + '\n')


