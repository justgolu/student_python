database = [{
    "name": "a",
    "roll_no": "1",
    "addres": "aaa",
    "contact": "544",
    "city": "bbb",
    "standard": "2"
},
    {
    "name": "b",
        "roll_no": "2",
        "addres": "aaa",
        "contact": "544",
        "city": "bbb",
        "standard": "2"
},
    {
    "name": "c",
        "roll_no": "3",
        "addres": "aaa",
        "contact": "544",
        "city": "bbb",
        "standard": "2"
},
    {"name": "d",

        "roll_no": "4",
        "addres": "aaa",
        "contact": "544",
        "city": "bbb",
        "standard": "2"
     },
    {
        "name": "e",
        "roll_no": "5",
        "addres": "aaa",
        "contact": "544",
        "city": "bbb",
        "standard": "2"
}]


def add():
    global database
    student_d = {
        "name": None,
        "roll_no": None,
        "addres": None,
        "contact": None,
        "city": None,
        "standard": None
    }
    student_d["name"] = input("enter student name: ")
    student_d["roll_no"] = input("enter student roll_no: ")
    student_d["addres"] = input("enter student address: ")
    student_d["contact"] = input("enter student contact: ")
    student_d["city"] = input("enter student city: ")
    student_d["standard"] = input("enter student standard: ")
    database.append(student_d)


def showall():
    global database
    for stud in database:
        print(stud["name"])
        print(stud["roll_no"])
        print(stud["addres"])
        print(stud["contact"])
        print(stud["city"])
        print(stud["standard"])
        print("\n")


def search(rn):
    global database

    for elem in database:
        if(elem["roll_no"] == rn):
            return elem
    return "not found"


def delete(rn):
    for i in range(len(database)):
        if(database[i]["roll_no"] == rn):
            elem = database.pop(i)
            return rn
    return "not found"


def update(rm, No, name, addres, contact, city, standard):
    for i in range(len(database)):
        if(database[i]["roll_no"] == rm):
            database[i]["roll_no"] = No
            database[i]["name"] = name
            database[i]["addres"] = addres
            database[i]["contact"] = contact
            database[i]["city"] = city
            database[i]["standard"] = standard

            return "student with roll no: " + rm + " is updated"
    return "not found"


print("\nOperations used, ") 
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student""\n5.Update Student Details\n6.Exit") 

for ch in range(1,6):
    ch = int(input("Enter the choice: "))

    if(ch == 1):
        add()
        for student in database:
         print(student)
    elif(ch == 2):
        showall()
    elif(ch == 3):
        res = search(input("Enter the roll no: "))
        print(res)
    elif(ch == 4):
        res = delete(input("Enter the roll no: "))
        print("The Student with roll no "+ res +" is deleted")
        for student in database:
         print(student)
    elif(ch == 5):
        roll = input("enetr roll no to be updated: ")
        rollno = input("enter rollno: ")
        name = input("enetr name to be updated: ")
        address = input("enetr address to be updated: ")
        contact = input("enetr contact to be updated: ")
        city = input("enetr city to be updated: ")
        standard = input("enetr standard to be updated: ")
        res = update(roll, rollno, name, address, contact, city, standard)
        print(res)
        for student in database:
            print(student)
    else:
        print("Thank You!!")

    



# ask user hw many student you want to enter.
# add()
# add()
# show()

# showall()
