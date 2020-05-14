database = []


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


def show():
    global database
    for stud in database:
        print(stud["name"])
        print(stud["roll_no"])
        print(stud["addres"])
        print(stud["contact"])
        print(stud["city"])
        print(stud["standard"])


# ask user hw many student you want to enter.


add()


show()
