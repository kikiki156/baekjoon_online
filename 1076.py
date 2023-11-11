dica = {'black':(0,1),'brown':(1,10),'red':(2,100),'orange':(3,1000),'yellow':(4,10000),'green':(5,100000),
          'blue':(6,1000000),'violet':(7,10000000),'grey':(8,100000000),'white':(9,1000000000)}
a = input()
b = input()
c = input()
print((dica[a][0]*10+dica[b][0])*dica[c][1])
'''dicb = ['black','borwn','red','orange','yellow','green','blue','violet','grey','white']
x = str(dicb.index(input()))
y = str(dicb.index(input()))
z = str(10**dicb.index(input()))
print(int(x+y+z[1:]))'''