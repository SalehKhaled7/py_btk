#numbers = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
# x = 0
# while x < len(numbers):
#     print(numbers[x])
#     x += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

# a = int(input("enter 1st number :"))
# b = int(input("enter 2nd number :"))
# x = a
# while x <= b :
#     if x % 2 == 1:
#         print(x)
#     x +=1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# x = 100
# while x > 0:
#     print(x)
#     x -= 1


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

# numbers = []
# x = 0
# while x < 5 :
#     number =int(input("enter a number:"))
#     numbers.append(number)
#     x += 1

# numbers.sort()
# print(numbers)


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


products=[]

productNUmber = int(input("how many products you want to add ?"))
x = 0
while x < productNUmber:
    name = input("product name:")
    price = int(input("product name:"))
    products.append({"name":name ,"price":price})
    x += 1



#with while loop
i = 0
while i < productNUmber:
    print(products[i]["name"],"->",products[i]["price"])
    i += 1

#with for loop
for product in products:
    print(product["name"],"->",product["price"])