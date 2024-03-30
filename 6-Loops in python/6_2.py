numbers = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
# for n in numbers:
#     if (n % 3 == 0):
#         print(n)


# 2- Sayilar listesinde sayıların toplamı kaçtır ?
# sum = 0
# for n in numbers:
#     sum += n
# print("total is :",sum)

# 3- Sayilar listesindeki tek sayıların karesini alınız.
# for n in numbers:
#     if (n % 2 == 1):
#         print(n,"-->",n**2)


# cities = ['kocaeli','istanbul','ankara','izmir','rize']
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
# for city in cities:
#     if len(city) <= 5:
#         print(city)


products = [
    {'name':'samsung S20', 'price': '3000' },
    {'name':'samsung S21', 'price': '4000' },
    {'name':'samsung S22', 'price': '5000' },
    {'name':'samsung S23', 'price': '6000' },
    {'name':'samsung S24', 'price': '7000' }
]
# 5- Ürünlerin fiyatları toplamı nedir ?
# total = 0
# for product in products:
#     total += int(product["price"])
# print(total)


# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for product in products:
    if int(product["price"]) <= 5000:
        print(product["name"],"-->",product["price"])
