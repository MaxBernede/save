import string
from termcolor import colored

lines = open("j3.txt", 'r').read().splitlines()
mid = 0
sum = 0
for i in range(0,len(lines),3):
    l1 = lines[i]
    l2 = lines[i+1]
    l3 = lines[i+2]
    char = ''.join(set(l1).intersection(l2).intersection(l3))
    print(colored(char, 'green'))
    letter = '0'
    x = 0
    # mid = len(lines[i]) / 2
    # first = lines[i][0:int(mid)]
    # second = lines[i][int(mid):len(lines[i])]
    # char = ''.join(set(first).intersection(second))
    for letter in string.ascii_letters:
        x += 1
        if (letter == char):
            sum += x
            break
    print(sum)
    