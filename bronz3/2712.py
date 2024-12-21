num = int(input())
for i in range(num):
    a, measure = input().split()
    if measure == 'kg':
        print(format(round(float(a)*2.2046,4),".4f"), "lb")
    elif measure == 'lb':
        print(format(round(float(a)*0.4536,4),".4f"), "kg")
    elif measure == 'l':
        print((format(round(float(a)*0.2642,4),".4f")), "g")
    elif measure == 'g':
        print(format(round(float(a)*3.7854,4),".4f"), "l")