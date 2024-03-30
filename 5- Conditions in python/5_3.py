# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

# name = input("your name :")
# age = int(input("your age :"))
# education = input("Education level :")

# if age >= 18 :
#     if (education == "lisa" or "university"):
#         print("you are Eligible to apply for driver licence")
#     else:
#         print("you need to finish \"secondary education\" or \"univerisy\" to apply for driver licence")
# else:
#     print("your most be 18 or older")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# written1 = int(input("written exam 1 result :"))
# written2 = int(input("written exam 2 result :"))
# verbal   = int(input("verbal exam result :"))

# avg = (written1 + written2 + verbal) / 3

# if avg >= 0 and avg <= 24 :
#     print(f"your avg is {avg} | 0/5")
# elif avg >= 25 and avg <= 44 :
#     print(f"your avg is {avg} | 1/5")
# elif avg >= 45 and avg <= 54 :
#     print(f"your avg is {avg} | 2/5")
# elif avg >= 55 and avg <= 69 :
#     print(f"your avg is {avg} | 3/5")
# elif avg >= 70 and avg <= 84 :
#     print(f"your avg is {avg} | 4/5")
# elif avg >= 85 and avg <= 100 :
#     print(f"your avg is {avg} | 4/5")
# else  :
#     print("please enter a valid exam results")





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün


import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print('1.servis aralığı')
elif days>365 and days<=365*2:
    print('2.servis aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')