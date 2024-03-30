
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# number = int(input("Enter a number :"))
# condition = (number > 0) and (number < 100)
# print(f"{number} between 0 and 100 :{condition}")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# number = int(input("Enter a number :"))
# condition = (number > 0) and (number % 2 == 0)
# print(f"{number} is positive and Even :{condition}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = 'email@sadikturan.com'
# password = 'abc123'
# emailFromUser = input("Enter the email :")
# passwardFromUser = input("Enter the passward :")
 
# auth = (emailFromUser.lower().strip() == email) and (passwardFromUser.strip() == password)
# print("User can login :",auth)

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# print(f'a:{a} is the greatest number :{a > b and a > c}')
# print(f'a:{b} is the greatest number :{b > a and b > c}')
# print(f'a:{c} is the greatest number :{c > a and c > b}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# visa1 = int(input("visa 1: "))
# visa2 = int(input("visa 2: "))
# final = int(input("final : "))

# # avg = (visa1*0.3 + visa2*0.3) + (final*0.4)
# avg = ((visa1 + visa2)/2)*0.6 + (final*0.4)

# condition_1 = avg >= 50
# condition_2 = final >= 50
# condition_3 = final >= 70

# studentPass = (condition_1 and condition_2) or condition_3
# print("result".ljust(10,'-'))
# print(f"visa 1: {visa1} \nvisa 2: {visa2} \nfinal: {final} \navg: {avg} \npassed: {studentPass}")
# print("-"*10)


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
print(f"-->skinny: {(index > 0) and (index < 18.4)}")
print(f"-->Normal: {(index > 18.5) and (index < 24.9)}")
print(f"-->fat: {(index > 25.0) and (index < 29.9)}")
print(f"-->obes: {(index > 30.0) and (index < 34.9)}")

