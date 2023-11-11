count = int(input())
show = 0
namecount = [0 for _ in range(26)]
for i in range(count):
    name = input()
    namecount[ord(name[0])-97]+=1
for j in range(26):
    if namecount[j]>=5:
        print(chr(j+97),end="")
        show = 1
if show == 0:
    print('PREDAJA')