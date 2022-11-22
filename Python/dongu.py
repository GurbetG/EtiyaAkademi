notlar=[]

for i in range(10):
    sayi=int(input("Bir not giriniz: "))
    notlar.append(sayi)
print(notlar)

gecenNot=0
kalanNot=0

for i in notlar:
    if notlar[i]>=50:
        gecenNot=gecenNot+1
    else:
        kalanNot=kalanNot+1

print(f"{gecenNot} dersten geçtiniz. {kalanNot} dersten kaldınız.")