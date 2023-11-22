import fonksiyonlar
import os
print("*****************\nADAM ASMACA OYUNU\n*****************")
kelime=input("Kelimenizi Giriniz: ")
os.system('cls')
kelime=kelime.lower()
kelime_list=fonksiyonlar.kelime_listesi(kelime)
can=7
tahmin=str()
uzunluk=fonksiyonlar.uzunluk(kelime)
deger=("_"*uzunluk)
deger_list=fonksiyonlar.kelime_listesi(deger)
print("Kelimeyi tahmin etmek istiyorsanız q tuşuna basınız ve tahmininizi giriniz")
print("Pes etmek için x tuşuna basınız")
while(can>0):
    tahmin=fonksiyonlar.kelime_üretme(deger_list)
    kelime2=kelime
    kelime2_list=list(fonksiyonlar.kelime_listesi(kelime2))
    print(f"Kalan Can Sayısı: {can}")
    print(f"TAHMİNİZ: {tahmin}")
    harf=input("\nHarf Giriniz: ")
    harf.lower()
    if(harf=="q"):
        tahmin2=input("Tahmininiz: ")
        if(tahmin2==kelime2):
            print(f"Tebrikler tahmininiz doğru\nKelime: {kelime}")
            break
        else:
            print("Tahmininiz Yanlış...")
            can-=1
    elif (harf in kelime):
        while True:
            if(tahmin==kelime):
                print(f"Tebrikler tahmininiz doğru.\nKelime: {kelime}")
                can=-1
                break
            elif(harf in kelime2):
                number=kelime2_list.index(harf)
                deger_list=fonksiyonlar.kelime_degistirme(deger_list,number,harf)
                kelime2_list=fonksiyonlar.kelime_degistirme(kelime2_list,number,"*")
                kelime2=fonksiyonlar.kelime_üretme(kelime2_list)
                tahmin=fonksiyonlar.kelime_üretme(deger_list)
                
            else:
                break
    else:
        can-=1
if(can==0):
    print("Kaybettiniz...")
    print(f"Kelime: {kelime}")