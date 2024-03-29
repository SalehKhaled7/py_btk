website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
s =' Hello World '
result = s.strip()

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = website.strip('htp/:')

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.upper()
result = course.lower()
result = course.title()
result = course.capitalize()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
doesStartsWith = website.startswith('www')
doesEndsWith = website.endswith('com')
result=f"start:{doesStartsWith} \nend:{doesEndsWith}"

# 6-  'website' içinde '.com' ifadesi var mı?

result = website.rindex('.com') #if true it returns the index
#result = website.rindex('comm') #if false it returns an exception

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isdigit()
result = course.isalpha()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*')
result = 'Contents'.ljust(50, '*')
result = 'Contents'.rjust(50, '*')

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ','-')

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'hello World'.replace('World','There')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')



print(result)   