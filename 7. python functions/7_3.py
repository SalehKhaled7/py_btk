# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 
print("\n#question 1")
def reapeat(name = 'user' ,times = 1):
    for a in range(times):
        print(name)

reapeat('sal',4)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
print("\n#question 2")
def makeList(*parms):
    list = []
    for parm in parms:
        list.append(parm)
    
    return list
myList = makeList(1,3,6,9,9,9,9,9,9,'hello',2.13,True)
print(myList)



# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
print("\n#question 3")
def findPrimes(number1 , number2):

    #start from 1
    if number1 <= 0:
        number1 = 1

    for number in range(number1 ,number2+1):
        isPrime = True
        if number == 1:
            pass
        else:
            for y in range(2,number):
                if (number % y)== 0 :
                    isPrime = False
    
        if isPrime:
            print(number)



findPrimes(-51,7)
        



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def factors(number):
    list = []
    for x in range(1,number):
        if number % x == 0:
            list.append(x)

    return list



print(factors(500))