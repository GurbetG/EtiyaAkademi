print("vize Notunuzu giriniz")
vizeNotu=float(input())
print("final Notunuzu giriniz")
finalNotu=float(input())

ortalamanot=vizeNotu*0.4 + finalNotu*0.6
print(ortalamanot)

if ortalamanot <50 and ortalamanot>0:
    print("FF ile kaldınız")
elif ortalamanot>=50 and ortalamanot<60:
    print("DD ile geçtiniz")
elif ortalamanot>=60 and ortalamanot<70:
    print("CC ile geçtiniz")
elif ortalamanot>=70 and ortalamanot<80:
    print("BB ile geçtiniz")
elif ortalamanot>=80 and ortalamanot>=100:
    print("AA ile geçtiniz")
else: 
    print(f"Sınava girmediniz notunuz:{ortalamanot}")

