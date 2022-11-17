#Bölüm Ödevi1
number1=40
number2=10

if number1>number2:
    print(number1)
else:
    print(number2)

if number1>number2:
    print(number1)
elif number2>number1:
    print(number2)
else:
    print("sayılar eşittir")

#Bölüm Ödevi 2

sayi1=3
sayi2=4
sayi3=7

#En Büyük olan sayı

if sayi1>sayi2 and sayi1>sayi3:
    print(sayi1)
elif sayi2> sayi1 and sayi2>sayi3:
    print(sayi2)
elif sayi3>sayi1 and sayi3>sayi1:
    print(sayi3)
else:
    print("Sayılar eşittir.")

#En Küçük olan sayı

if sayi1 < sayi2 and sayi1 < sayi3:
    print(sayi1)
elif sayi2 < sayi1 and sayi2 < sayi3:
    print(sayi2)
elif sayi3<sayi1 and sayi3<sayi1:
    print(sayi3)
else:
    print("Sayılar eşittir.")


#Bölüm Ödevi 3

oncekiGumusFiyati=12.6639
bugunkiGumusFiyati=12.6603

if oncekiGumusFiyati>bugunkiGumusFiyati:
    print("↓")
elif oncekiGumusFiyati< bugunkiGumusFiyati:
    print("↑")
else:
    print("=")


     