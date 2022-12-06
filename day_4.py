# part one
file = open("inputs\day_4_input.txt")
input = file.read().splitlines()

sums = 0
for i in input:
    a, b = i.split(',')
    a = a.split('-')
    b = b.split('-')
    a0, a1 = [int(j) for j in a]
    b0, b1 = [int(j) for j in b]
    
    if a0 <= b0 and a1 >= b1:
        sums += 1
    elif b0 <= a0 and b1 >= a1:
        sums += 1

print(sums)

# part two
sums = 0
for i in input:
    a, b = i.split(',')
    a = a.split('-')
    b = b.split('-')
    a0, a1 = [int(j) for j in a]
    b0, b1 = [int(j) for j in b]
    
    if a0 <= b1 and b0 <= a1:
        sums += 1

print(sums)