n=int(input("Введите количество минут"))
hours=24
minuts=00

k=n//60
t=n%60
hours-=k
minuts-=t
if minuts<0:
    hours-=1
    minuts=60
    minuts-=t
if hours<0:
    hours=0
    minuts=0
print( f"Время {hours}:{minuts}" )