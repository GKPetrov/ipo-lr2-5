n=int(input("Введите количество минут"))
hours=00
minuts=00
n=n%(24*60)
hours=n//60
minuts=n%60
print( f"Время {hours}:{minuts}" )
