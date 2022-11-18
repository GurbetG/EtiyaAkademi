file=open("employees.txt","a")
while True:
    try:
        employeeCount=int(input("Çalışan sayısı giriniz:"))
    except ValueError:
        print("Hatalı giriş yaptınız. Sadece sayı giriniz.")
    else:
        break

for i in range(0,employeeCount):
    try:
        name=str(input(f"{i+1}. çalışanın adını giriniz:"))
        surname=str(input(f"{i+1}. çalışanın soyadını giriniz:"))
        count=float(input(f"{i+1}. çalışanın maaşını giriniz:"))
        file.write((f"\n{name} {surname} - {count}")) 
    except:
        print("hatalı giriş yaptınız.")
   
file.close()

file1=open("employees.txt","r")
lines=file1.readlines()
for i in lines:
    print(i)
   
file1.close()







