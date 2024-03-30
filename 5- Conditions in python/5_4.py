
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# number = float(input("enter a numbr :"))

# if number > 0 and number <= 100 :
#     print(f"{number} is between 0 - 100")
# else:
#     print(f"{number} is not between 0 - 100")




# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.


# number = float(input("enter a numbr :"))

# if number > 0:
#     if number %2 == 0:
#         print(f"{number} is poszitive and Even")
#     else:
#         print(f"{number} positive but odd" )
# elif number == 0:
#     print(f"{number} is zero")
# else:
#     print(f"{number} negative")




# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

# email = 'salkal@gmail.com'
# password = '123456'

# emailFromUser = input('email: ')
# passwordFromUser = input('password: ')

# if emailFromUser == email:
#     if passwordFromUser == password:
#         print("welcome back")
#     else:
#         print("passward is wrong")
# else:
#     print("please enter a valid email")


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# print(f"numbers a:{a} ,b:{b} ,c:{c}")
# if a > b and a > c:
#     print(f"a:{a} is the greatest number")
# if b > a and b > c:
#     print(f"b:{b} is the greatest number")
# if c > a and c > b:
#     print(f"c:{c} is the greatest number")




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# midterm1    = float(input('midterm 1: '))
# midterm2    = float(input('midterm 2: '))
# final       = float(input('final : '))

# avg = ((midterm1 + midterm2)/2) * 0.6 + final * 0.4

# if final >= 70:
#     print("you have passed !")
# elif avg >= 50:
#     if final >=50 :
#         print(f"avg:{avg} you have passed !")
#     else:
#         print(f"avg:{avg} final bellow 50 !you have failed !")
# elif (avg > 100) or (avg < 0):
#     print("please enter a valid grades")
# else:
#     print(f"avg:{avg}  ,you have faild !!")



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)




name = input('your name: ')
kg = float(input('your weight: '))
hg = int(input('yout length (CM): '))

index = (kg) / ((hg/100)**2) #hg / 100 m-> cm
print(f"{name} ({kg}kg ,{hg}hg |index:{index})")


if (index > 0) and (index < 18.4):
    print("skinny")
elif (index > 18.5) and (index < 24.9):
    print("normal")
elif (index > 25.0) and (index < 29.9):
    print("fat")
elif (index > 30.0) and (index < 34.9):
    print("obes")
else:
    print("please enter valid data")

