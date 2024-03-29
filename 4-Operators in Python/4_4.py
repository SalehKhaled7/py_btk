# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input("enter 1st number: "))
# b = int(input("enter 2st number: "))

# print(f"{a} > {b} :{a>b} ")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# visa1 = int(input("visa 1: "))
# visa2 = int(input("visa 2: "))
# final = int(input("final : "))

# avg = (visa1*0.3 + visa2*0.3) + (final*0.4)
# avg = ((visa1 + visa2)/2)*0.6 + (final*0.4)
# result = (avg >= 50)

# print(f"your average is :{avg} \npassed:{result}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# number = int(input("Enter a number: "))
# print("number is Odd :",(number % 2) != 0)
# print("number is Even :",(number % 2) == 0)


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# number = int(input("Enter a number: "))
# print("number is positive :",number > 0)
# print("number is negative :",number < 0)
# print("number is zero :",number == 0)

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)
email ,passward = "email@sadikturan.com", "abc123"
emailFromUser = input("Enter your email: ")
passwardFromUser = input("Enter your passward: ")

emailMatch = emailFromUser.lower().strip() == email
passMatch = passwardFromUser.lower() == passward

print(f"Email match: {emailMatch} \nPassward match: {passMatch}")