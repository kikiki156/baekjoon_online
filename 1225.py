al,bl = list(map(str,input().split()))
suma,sumb=0,0
for i in al:
    suma += int(i)
for j in bl:
    sumb += int(j)
print(suma*sumb)