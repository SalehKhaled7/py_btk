website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result =len(course)
# 2- 'website' içinden www karakterlerini alın.
result= website[7:10]

# 3- 'website' içinden com karakterlerini alın.
result= website[-3:len(website)]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result =course[0:15]
result = course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]

name, surname, age, job = 'Bora','Yılmaz', 32, 'engineer' 
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 

result = "my name is " + name + " " +surname+", my age is "+str(age)+" and i am an "+ job
result = "my name is {0}  {1}, my age is {2} and i am an {3} ".format(name,surname,age,job)
result = f"my name is {name} {surname}, my age is {age} and i am an {job}"

#print("my name is",name,surname,", my age is ",age," and i am an ",job)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s ="hello world"
result = s[:6]+"W"+s[-4:]

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.


result = "abs " * 3
print(result)