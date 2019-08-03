# -*- coding: utf-8 -*-

import random
import time

raffle_timer = 3
current_raffle_timer = raffle_timer
participants = []   
participant_no = int(input("Çekiliş için katılımcı sayısını giriniz: "))

for participant in range(0, participant_no):
    name = str(input('Katılımcı ismini giriniz: '))
    name = '"{0}"'.format(name)
    participants.append(name)

while current_raffle_timer > 0:
    time.sleep(1)
    print("Çekilişin başlamasına {0} saniye!".format(current_raffle_timer))
    current_raffle_timer-=1

time.sleep(1)
print("\nÇekiliş başladı...\n")
time.sleep(2)

winner = random.choice(participants)
print("Kazanan oyuncu: {0} Tebrikler!!!\n".format(winner))

def chooseWinner(list):
    return random.choice(list)

def shuffleList(list):
    random.shuffle(list)

def main():
    #shuffleList(participants)
    chooseWinner(participants)

if __name__ == "__main__":
    main()