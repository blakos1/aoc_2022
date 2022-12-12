# part one
file = open("inputs\day_6_input.txt")
input = file.read().splitlines()

text = input[0]

for i in range(0, len(text)):
    a = text[i:i+4]
    if len(a) == len(set(a)):
        print(i+4, a)
        break

# part two
for i in range(0, len(text)):
    a = text[i:i+14]
    if len(a) == len(set(a)):
        print(i+14, a)
        break