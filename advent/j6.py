lines = open("j6.txt", 'r').read()
x = 14
for i in range(len(lines)):
    if (len(set(lines[i:i+14])) == 14):
        print(x)
        break
    x += 1