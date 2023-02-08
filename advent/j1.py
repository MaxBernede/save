lines = open("j1.txt", "r").read().splitlines()
x = 0
max = 0
max2 = 0
max3 = 0
while (lines):
    sum = 0
    temp = 0
    while (lines[x]):
        sum += int(lines[x])
        x += 1
    if (sum > max):
        temp = max
        max = sum
        sum = max2
        max2 = temp
        max3 = sum
    elif (sum > max2):
        temp = max2
        max2 = sum
        max3 = temp
    elif (sum > max3):
        max3 = sum
    print(f"max {max} max2 {max2} max3 {max3}")
    print(f"{max + max2 + max3}")
    x += 1
print("END")