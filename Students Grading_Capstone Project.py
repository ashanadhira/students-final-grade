studentReports={
    '19001':{
        'name':'Aliyyah',
        'homework': 90,
        'midTest':85,
        'finTest':90,
    },
    '19002':{
        'name':'Fara',
        'homework': 95,
        'midTest':85,
        'finTest':90,
    },
    '19003':{
        'name':'Raina',
        'homework': 90,
        'midTest':95,
        'finTest':85,
    },
    '19004':{
        'name':'Ian',
        'homework': 90,
        'midTest':90,
        'finTest':95,
    },
    '19005':{
        'name':'Brian',
        'homework': 95,
        'midTest':80,
        'finTest':80,
    }
}

def displayMenu():
    print("\nMenu:")
    print("1. See all data")
    print("2. Add students data")
    print("3. Erase students data")
    print("4. Change student grades")
    print("5. Exit")

def averageStudent(hw,mid,fin):
    totalGrade=hw+mid+fin
    averageGrade=round((totalGrade/3),2)
    return averageGrade

def subSee():
    print(f"\nCHECK STUDENT'S DATA\n1. See all data\n2. See specific student's data\n3. Exit to main menu")
    seeData()

def seeData():
    checkData=int(input("\nWhich data would you like to see? "))
    if checkData==1:
        seeAllData()
        subSee()
    elif checkData==2:
        seeOneData()
        subSee()
    elif checkData==3:
        return
    else:
        print("\nChoose a valid number between 1-3")

def seeAllData():
    print(f"\nSTUDENTS:")
    for nis, data in studentReports.items():
        print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")

def seeOneData():
    chooseStudent=input("\nEnter student's NIS you'd like to see: ")
    for nis, data in studentReports.items():
        if nis==chooseStudent:
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")
            break
    else:
        print("\nStudent's data not found")

def subAdd():
    print(f"\nADD STUDENT'S DATA\n1. Add new data\n2. Exit to main menu")
    addMenu=int(input("\nPlease enter your preferred menu: "))
    if addMenu==1:
        addData()
    elif addMenu==2:
        return

def addData():
    nisAdd=input("\nEnter NIS: ")
    for nis in studentReports:
        if nis==nisAdd:
            print(f"\nStudent's NIS already existed")
            subAdd()
            break
    else:
        nameAdd=input("Enter name: ")
        homeworkAdd=int(input("Enter homework grade: "))
        midAdd=int(input("Enter mid test grade: "))
        finAdd=int(input("Enter final test grade: "))
        saveNewData=input("\nWould you like to save the data? (Y/N): ")
        if saveNewData=='Y':
            studentReports[nisAdd]={'name':nameAdd,'homework':homeworkAdd,'midTest':midAdd,'finTest':finAdd}
            print(f"\nData successfully saved")
            subAdd()
        else:
            print(f"\nData is not saved")
            subAdd()

def subErase():
    print(f"\nERASE DATA MENU:\n1. Erase student's data\n2. Exit to main menu")
    eraseMenu=int(input("Choose your preferred menu (1-2): "))
    if eraseMenu==1:
        eraseData()
    elif eraseMenu==2:
        displayMenu()

def eraseData():
    studentErase=input("\nEnter student's NIS you'd like to erase: ")
    for nis, data in studentReports.items():
        if nis==studentErase:
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}\n")
            eraseConfirm=input("Are you sure you want to delete this data? (Y/N): ")
            if eraseConfirm=='Y':
                studentReports.pop(nis)
                print(f"Student data {studentErase} has been successfully deleted")
                subErase()
                break
            else:
                print(f"Student's data is not deleted")
                subErase()
                break
    else:
        print(f"Student's data not found")
        subErase()

def subChange():
    print(f"\nCHANGE DATA:\n1. Student's name\n2. Student's homework grade\n3. Student's mid test grade\n4. Student's final test grade\n5. Exit to main menu")
    dataChange=int(input("What data would you like to edit? "))
    if dataChange==1:
        changeName()
    elif dataChange==2:
        changeHomework()
    elif dataChange==3:
        changeMidGrade()
    elif dataChange==4:
        changeFinGrade()
    elif dataChange==5:
        return
    else:
        print(f"Choose only number 1-4")
        subChange()

def changeName():
    editName=input(f"Enter student's NIS you'd like to edit: ")
    for nis, data in studentReports.items():
        if nis==editName:
            print(f"\nPrevious Name: {data['name']}")
            newName=input(f"Enter updated student's name: ")
            data['name']=newName
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")
            subChange()
            break
    else:
        print(f"Student's data not found")
        subChange()

def changeHomework():
    editHomework=input(f"Enter student's NIS you'd like to edit: ")
    for nis, data in studentReports.items():
        if nis==editHomework:
            print(f"\nPrevious score: {data['homework']}")
            newHomeGrade=int(input(f"Enter updated student's grade: "))
            data['homework']=newHomeGrade
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")
            subChange()
            break
    else:
        print(f"Student's data not found")
        subChange()

def changeMidGrade():
    editMidGrade=input(f"\nEnter student's NIS you'd like to edit: ")
    for nis, data in studentReports.items():
        if nis==editMidGrade:
            print(f"\nPrevious score: {data['midTest']}")
            newMidGrade=int(input(f"Enter updated student's grade: "))
            data['midTest']=newMidGrade
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")
            subChange()
            break
    else:
        print(f"Student's data not found")
        subChange()

def changeFinGrade():
    editFinGrade=input(f"Enter student's NIS you'd like to edit: ")
    for nis, data in studentReports.items():
        if nis==editFinGrade:
            print(f"\nPrevious score: {data['finTest']}")
            newFinGrade=int(input(f"Enter updated student's grade: "))
            data['finTest']=newFinGrade
            print(f"\nNIS: {nis}\nNAME: {data['name']}\nHomework Grade: {data['homework']}\nMid Test: {data['midTest']}\nFinal Test: {data['finTest']}\nAverage: {averageStudent(data['homework'],data['midTest'],data['finTest'])}")
            subChange()
            break
    else:
        print(f"Student's data not found")
        subChange()

def main():
    while True:
        displayMenu()
        chooseMain=int(input("Please choose your preferred menu: "))
        if chooseMain==1:
            subSee()
        elif chooseMain==2:
            subAdd()
        elif chooseMain==3:
            subErase()
        elif chooseMain==4:
            subChange()
        elif chooseMain==5:
            print(f"Thank you for using this program")
            break
        else:
            print(f"Choose number 1-5")
            main()

if __name__ == "__main__":
    main()
