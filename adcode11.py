f = open("C:/Users/nikol/Downloads/adcode1.txt", 'r')
import time
start_time = time.time()
thing = 75
line = f.readline().split(' ')
number = []
numbers_present = []
numbersdict = {}
new_dict = {}
for num in line:
    number.append(int(num))

for num in number:
    numbersdict.update({num:1})

for n in range(int(thing)):
    new_dict = {}
    for key in numbersdict:
        if key == 0:
            if new_dict.get(1) == None:
                new_dict.update({1: numbersdict[0]})
            else:
                new_dict.update({1: numbersdict[0] + new_dict[1]})

        elif len(str(key))%2 == 0:
            half = len(str(key))//2
            a = int(str(key)[(len(str(key))- half):])
            b = int(str(key)[:half])
            if new_dict.get(a) == None:
                new_dict.update({a: numbersdict[key]})
            else:
                new_dict.update({a: numbersdict[key] + new_dict[a]})
            
            if new_dict.get(b) == None:
                new_dict.update({b: numbersdict[key]})
            else:
                new_dict.update({b: numbersdict[key] + new_dict[b]})
            
        else:
            q = key * 2024
            if new_dict.get(q) == None:
                new_dict.update({q: numbersdict[key]})
            else:
                new_dict.update({q: numbersdict[key] + new_dict[q]})
    numbersdict = new_dict.copy()            
sum = 0
for key in numbersdict:
    sum += numbersdict[key]
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))