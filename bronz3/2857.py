ans = []
for i in range(1,6):
    a = input()
    if 'FBI' in a:
        ans.append(i)
if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    for k in range(len(ans)):
        print(ans[k], end = " ")