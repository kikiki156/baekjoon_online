number = 0
while(True):
    diameter,rotation,time = map(float,input().split())
    if rotation == 0:
        break
    number += 1
    distance = diameter*3.1415927*rotation/5280/12
    speed = distance / time * 3600
    print(f"Trip #{number}: {distance:.2f} {speed:.2f}")
#inch feet mile, sec min hour 단위를 잘 구분하자