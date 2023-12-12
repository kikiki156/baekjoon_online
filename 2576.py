list = []
oddlist = []
sum = 0
for i in range(7):
    list.append(int(input()))
list.sort()
for i in list:
    if i % 2 == 1:
        oddlist.append(i)
        sum += i
if  len(oddlist) == 0:
    print('-1')
else:
    print(sum)
    print(oddlist[0])