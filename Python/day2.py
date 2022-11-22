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

#döngüler

for i in range(6):
    print(i)

students= ["Nilüfer","özlem","Berk","Zakir"]
for i in students:
    print(i)

i=0
while 1<10:
    print(i)
    i+=1







