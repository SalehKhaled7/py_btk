# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars =["Bmw", "Mercedes", "Opel", "Mazda"]
result = cars

# 2-  Liste Kaç elemanlıdır ?
result = len(cars)

# 3-  Listenin ilk ve son elemanı nedir ?
result = "first: "+cars[0] +"\nlast: "+cars[-1]

# 4-  Mazda değerini Toyota ile değiştirin.
cars[3] ="Toyota"
result = cars

# 5-  Mercedes listenin bir elemanı mıdır ?
result ="Mercedes" in cars

# 6-  Listenin -2 indeksindeki değer nedir ?
result = cars[-2]

# 7-  Listenin ilk 3 elemanını alın.
result = cars[0:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
cars[-2] = "Totoya"
cars[-1] = "Renault"
#cars[-2:] = ["Totoya" ,"Renault"]
result = cars

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
cars  += ["Audi" , "Nissan"]
result = cars
# 10- Listenin son elemanını silin.
del cars[-1] # del(cars[-1])
result = cars

# 11- Liste elemanlarını tersten yazdırınız.
result = cars[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 
student1 = ["Yiğit","Bilgi", 2010 ,[70,60,70]]
student2 = ["Sena","Turan", 1999 ,[80,80,70]]
student3 = ["Ahmet","Bilgi", 1998 ,[80,70,90]]

students = [student1,student2,student3]
result = students


# 13- Liste elemanlarını ekrana yazdırınız.
result = f"student: {student1[0]} {student1[1]}, age:{2024-student1[2]}, grade:{(student1[3][0] + student1[3][1] + student1[3][2])/3}"
result = f"student: {student2[0]} {student2[1]}, age:{2024-student2[2]}, grade:{(student2[3][0] + student2[3][1] + student2[3][2])/3}"
result = f"student: {student3[0]} {student3[1]}, age:{2024-student3[2]}, grade:{(student3[3][0] + student3[3][1] + student3[3][2])/3}"

print(result)
