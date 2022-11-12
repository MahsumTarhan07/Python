from random import randint
rand = randint(1,55)

sayac = 0

while True:
    sayac +=1
    sayi = int(input("1 İle 55 arasında deger girin(0 cıkış)"))

    if(sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    else:
        print("Rastegele secilen sayı {0}!". format(rand))
        print("Tahmin sayınız {0}".format(sayac))