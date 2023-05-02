
#list = ["1","2","3","4","5a","10b","abc","10","50"]

#list içersindeki elamanların içindeki sayısal değeri bulma.

#for x in list:
#    try:
#        result = int(x)
#       print(result)
#    except ValueError:
#       continue    




#2 - kullanıcı 'q' değerinin girmedikce aldığınız her input sayı,olduğunda emin olup,olamadığında hata mesajı yazınız.

#while True:
#   sayi = input("sayı :")
#   if sayi == "q":
#       break
    
#    try:
#       result = float(sayi)
#        print("Gidiğiniz sayı :", result)
#   except ValueError:
#       print("Gecersiz sayı")
#        continue



# 3:Girilen parola içinde türkce karakter hatası ver

""" 
def chcekPassword(parola):
    turkce_karkter = "şçüğöIİ"

    for i in input:
        if i in turkce_karkter:
            raise TypeError("Parlola türkce karakter içermez.")
        else:
            pass
    print("parola geçerili")

parola = input("parola giriniz : ")

try:
    chcekPassword(parola)
except TypeError as error:
    print(error)
"""

#4- Faktöriyel fonksiyonu oluşturuo fonksiyona gelen değer icin hata mesajıları verme.

def faktoriyel(x):
    x = int(x)
    
    
    if x < 10:
        raise ValueError("Negatif değer")
    
    result = 1
    
    for i in range(1, x+1):
        result *=i
    return result

    
for  x in [5,10,20,-5,40,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
    
        
    