
"""
try:
    x = int(input("x :"))
    y = int(input("y :"))
    print (x/y)
except (ZeroDivisionError,ValueError) as e: #kısa yolu
    print("Yanlış değer girdiniz");
    print(f"hata mesajı : {e}");
    
except ZeroDivisionError:
    print("y icin 0 girilemez") 
except ValueError:
    print("x ve y icin sayısal değer girmelisiniz")"""
    
""" 
try:
    x = int(input("x :"))
    y = int(input("y :"))
    print (x/y)
except:
    print("Yanlış bilgi girdininz");
else:
    print("Hersey yolunda");
"""

while True:
    try:
        x = int(input("x :"))
        y = int(input("y :"))
        print (x/y)
    except Exception as error:
        print("Yanlış bilgi girdiniz.", error)
    else:
        break
    finally:
        print("try except sonlandı.")
    