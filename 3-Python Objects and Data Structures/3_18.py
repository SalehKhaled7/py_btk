'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}


1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
    
'''



students = {}
studentNumber = input('student Number :')
studentFirstName = input('student First Name :')
studentLastName = input('student Last Name :')
studentPhoneNumber = input('student Phone Number :')
students[studentNumber]={'ad': studentFirstName,
                         'soyad': studentLastName,
                         'telefon': studentPhoneNumber
                        }

studentNumber = input('student Number :')
studentFirstName = input('student First Name :')
studentLastName = input('student Last Name :')
studentPhoneNumber = input('student Phone Number :')

# you cant use update()
# update() allow to add more than one object at the same time
students.update({
    studentNumber: {
        'ad': studentFirstName,
        'soyad': studentLastName,
        'telefon':studentPhoneNumber 
    }
   
})

studentNumber = input('student Number :')
studentFirstName = input('student First Name :')
studentLastName = input('student Last Name :')
studentPhoneNumber = input('student Phone Number :')
students[studentNumber]={'ad': studentFirstName,
                         'soyad': studentLastName,
                         'telefon': studentPhoneNumber
                        }

print(students)



studentNumber = input('Enter student number :')
student = students[studentNumber]

print('#'*50)
print(f"Name: {student['ad']}\nsurename: {student['soyad']}\nPhone: {student['telefon']}")