# -*- coding: utf-8 -*-

import random
import time

count = 0

while True:
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)

    count += 1
    
    if zar1 == 6 and zar2 == 6:
        print("{0}.Tur".format(count))
        print("Sonuç: {0} - {1}".format(zar1, zar2))
        print("OYUN BİTTİ!! {0}. turda iki zar da 6 geldi!".format(count))
        break
     
    print("{0}.Tur".format(count))
    print("Sonuç: {0} - {1}".format(zar1, zar2) + "\n")
    time.sleep(1)


