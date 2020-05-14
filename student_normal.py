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
    database.append(student_d)
    student_d["roll_no"] = input("enter student roll_no: ")
    database.append(student_d)
    student_d["addres"] = input("enter student address: ")
    database.append(student_d)
    student_d["contact"] = input("enter student contact: ")
    database.append(student_d)
    student_d["city"] = input("enter student city: ")
    database.append(student_d)
    student_d["standard"] = input("enter student standard: ")
    database.append(student_d)


def show():
    global database
    for stud in database:
        print(stud["name"])


# ask user hw many student you want to enter.


add()


show()