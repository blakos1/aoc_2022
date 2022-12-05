# part one
file = open("inputs\day_3_input.txt")
input = file.read().splitlines()

import string
alphabet = list(string.ascii_letters)
priorities = list(range(1,53))
mydict = dict(zip(alphabet, priorities))

sums = 0
for i in input:
    rucksack1 = slice(0, len(i)//2)
    rucksack2 = slice(len(i)//2, len(i))
    common_characters = ''.join(
        set(i[rucksack1]).intersection(i[rucksack2])
    )
    sums += mydict[common_characters]

print(sums)

# part two
sums = 0
for i in range(0,len(input),3):
    common = ''.join(
        set(input[i]).intersection(input[i+1], input[i+2])
    )
    sums += mydict[common]

print(sums)