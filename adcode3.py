f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')

sum = 0
i1 = 0
i2 = 0
check = False
do = True
while True:
    check = False
    t1 = f.read(1)
    num1 = 0
    num2 = 0
    if t1 == 'EOF' or t1 == '' :
        break
    if(t1) == 'd':
        t2 = f.read(1)
        if t2 == 'o':
            t3 = f.read(1)
            if(t3 == '('):
                 t4 = f.read(1)
                 if t4 == ')':
                    do = True
            elif t3 == 'n':
                
                t4 = f.read(1)
                if t4 == "'":
                    tz = f.read(1)
                    if tz == 't':
                        t5 = f.read(1)
                        if t5 == '(':
                            t6 = f.read(1)
                            if t6 == ')':
                                do = False
    if do:
        if(t1) == 'm':
            print(t1)
            t2 = f.read(1)
            if t2 == 'u':
                print(t1 + t2)
                t3 = f.read(1)
                if t3 == 'l':
                    print(t1 + t2 + t3)
                    t4 = f.read(1)
                    if t4 == '(':
                        i1 = f.read(1)
                        if i1 == '0' or i1 == '1' or i1 == '2' or i1 == '3' or i1 == '4' or i1 == '5' or i1 == '6' or i1 == '7' or i1 == '8' or i1 == '9':
                            i2 = f.read(1)
                            num1 = int(i1)
                            print(int(i1))
                            if i2 == '0' or i2 == '1' or i2 == '2' or i2 == '3' or i2 == '4' or i2 == '5' or i2 == '6' or i2 == '7' or i2 == '8' or i2 == '9':
                                num1 = num1 * 10 + int(i2)
                                i3 = f.read(1)
                                
                                if i3 == '0' or i3 == '1' or i3 == '2' or i3 == '3' or i3 == '4' or i3 == '5' or i3 == '6' or i3 == '7' or i3 == '8' or i3 == '9': 
                                    num1 = num1 * 10 + int(i3)
                                    t5 = f.read(1)
                                    
                                    if t5 == ',':
                                        check = True
                                elif i3 == ',':
                                    check = True
                            elif i2 == ',':
                                check = True
        num2 = num1
        num1 = 0
        if(check):
            i1 = f.read(1)
            if i1 == '0' or i1 == '1' or i1 == '2' or i1 == '3' or i1 == '4' or i1 == '5' or i1 == '6' or i1 == '7' or i1 == '8' or i1 == '9':
                i2 = f.read(1)
                num1 = num1 * 10 + int(i1)
                if i2 == '0' or i2 == '1' or i2 == '2' or i2 == '3' or i2 == '4' or i2 == '5' or i2 == '6' or i2 == '7' or i2 == '8' or i2 == '9':
                    num1 = num1 * 10 + int(i2)
                    i3 = f.read(1)

                    if i3 == '0' or i3 == '1' or i3 == '2' or i3 == '3' or i3 == '4' or i3 == '5' or i3 == '6' or i3 == '7' or i3 == '8' or i3 == '9': 
                        num1 = num1 * 10 + int(i3)
                        t5 = f.read(1)
                        if t5 == ')':
                            sum += num1 * num2
                    elif i3 == ')':
                            sum += num1 * num2
                elif i2 == ')':
                            sum += num1 * num2


print(sum)