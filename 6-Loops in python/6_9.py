'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''
number = int(input("enter a number : "))

isPrime = True
if number == 1:
    isPrime = False

for x in range(2,number):
    if number % x == 0 :
        isPrime = False
        break

if isPrime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")