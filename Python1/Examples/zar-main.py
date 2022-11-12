
import random
import time
"""
    Bir zar oyunu yaptık eğer 6 == 6 eşitlensen oyun otomatik olark oyunu bitiriyor
"""
i = 1

while True:
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)

    if zar1 == 6 and zar2 == 6:
        print("Deneme {}:\t({}, {})".format(i, zar1,zar2))
        time.sleep(2)
        break
    print("""Deneme {}:\t({},{}) """.format(i, zar1, zar2))
    i +=1
    time.sleep(0.5)
print("""\n*** {}. denemede (6,6) geldi ***""".format(i))