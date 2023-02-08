lines = open("j2.txt", "r").read().splitlines()
sum = 0

## A rock B paper C Scissor X rock Y paper Z scissor
score = {
    'A Y': 4,
    'A X': 3,
    'A Z': 8,
    'B Y': 5,
    'B X': 1,
    'B Z': 9,
    'C Y': 6,
    'C X': 2,
    'C Z': 7,
}

choix = {
    'A Y': 'X',
    'A X': 'Z',
    'A Z': 'Y',
    'B Y': 'Y',
    'B X': 'X',
    'B Z': 'Z',
    'C Y': 'Z',
    'C X': 'Y',
    'C Z': 'X',
}

'''
for i in range(len(lines)):
    add = 0
    data = lines[i].split(' ')
    if (data[1] == "X"):
        add += 1
        if (data[0] == "A"):
            add += 3
        elif (data[0] == "C"):
            add += 6
    elif (data[1] == "Y"):
        add += 2
        if (data[0] == "A"):
            add += 6
        elif (data[0] == "B"):
            add += 3
    elif (data[1] == "Z"):
        add += 3
        if (data[0] == "B"):
            add += 6
        elif (data[0] == "C"):
            add += 3
    print(f"{i} : {lines[i]} et add : {add}")
    sum += add
'''

res = dict((v,k) for k,v in choix.items())
for i in range(len(lines)):
    print(score[lines[i]])
    sum += score[lines[i]]
    
print(f"{sum}")