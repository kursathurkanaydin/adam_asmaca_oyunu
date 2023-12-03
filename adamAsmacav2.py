from random import randint
from fonksiyonlar import*
wordsList=list()
with open("words.txt","r",encoding="utf-8")as dosya:
    words=dosya.readlines()
    for word in words:
        word=word.replace("\n","")
        wordsList.append(word)
while True:
    can=7
    print("*****************\nADAM ASMACA OYUNU\n*****************")
    print("Kelimeyi tahmin etmek istiyorsanız q tuşuna basınız ve tahmininizi giriniz")
    print("Pes etmek için x tuşuna basınız")
    number=randint(0,len(wordsList))
    kelime=wordsList[number].lower()
    height=uzunluk(kelime)
    kelime2=kelime
    kelime2list=kelime_listesi(kelime2)
    tahmin=replace_etme(kelime)
    #print(tahmin)
    tahmin_list=kelime_listesi(tahmin)
    while(can>0):
        print(f"Kalan Can: {can}")
        print(f"TAHMİN: {tahmin}")
        harf=input("HARF GİRİNİZ: ")
        harf=harf.lower()
        if(harf=="q"):
            break
        if(harf=="x"):
            print("Pes Ettiniz...")
            print("KELİME: {}".format(kelime))
            break
        elif(harf in kelime2):
            while True:
                if(tahmin==kelime):
                    print(f"Tebrikler Kelimeyi Bildiniz\nKelime: {tahmin}")
                    can=-1
                    break
                elif(harf in kelime2):
                    sayı=kelime2.index(harf)
                    kelime2list=kelime_degistirme(kelime2list,sayı,"*")
                    tahmin_list=kelime_degistirme(tahmin_list,sayı,harf)
                    tahmin=kelime_üretme(tahmin_list)
                    kelime2=kelime_üretme(kelime2list)
                else:
                    break
        else:
            can-=1
    if harf=="q":  
        break
    