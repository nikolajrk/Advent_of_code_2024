f = open("C:/Users/nikol/OneDrive/Desktop/Adventofcode/input.txt")
lines = f.readlines()
equation = []
sum = 0
for line in lines:
    if '\n' in line:
        line = line[:-1]
    
    equation = line.split(' ')

    equation[0] = equation[0][:-1]
    stack = [(int(equation[1]), equation[2:], int(equation[0]))]
    print(stack)
    shit = True
    while shit and stack != []:
        (val, things,ori) = stack.pop(0)
        if (len(things) == 0):
            if val == ori:
                sum += ori
                shit = False
        else:
            first = int(things[0])
            if(val * first <= ori):
                stack.append((val*first, things[1:],ori))
            if(val + first <= ori):
                stack.append((val + first, things[1:], ori))
            if (val % 1 == 0) and (int(str(val) + str(first)) <= ori):
                stack.append((int(str(val) + str(first)), things[1:], ori))
print(sum)


