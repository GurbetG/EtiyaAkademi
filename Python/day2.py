#kullanıcıdan girdi alma
#userInput=input()
#print(f"Girilen değer: {userInput}")

#type conversion
numberStr="10"
#print(type(numberStr))
number=int(numberStr)

#print(number+10)
#print(type(number))

userInput=input()
lessonNote=int(userInput)
print(f"Ders notunuz: {lessonNote}")

#indent

#conditonal
if lessonNote >50:
    print("Geçtiniz")
print("kaldınız")

if lessonNote>50:
    print("geçtiniz")
else:
    print("kaldınız")

if lessonNote>50:
    print("geçtiniz")
elif lessonNote==50:
    print("sınırda geçtiniz")
elif lessonNote==49:
    print("sınırda kaldınız")
else:
    print("kaldınız")

#kulanıcıdan vize ve fianl notları al
#vize %40 final %60
#değer double olbabilir
#0-49 FF, 50-60 DD, 60-70 CC ,70-80 BB, 80-100 AA
#not ortalaması ve harf gdeğeri yazdır




