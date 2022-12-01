# part one
file = open("inputs\day_1_input.txt")
input = file.read().splitlines()

a = 0
sums = list()
for i in input:
    if i == "":
        sums.append(a)
        a = 0
    else:
        a += int(i)

print(max(sums))


# part two
print(sum(sorted(sums, reverse=True)[0:3]))