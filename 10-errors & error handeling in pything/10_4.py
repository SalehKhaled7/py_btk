import re
listA = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for item in listA:
#     try:
#         int(item)
#         print(item)
#     except:
#         continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True :
#     x = input('enter a number : ')
#     if x == 'q':
#         print("ended by user")
#         break
        
#     try:
#         num = int(x)  
#         print("you entered :",num)      
#         break
#     except:
#         print("invalid number !")
#         continue




# 3: Girilen parola içinde türkçe karakter hatası veriniz.

# def checkPassword(psw):
#     turkishSpeacialChars = "şçğöüıİ"
#     for l in psw:
#         if l in turkishSpeacialChars:
#             raise Exception("password can contain speacial charectersZ \"şçğüöıİ\"")
#         else:
#             pass

# password= input("enter you password : ")
# try:
#     checkPassword(password)
#     print("check passed")
# except Exception as e :
#     print(e)

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

import re
def factorial(num):
    total = 1
    num = int(num)
    if num < 0 :
        raise Exception("negative number")
    else:
        x = num
        while x > 0 :
            total *= x
            x -= 1
    
    return f"factorial of {num} is {total}"
        
# while True:
for x in [5, 10, 20, -3, '10a']:
    try:
        #x = input("entre a numebr : ")
        print(factorial(x))
        
    except Exception as e :
        print("wrong input :",e)
        #continue