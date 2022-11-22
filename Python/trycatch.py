#runtime exception ve compile exceptime

#hata yakalama
#handled exception

try:
    examNote=float(input("Lütfen sınav notunu giriniz:"))
    print(examNote)
except ValueError:
    print("deneme")
except ZeroDivisionError:
    print("Hiç bir sayı sıfıra bölünemez")
except:
    print("Doğru bir değer girmediniz")
finally:
    print("Try/except bloğu çalıştı.")

