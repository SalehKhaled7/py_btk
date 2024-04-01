'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

import random


print("welcome to guess the number game")
print('*'*50)
print("you have 5 chaces to guess the number the number is between 1-10")
goal = random.randrange(0, 100)
totalattempts = int(input("how many attempts you want ?"))

attempts = totalattempts
while attempts > 0:
    attempts -= 1
    guess = int(input("your guess: "))
    if guess == goal:
        print(f"congradulation you win ")
        print(f"guessed in :{totalattempts-attempts}/{totalattempts}  | your points:{(100/totalattempts)*(attempts+1)}")
        break
    elif guess < goal:
        print(f"wrong guess try , guess higher number")
    elif guess > goal:
        print(f"wrong guess try , guess lower number")
        

    if attempts == 0 :
        print(f"you lost he game the numebr was:{goal}")
