file=open("sample.txt","a")
# "w" dosyayı yazmaya açtık write
#"a" üzerine ekleme mevcutu tutar append
#"r" read dosyayı okumaya izin veriri.
#birden fazla kullanmak için 
file.write("\nhello world aaaa")

print(file.read())
file.close()

#pair ödevi
#dosyada şirket çalışanlarının bilgileri tutulaacak
#kullancıdan çalışan saysı alınacak
#çalışan sayısı kadar isim soyisim maaş bilgisi alınacak
#dosyadaki her satıra "Ad Soyad- Maaş" kalıbında çalışan bilgiler
#try except kullanılacak

