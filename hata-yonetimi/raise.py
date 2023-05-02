import re

""" 
def check_password(psw):
    
    if len(psw) < 9:
        raise Exception("Parola en az 8 karkter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola kücük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola sayı içermelidir.")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alfa numeric karkter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Paralo geçerli")
    
password = "123456789aA$";

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("gecerli parola : else")
finally:
    print("validation gecerli")
"""

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanın fazla karakter içeriyor.")
        else:
            self.name = name

Person("Aliiiiiiiiiiiiii",1950)