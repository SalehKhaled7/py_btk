def calculateAvg(examsResults):

    exam1 = float(examsResults[0])
    exam2 = float(examsResults[1])
    exam3 = float(examsResults[2])
    avg = (exam1+exam2+exam3)/3

    if (avg >= 90) and (avg <= 100):
        return "(AA)"
    elif  (avg >=85) and (avg <= 89) :
        return "(BA)"
    elif  (avg >=80) and (avg <= 84) :
        return "(BB)"
    elif  (avg >=75) and (avg <= 79) :
        return "(CB)"
    elif  (avg >=70) and (avg <= 74) :
        return "(CC)"
    elif  (avg >=65) and (avg <= 69) :
        return "(DC)"
    elif  (avg >=60) and (avg <= 64) :
        return "(DD)"
    elif  (avg >=50) and (avg <= 59) :
        return "(FD)"
    else :
        return "(FF)"

def readRecords():
    with open("records.txt","r") as file:
        for line in file:
            fullName = getStudentName(line)
            examList = getStudentExams(line)
            print(fullName,calculateAvg(examList))
    
    print("\n")

            




def addNewRecord():
    with open("records.txt","a",encoding="utf-8") as file:
        name  = input("student name :")
        surname  = input("student surname :")
        while True:
            try:
                exam1  = float(input("exam 1 :"))
                break
            except:
                print("invalid imput\n")
        while True:
            try:
                exam2  = float(input("exam 2 :"))
                break
            except:
                print("invalid imput\n")
        
        while True:
            try:
                exam3  = float(input("exam 2 :"))
                break
            except:
                print("invalid imput\n")

        file.write(f"\n{name} {surname}:{exam1},{exam2},{exam3}")
    


def getStudentName(line):
    record = line.split(":")
    return record[0]

def getStudentExams(line):
    record = line.split(":")
    examsResults = record[1].split(",")
    return examsResults

def saveResults():
    records =[]
    with open("records.txt","r") as file:
        for line in file:
            fullName = getStudentName(line)
            examList = getStudentExams(line)
            avg = calculateAvg(examList)
            record = fullName+" "+str(avg)
            records.append(record)

    with open("results.txt","w",encoding="utf-8") as file : 
        for record in records:
            file.write(record+"\n")

    print("records saved to results.txt")
        


records =[]
while True:
    process = input("please select an operation :\n1-read the records \n2-add new record \n3-save to a file \n4-quit\n")
    if process == "1":
        readRecords()

    elif process == "2":
        addNewRecord()
        

    elif process == "3":
        saveResults()

    elif process == "4":
        break

    else:
        print("invalid input please puck 1 ,2 ,3 or 4 \n")
        continue