
def kelime_listesi(word):
    liste=list()
    for i in word:
        liste.append(i)
    return liste
def kelime_degistirme(liste,index,harf):
    liste[index]=harf
    return liste
def kelime_üretme(liste):
    word=str()
    for x in liste:
        word=word+x
    return word
def uzunluk(word):
    sayi=len(word)
    return sayi
def index(liste,harf):
    liste=list()
    try:
        sayi=liste.index(harf)
        return sayi
    except:
        pass
def karakok(sayı):
    sayı=sayı**(1/2)
    return sayı
print(karakok(36))