n = input()
f = int(input())
sepn = int(n[:len(n)-2])*100%f
if sepn == 0:
    print("00")
elif f-sepn<10:
    print('0',f-sepn,sep="")
else:
    print(f-sepn)