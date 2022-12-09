# part one
file = open("inputs\day_5_input.txt")
input = file.read().splitlines()

cratestate = input[:8]

mainlist = list()
for i in range(1,len(cratestate[0]),4):
    sublist = list()
    for j in reversed(range(0,len(cratestate))):
        if input[j][i] != ' ':
            sublist.append(input[j][i])

    mainlist.append(sublist)

insctructions = input[10:]
for i in insctructions:
    i = i.replace('move ','').replace('from ','').replace('to ','').split()
    i = [int(j) for j in i]
    
    numcrates = i[0]
    colfrom = i[1]-1
    colto = i[2]-1

    itemstoadd = mainlist[colfrom][-numcrates:]
    destination = mainlist[colto]
    destination.extend(reversed(itemstoadd))
    del mainlist[colfrom][-numcrates:]

last = list()
for i in mainlist:
    last.append(i[len(i)-1])

print(''.join(last))


# part two
mainlist = list()
for i in range(1,len(cratestate[0]),4):
    sublist = list()
    for j in reversed(range(0,len(cratestate))):
        if input[j][i] != ' ':
            sublist.append(input[j][i])

    mainlist.append(sublist)

insctructions = input[10:]
for i in insctructions:
    i = i.replace('move ','').replace('from ','').replace('to ','').split()
    i = [int(j) for j in i]
    
    numcrates = i[0]
    colfrom = i[1]-1
    colto = i[2]-1

    itemstoadd = mainlist[colfrom][-numcrates:]
    destination = mainlist[colto]
    destination.extend(itemstoadd)
    del mainlist[colfrom][-numcrates:]

last = list()
for i in mainlist:
    last.append(i[len(i)-1])

print(''.join(last))