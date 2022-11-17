#kullanıcı gireceği ders sayısını belirtecek

lessonCount=int(input("Kaç adet ders notu gireceksiniz"))

#girilen ders sayısı kadar vize ve final notu giriniz
passedExams=0
failedExam=0
for i in range(lessonCount):
    lessonExam1=float(input(f"{i+1}. ders için vize notu giriniz"))
    lessonExam2=float(input(f"{i+1}. ders için vize notu giriniz"))
    totalEzamNote=(lessonExam1*0.4)+(lessonExam2*0.6)
    if totalEzamNote >=50:
        passedExams+=1
    else:
        failedExam+=1
print(f"{passedExams} adet dersten geçtiniz. {failedExam} adet dersten kaldınız")