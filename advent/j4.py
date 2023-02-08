from termcolor import colored

lines = open("j4.txt", "r").read().splitlines()

sum = 0
for i in range(len(lines)):
    shift = lines[i].split(',')
    w1 = shift[0].split('-')
    a = int(w1[0])
    b = int(w1[1])
    w2 = shift[1].split('-')
    c = int(w2[0])
    d = int(w2[1])
    if ((a <= c) & (b >= d)):
        sum += 1
        print("w1 contient")
    elif ((a >= c) & (b <= d)):
        sum += 1
        print("w2 cotient")
    if (a <= c <= b):
        sum +=1
        print(colored("next good", 'green'))
    elif (c <= b <= d):
        sum +=1
        print(colored("next good", 'blue'))
    elif (c <= a <= d):
        sum +=1
        print(colored("next good", 'red'))       
    else: 
        print(a, b, c, d)
print(sum)    
